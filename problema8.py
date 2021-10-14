s=str(input('Introduceți șirul de caractere format din litere majuscule ale alfabetului latin și spațiu:  '))
s1=""
for i in s:
    if (ord(i)>=65)and(ord(i)<=89):
        s1+=chr(ord(i)+1)
    if i=='Z':
        s1+="A"
    if i==' ':
        s1+="-"
print('Șirul în care fiecare literă de la ’A’ până la ’Y’ se înlocuieşte prin următoarea literă din alfabet, fiecare literă ’Z’ se înlocuieşte prin litera ’A’ și fiecare spaţiu se înlocuieşte prin ’-’ este: \n ',s1)