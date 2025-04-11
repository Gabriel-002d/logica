# tratamento de nota invalida if nota emtre 0 a 10
#comdicional composta, entrada do usuario

nota = float(input("qual sua nota : "))

if nota <= 0 or nota > 10:
    print(" erro : nota invalida digite um valor emrtre 0 a 10")
    
elif nota >= 9:
    print(" aluno exenplar ")
    
else :
    print(" estude mais")