from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import math
import os

def convert_dms_to_dd(degrees, minutes, seconds, direction):
	decimal_degrees = degrees + (minutes / 60.0) + (seconds / 3600.0)
	if direction in ['S', 'W']:
		decimal_degrees = -decimal_degrees
	return decimal_degrees

def convert_dd_to_dms(decimal_degrees):
	degrees = int(decimal_degrees)
	decimal_minutes = (decimal_degrees - degrees) * 60.0
	minutes = int(decimal_minutes)
	seconds = (decimal_minutes - minutes) * 60.0

	if decimal_degrees < 0:
		direction = 'S' if degrees < 0 else 'W'
	else:
		direction = 'N' if degrees >= 0 else 'E'

	return abs(degrees), abs(minutes), abs(seconds), direction

def get_dji_meta(image_path):

	# Extract xmp data
	
	djimeta=["RelativeAltitude","GimbalPitchDegree","FlightYawDegree"]
	fd = open(image_path,'rb')
	d = fd.read()
	xmp_start = d.find(b'<x:xmpmeta')
	xmp_end = d.find(b'</x:xmpmeta')
	xmp_b = d[xmp_start:xmp_end+12]
	xmp_str = xmp_b.decode()
	fd.close()
    
	xmp_dict={}
	for m in djimeta:
		istart = xmp_str.find(m)
		ss=xmp_str[istart:istart+len(m)+10]
		val = float(ss.split('"')[1])
		xmp_dict.update({m : val})
		
	# Extract gps data
	
	img = Image.open(image_path)
	exif_data = img._getexif()
	
	if exif_data is not None:
		for tag, value in exif_data.items():
			tag_name = TAGS.get(tag, tag)
			if tag_name == 'GPSInfo':
				gps_info = {}
				for gps_tag, gps_value in value.items():
					gps_tag_name = GPSTAGS.get(gps_tag, gps_tag)
					gps_info[gps_tag_name] = gps_value

				latitude_data = gps_info.get('GPSLatitude', (0, 0, 0))
				longitude_data = gps_info.get('GPSLongitude', (0, 0, 0))

				latitude_dd = convert_dms_to_dd(*latitude_data, gps_info.get('GPSLatitudeRef', 'N'))
				longitude_dd = convert_dms_to_dd(*longitude_data, gps_info.get('GPSLongitudeRef', 'E'))

				xmp_dict.update({"GPSLatitude" : latitude_dd})
				xmp_dict.update({"GPSLongitude" : longitude_dd})
		
	return xmp_dict

def get_location(dji):
	dist = dji["RelativeAltitude"] / math.tan(math.radians(abs(dji["GimbalPitchDegree"]))) # dist = height / tan(gimbalPitchDegree)
	print("distance:", dist)
	y = dist * math.cos(math.radians(dji["FlightYawDegree"])) # y = dist * cos(flightYawDegree)
	x = dist * math.sin(math.radians(dji["FlightYawDegree"])) # x = dist * sin(flightYawDegree)
	print("\ny in meters:",y)
	print("x in meters:",x)
	lp = 40075.017 * 1000 * math.cos(math.radians(dji["GPSLatitude"])) # parallel_len = 40,075 * 1000 * cos(latitude)
	lm = 40007.863 * 1000 * math.cos(math.radians(dji["GPSLongitude"])) # meridian_len = 40,075 * 1000 * cos(longitude)
	
	y_degree = (360 * y) / lp # y_degree = (360 * y) / parallel_len
	x_degree = (360 * x) / lm # x_degree = (360 * x) / meridian_len
	
	# print values
	
	print("\ny in degrees: ", y_degree, convert_dd_to_dms(y_degree))
	print("x in degrees: ", x_degree, convert_dd_to_dms(x_degree))
	
	latitude = dji["GPSLatitude"] + x_degree # target_lat = latitude + x_deg
	longitude = dji["GPSLongitude"] + y_degree # target _lon = longitude + y_deg
	
	return {"GPSLatitude": latitude, "GPSLongitude": longitude}
	
# START
    
image_path = '/home/kyialbek/Projects/python_workspace/100_0140/DJI_0007.JPG'
print(os.path.basename(image_path),'\n')

dji = get_dji_meta(image_path)

location = get_location(dji)

print("\nDJI META")
print(dji)

print("\nTARGET LOCATION")
print(location)

print("\nLatitude")
degrees, minutes, seconds, direction = convert_dd_to_dms(location["GPSLatitude"])
print(f"{degrees}° {minutes}' {seconds}\" {direction}")

print("\nLongitude")
degrees, minutes, seconds, direction = convert_dd_to_dms(location["GPSLongitude"])
print(f"{degrees}° {minutes}' {seconds}\" {direction}")




