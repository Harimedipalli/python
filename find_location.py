import phonenumbers
from phonenumbers import geocoder

ph1 = phonenumbers.parse("+917569079217")

print("\nprint phone number location\n")
print(geocoder.description_for_number(ph1, "en"));
