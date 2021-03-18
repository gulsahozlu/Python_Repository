name = 'GULSAH'
surname ="OZLU "


print("My name is {} {}".format(name,surname)) #format metodu ile süslü parantez yerine name bilgisi gelecek
print("My name is {0} {1}".format(name,surname))
print("My name is {1} {0}".format(name,surname))
print("My name is {n} {s}".format(n=name,s=surname))
print("My name is {} {} and I am {} years old".format(name,surname,'25'))

age = '25'

print("My name is {} {} and I am {} years old".format(name,surname,age))
###

result = 200 / 700

print('the result is {}'.format(result))
print('the result is {r:1.3}'.format(r=result))  # 3 bilgisi virgülden sonra kaç basamak olacağını söyler
print('the result is {r:10.4}'.format(r=result))  #10 ise is'den sonra kaç karakterlik boşluk bırakılacağını söyler


###

isim = 'GULSAH'
soyisim ='OZLU'
yas='25'

print(f"My name is {isim} {soyisim} and I'm {yas} years old ") #fstring ile süslü parantez içine direkt degisken isimlerini yazabiliriz

