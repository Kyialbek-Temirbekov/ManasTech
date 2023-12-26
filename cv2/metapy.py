import exifread

def read_exifread_metadata(image_path):
    try:
        with open(image_path, 'rb') as f:
            exif_data = exifread.process_file(f)
            if exif_data:
                print("ExifRead metadata:")
                for tag, value in exif_data.items():
                    print(f"{tag}: {value}")
            else:
                print("No ExifRead metadata found.")
    except Exception as e:
        print(f"Error (ExifRead): {e}")

# Replace 'your_image.jpg' with the path to your image file
image_path = '/home/kyialbek/Projects/python_workspace/drone_pictures/DJI_0002.JPG'

# Read metadata using ExifRead
read_exifread_metadata(image_path)


