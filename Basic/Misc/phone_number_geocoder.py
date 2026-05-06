import phonenumbers,random
from phonenumbers import geocoder
generated_number = random.randint(1000000000, 9999999999)
print("Generated Phone Number:", generated_number)
phone = phonenumbers.parse("+91" + str(generated_number))
print(geocoder.description_for_number(phone,"en"))
    