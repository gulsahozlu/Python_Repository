name ='gulsah'
surname='ozlu'
age = '25'
greeting = 'My name is ' + name + '  ' + surname + ' and \nI am ' + age + ' years old'

length = len(greeting) #greeting stringinin kaç karakterden olustugunu bul

print(greeting)
print(greeting[0])
print(greeting[3])
print(len(greeting)) #kaç karakterten olusuyor
print(greeting[length-1])#sonuncu karakteri gösterir

print(greeting[-1]) # bu da alternatif olarak sopn karakteri verir

print(greeting[3:7]) #3.indexten başla 7.i indexe kadar git
print(greeting[3:]) #3.indexten başla sonuna kadar yazdır
print(greeting[:15]) #baştan başla 15. indexe kadar yaz
print(greeting[2:40:4])  #2. indexten itibaren 4 karakterde bir 40. indexe kadar yazdır
