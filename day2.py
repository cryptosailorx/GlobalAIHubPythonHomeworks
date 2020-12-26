#◘liste oluşturuldu
userlist=list()

#isim girilmesi istendi
name= input("Please enter your name:")

#girilen isim listeye eklendi.
userlist.append(["Name", name])

#soyisim girilmesi istendi
surname= input("Please enter your surname:")

#girilen soyisim listeye eklendi.
userlist.append(["Surname", surname])

#yas girilmesi istendi.
age= int(input("Please enter your age:"))

#girilen yaş listeye eklendi.
userlist.append(["Age", age])

#doğum yılı girilmesi istendi
birthdate= int(input("Please enter your birthdate:"))

#doğumyılı listeye eklendi.
userlist.append(["Birtdate", birthdate])

#for döngüsü ile liste içindeki elemanlara ekrana bastırıldı.
for i in userlist:
    print(f" {i[0]},{i[1]}.")

#liste içindeki yaş değerine göre sokağa çıkış kontrolğ yapıldı.    
for i in userlist:
    if i[0] == "Age" or i[0]== "age":
        if i[1]>18:
        
            print("You can go out to the street.")
        
        else:
        
            print("You can't go out because it's too dangerous.")
   

 