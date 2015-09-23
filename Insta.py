from instagram.client import InstagramAPI
import urllib, io
from PIL import Image

urls = []

count = "10" 
lat = "51.507606"
lng = "-0.111370"
min_timestamp = "1442994611"
max_timestamp = "1443001813"

api = InstagramAPI(client_id = "XXXX", client_secret = "XXXX", )
lat_media = api.media_search(count=100,lat=lat,lng=lng,min_timestamp=min_timestamp,max_timestamp=max_timestamp,distance=500)
for media in lat_media:
    urls.append(media.images['standard_resolution'].url)

for URL in urls:
	print URL
	fd = urllib.urlopen(URL)
	image_file = io.BytesIO(fd.read())
	im = Image.open(image_file)
	im.show()

