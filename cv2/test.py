from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def convert_dms_to_dd(degrees, minutes, seconds, direction):
    decimal_degrees = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if direction in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def extract_exif_data(image_path):
    # Open the image
    img = Image.open(image_path)

    # Extract Exif data
    exif_data = img._getexif()

    if exif_data is not None:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)

            # Check if the tag represents GPS information
            if tag_name == 'GPSInfo':
                gps_info = {}
                for gps_tag, gps_value in value.items():
                    gps_tag_name = GPSTAGS.get(gps_tag, gps_tag)
                    gps_info[gps_tag_name] = gps_value

                # Convert latitude and longitude to decimal degrees
                latitude_data = gps_info.get('GPSLatitude', (0, 0, 0))
                longitude_data = gps_info.get('GPSLongitude', (0, 0, 0))

                latitude_dd = convert_dms_to_dd(*latitude_data, gps_info.get('GPSLatitudeRef', 'N'))
                longitude_dd = convert_dms_to_dd(*longitude_data, gps_info.get('GPSLongitudeRef', 'E'))

                print("Latitude (Decimal Degrees):", latitude_dd)
                print("Longitude (Decimal Degrees):", longitude_dd)

# Example usage
image_path = '/home/kyialbek/Projects/python_workspace/100_0140/DJI_0001.JPG'
extract_exif_data(image_path)




