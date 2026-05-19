##  Camera Auto-Transfer & Timestamp Script

A lightweight, automated Python script designed to streamline the process of transferring photos from your digital camera to your PC while adding a customizable, nostalgic retro/digital date stamp. 

Unlike basic image editors, this script dynamically scales the font size based on each photo's resolution and ensures that your original metadata (EXIF) remains perfectly intact.

### Features

- **Smart On-Demand Processing:** Only processes and transfers **new** photos. If a photo has already been imported, it skips it to save time and storage.
- **Dynamic Font Sizing:** Automatically calculates the font size based on the image's height (set to 4.5%). Whether it's a low-res snap or a high-megapixel shot, the timestamp remains perfectly proportioned.
- **EXIF Data Preservation:** Uses `piexif` to dump and rewrite original camera metadata (camera model, shutter speed, GPS, etc.) into the newly saved stamped image.
- **Authentic Retro Aesthetics:** Uses the **Share Tech Mono** font with a custom shadow effect and a bright digital yellow tint to mimic old-school cyber-shot/vizor displays.
- **Zero Background Overhead:** Designed to run as a single execution (on-demand) rather than constantly polling in the background, keeping your CPU free.

### Prerequisites & Dependencies

Before running the script, make sure you have Python installed along with the following libraries:
```
pip install Pillow piexif
```

### How to Use

1.**Configure the Paths: Open the file and modify the top variables according to your system setup:**
```
SOURCE_FOLDER = r"D:\DCIM\101MSDCF"  # Your camera's SD card directory
DEST_FOLDER = r"C:\Users\...\Desktop\cybershot"  # Target PC folder
FONT_PATH = r"C:\Users\...\Desktop\ShareTechMono-Regular.ttf"
```
2.**Run the Script**


### License

This project is open-source and free to use.
