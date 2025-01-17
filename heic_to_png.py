import os
import pillow_heif
from PIL import Image

def convert_heic_to_png(input_folder, output_folder):
    # List all files in the input directory
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            heic_file_path = os.path.join(input_folder, filename)
            
            # Open and convert the HEIC file to PNG
            heif_file = pillow_heif.open_heif(heic_file_path)
            image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)
            
            # Save the file as PNG in the output folder
            png_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")
            image.save(png_file_path, "PNG")
            print(f"Converted {filename} to {os.path.basename(png_file_path)}")

if __name__ == "__main__":
    input_folder = "heic_input_folder"  # Change this to the directory where your HEIC files are located
    output_folder = "png_output_folder"  # Change this to the desired output directory where the PNG files will be saved
    os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist
    convert_heic_to_png(input_folder, output_folder)