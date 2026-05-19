import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import piexif

SOURCE_FOLDER = r"D:\DCIM\101MSDCF"  #your camera's default folder for photos
DEST_FOLDER = r"C:\Users\...\Desktop\cybershot" #where you want the processed photos to be saved
FONT_PATH = r"C:\Users\...\Desktop\ShareTechMono-Regular.ttf" #make sure to get it from google fonts or use default fonts
FONT_SIZE = 100 
TEXT_COLOR = (255, 255, 0) #yellow

Path(DEST_FOLDER).mkdir(parents=True, exist_ok=True)
processed_count = 0

def add_date_stamp(input_path, output_path): 
    with Image.open(input_path) as img:
        if "exif" not in img.info:
            print(f"no EXIF: {input_path.name}")
            return False
        
        exif_dict = piexif.load(img.info["exif"])

        try:
            raw_date = exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal]
            raw_date = raw_date.decode()
        except KeyError:
            print(f"no date info: {input_path.name}")
            return False
        
        #edit date format as you like
        date = raw_date.split(" ")[0]   
        y, m, d = date.split(":")
        formatted = f"{d}/{m}/{y[-2:]}'" 

        draw = ImageDraw.Draw(img)
        
        #dynamic font sizing
        dynamic_font_size = int(img.height * 0.045) # slightly increased the font size
        try:
            font = ImageFont.truetype(FONT_PATH, dynamic_font_size)
        except OSError:
            #fallback to base size if font not found
            print(f"Warning: Font not found at {FONT_PATH}, using fallback size.")
            font = ImageFont.truetype("arial.ttf", FONT_SIZE)

        bbox = draw.textbbox((0, 0), formatted, font=font)  
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        #position the text at the bottom right corner with generous padding based on font size
        padding_x = int(dynamic_font_size * 2.2) 
        padding_y = int(dynamic_font_size * 1.5) # increased to move text a bit higher
        x = img.width - text_width - padding_x
        y = img.height - text_height - padding_y

        shadow_offset = int(dynamic_font_size * 0.05)
        # dynamically calculate stroke thickness to make the font bolder
        text_thickness = max(1, int(dynamic_font_size * 0.015)) 
        
        draw.text((x + shadow_offset, y + shadow_offset), formatted, font=font, fill=(0, 0, 0), stroke_width=text_thickness, stroke_fill=(0, 0, 0)) 
        draw.text((x, y), formatted, font=font, fill=TEXT_COLOR, stroke_width=text_thickness, stroke_fill=TEXT_COLOR) 
        
        try:
            exif_bytes = piexif.dump(exif_dict)
            img.save(output_path, quality=95, exif=exif_bytes)
        except Exception as e:
            img.save(output_path, quality=95)
            
    print(f"successful: {input_path.name}")
    return True

print("starting...\n")

if os.path.exists(SOURCE_FOLDER):
    for file in Path(SOURCE_FOLDER).iterdir():
        if file.suffix.lower() in [".jpg", ".jpeg"]:
            output_file = Path(DEST_FOLDER) / file.name
            
            #only process new files
            if not output_file.exists():
                try:
                    if add_date_stamp(file, output_file):
                        processed_count += 1
                except Exception as e:
                    print(f"error ({file.name}): {e}")
            else:
                 print(f"already in dir: {file.name}")
else:
    print(f"error: cannot find {SOURCE_FOLDER}. make sure path exists.")

print(f"\ncompleted! total {processed_count} new photos.")
input("enter to close")
