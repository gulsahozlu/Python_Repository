#Python da değişken tanımlarken mutlaka içine değer atamalısı
#yoksa degişken tanımlaması yapamazsın

customer_Name    = 'Gulsah'
customer_Surname = 'Ozlu'
customer_NameSurname = customer_Name + " " + customer_Surname
print(customer_NameSurname)
customer_Gender = True #kadın
customer_TCno =  '123456789'
customer_BirthYear = 1989
customer_Address = "Trabzon Ortahisar"
customer_Age = 2021 - customer_BirthYear

print(customer_Age)


"""Asagıdaki siparişlerin toplam bilgisini hesapla

Sipariş 1 => 110 TL
Sipariş 2 => 1100.5
Sipariş 3 => 356.95
"""
order1 = 110
order2= 1100.5
order3= 356.95
total = order1 + order2 + order3
print("TOTAL :" , total )