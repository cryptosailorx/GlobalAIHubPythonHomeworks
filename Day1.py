#Program açılış bilgilendirilmesi
print("The information you provide will be translated from English to Turkish.")

#İsim girişi
name = input("Please enter your Name:")

#Soyisim girişi
surname = input("Please enter your Surname:")

#Yaş girişi string e cevrilecek
age = float(input("Please enter your Age:"))
     
#Medeni durum girişi
maritalstatus = input("Please enter your Marital status:")

#konuşulabilen bir dil girişi
language = input("Please enter a language you can speak:")

# İsim ve Soyisim girişinin f-print metodu ile yazdırılması
print(f' Hello {name} {surname}.')

#Medeni durum, yaş ve konuşulabilen bir dilin format metodu ile yazdırılması
print(" Your Marital Status is {}, you are {} years old and you can speak {}.".format(maritalstatus, age, language))

#5 adet input ile alınan verinin format metodu ile type' larının ekrana yazdırılması
print("Name type : {} \nsurname type : {} \nAge type : {} \nmaritalstatus type : {} \nlanguage type : {}".format(type(name), type(surname), type(age), type(maritalstatus), type(language)))