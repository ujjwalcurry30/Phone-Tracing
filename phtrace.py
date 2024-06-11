import phonenumbers
from phonenumbers import geocoder
#from test import number
import folium

key = "b319cc5618624de092a44a3bb6a14c39"
number = input("Enter Phone Number with Country Code :")
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)


from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = (number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)


map_location = folium.Map(location = [lat,lng], zoom_start = 7)
folium.Marker([lat,lng] ,popup=number_location).add_to(map_location)
map_location.save("mylocation.html")
