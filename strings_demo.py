
website = "https://www.twitter.com/home"
course ="Python Kursu : Baştan Sona Python Programlama Rehberi (40 saat)"

#1- 'course' karakter dizisindeki karakter sayısı

course_length = len(course)
print(course_length)

#2- 'website' içinden www karakterlerini alınız

array= website[8:11]
print(array)

#3-'website' içinden com karakterlerini alın
array2= website[20:23]
print(array2)

#4-course içinden ilk 15 ve son 15 karakteri alın

array3= website[:15]
print(array3)

array4= website[15:]
print(array4)

#5-course ifadesindeki karakterleri tersten yazdırın

print(course[::-1])  #diziyi tersten yazdırma
print(course[::2])
#course ="Python Kursu : Baştan Sona Python Programlama Rehberi (40 saat)"
# P karakteri soldan bakınca bizim için 0. karaktere denk geliyor. Fakat sağdan bakınca negatif bir değere 
#karşılık gelir. yani en sondaki ')' karakter -1. karakterdir
###

#6-
name, surname, age, job = "Gulsah", "Ozlu", 25, "muhendislik"
 
result = "Benim adım " + name+ " " + surname+ " Yaşım " + str(age) + " " + "Ve benim mesleğim "+ job
print(result)

#OR

result = "Benim adım {} {}, Yaşım {} ve Mesleğim {}. ".format(name,surname,age,job)
print(result)

#OR

result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"
print(result)

#7- 

s="Bilgisayar mühendisliği"

s = s[0:11] + 'M' + s[-11:] 
print(s)
