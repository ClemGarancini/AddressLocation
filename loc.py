import geopy.geocoders
from geopy.geocoders import Nominatim
import ssl
import certifi

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

geolocator = Nominatim(user_agent="adele_app", scheme="http")
location = geolocator.geocode("175 5th Avenue NYC")

print(location.address)
print((location.longitude, location.latitude))
print(location.raw)
