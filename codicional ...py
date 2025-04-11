nota1 = float(input("digite a primeira nota:  "))

nota2 = float(input("digite a segunda nota:  "))

media = (nota1 + nota2)/2
print(media)

if media <=0 or media > 10:
   print(" erro : imsira uma nota de 0 a 10 nos espacos")

elif media >=9:
  print("passoun com merito")

elif media >=8:
   print("passou como se esperava")
   
elif media >=7:
   print(" estude criatura, que chamo de filho ")

elif media >= 6:
   print(" qual e")
else:
   print(" reprovado, estude maios, filho")
   