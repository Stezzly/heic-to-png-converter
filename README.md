
# HEIC to PNG Converter

This Python script allows you to convert HEIC (High Efficiency Image Format) images to the more widely supported PNG format. It's perfect for users with HEIC images from Apple devices who need them in a more compatible format.

## Features

- Batch conversion of HEIC images to PNG format.
- User-friendly: simply specify the folder containing your HEIC files.
- Preserves image quality during conversion.

## Requirements

- Python 3.x
- Pillow library: `pip install Pillow`
- pillow-heif library: `pip install pillow-heif`

## Usage

1. **Installation:**
   Install the required libraries using pip:

   ```bash
   pip install Pillow pillow-heif
   ```

2. **Download and Run the Script:**
   * Clone the repository:

   ```bash
   git clone https://github.com/Stezzly/heic-to-png-converter.git
   ```

   * Navigate to the project directory:

   ```bash
   cd heic-to-png-converter
   ```

   * Open the script `heic_to_png.py` and locate the `input_folder` variable. Set it to the path containing your HEIC files.

   * Run the script:

   ```bash
   python heic_to_png.py
   ```

3. **Converted Files:**
   The converted PNG files will be saved in a subfolder named `converted_pngs` within the same folder as your HEIC images.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
