from faker import Faker

fake = Faker("tr_TR")
adet = int(input("Kaç adet test kullanıcısı üretilsin?: "))

for i in range(1, adet + 1):
    print(f"{i}. İsim: {fake.name()} | Tel: {fake.phone_number()} | E-posta: {fake.email()} | Şehir: {fake.city()}")