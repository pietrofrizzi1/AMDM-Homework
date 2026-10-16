if __name__ == '__main__':
    print("Hello, World!")





#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2==1:
    print("Weird")
else:
    if 2<=n<=5:
        print("Not Weird")
    else:
        if 6<=n<=20:
            print("Weird")
        else:
            print("Not Weird")





if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
print(a-b)
print(a*b)



if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/b) 




if __name__ == '__main__':
    n = int(input())
if n>0:
    i=0
    while i<n:
        print(i*i)
        i=i+1





def is_leap(year):
    leap = False
    
    if year%4==0:
        leap= True
        if year%100==0:
            leap = False
            if year%400==0:
               leap=True
    
    return leap

year = int(input())
print(is_leap(year))





if __name__ == '__main__':
    n = int(input())
i=1
stringa=""
while (i)<=n:
    stringa=stringa + str(i)
    i=i+1
print(stringa)
    



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
vettore=[]
for i in range(0,x+1):
  for o in range(0,y+1):
    for p in range(0,z+1):
        
        if p+o+i!=n:
          vettore.append([i,o,p])
print(vettore)






if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


arr=list(arr)

arr=list(set(arr))
arr.sort(reverse=True)

print(arr[1])




if __name__ == '__main__':
    listone=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dizionario=[name,score]
        listone.append(dizionario)
min=100
for o in range(len(listone)):
 
 if listone[o][1]<min:
    min=listone[o][1]
    

secondo=[100]
nomi=[]
for p in range(len(listone)):
 
 if listone[p][1]>min:
    if listone[p][1]==secondo[0]:
        secondo.append(listone[p][1])
        nomi.append(listone[p][0])
    if listone[p][1]<secondo[0]:
        secondo=[listone[p][1]]
        nomi=[listone[p][0]]
    
    





if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    

obiettivo=student_marks[query_name]
final=round((obiettivo[0]+obiettivo[1]+obiettivo[2])/3, 2)
print(f"{final:.2f}")





if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
lista=list(integer_list)


tupla=tuple(lista)

print(hash(tupla))





def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)





#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print("Hello "+first+" "+last+"! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)







def mutate_string(string, position, character):
    rosita=list(string)
    rosita[position]=character
    finale=''.join(rosita)
    return finale

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)




def count_substring(string, sub_string):
    string=list(string)
    sub_string=list(sub_string)
    vero=0
    conta=0
    for i in range(len(string)-len(sub_string)+1):
        
        for o in range(len(sub_string)):
           
           if string[i+o]==sub_string[o]:
             conta=conta+1
        if conta==len(sub_string):
            vero=vero+1
        conta=0
    
       
    return vero

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)





if __name__ == '__main__':
    s = input()

lisa=list(s)
vero=0
for i in range(len(lisa)):
    if lisa[i].isalnum():
        vero=1
if vero==1:
    print(True)
else:
    print(False)

vero=0
for i in range(len(lisa)):
    if lisa[i].isalpha():
        vero=1
    
if vero==1:
    print(True)  
else:
    print(False)
  
vero=0
for i in range(len(lisa)):
    if lisa[i].isdigit():
        vero=1
if vero==1:
    print(True)
else:
    print(False)
  
vero=0
for i in range(len(lisa)):
    if lisa[i].islower():
        vero=1
if vero==1:
    print(True)
else:
    print(False)
    
vero=0  
for i in range(len(lisa)):
    if lisa[i].isupper():
        vero=1
if vero==1:
    print(True)
else:
    print(False)








#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))








import textwrap

def wrap(string, max_width):
    lista=list(string)
    lunghezza=len(lista)
    counter=0
    totale=""
    while lunghezza>0:
        parola=""
        for i in range (max_width):
            if counter<len(lista):
              parola=parola+lista[counter]
              
              counter=counter+1
        
        totale=totale+parola+"\n"
        lunghezza=lunghezza-max_width
    return totale
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)











#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max=candles[0]
    total=0
    for i in range(len(candles)):
      
      if candles[i]==max:
        
        total=total+1
        
      if candles[i]>max:
        total=1
        max=candles[i]
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()










#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if x1>x2 and v1>=v2:
        risultato="NO"
        return risultato
    
    if x2>x1 and v2>=v1:
        risultato="NO"
        return risultato
    posizione1=x1
    posizione2=x2
    risultato="NO"    
    if x1>x2:
        if posizione1==posizione2:
                risultato="YES"
                return risultato
        
        while(posizione1>posizione2):
            
            posizione1=posizione1+v1
            posizione2=posizione2+v2
        if posizione1==posizione2:
                risultato="YES"
                return risultato
    
    if x2>x1:
        if posizione1==posizione2:
                
                risultato="YES"
                return risultato
        while(posizione2>posizione1):
            
            posizione1=posizione1+v1
            posizione2=posizione2+v2
        
        if posizione1==posizione2:
                risultato="YES"
                return risultato
        
        
    
    
    
    
    return risultato

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()







#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    total=5
    
    somma=0
    for i in range(0,n):
        total=math.floor(total/2)
        somma=somma+total
        print(total)
        total=total*3
      
        
    return somma

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()






#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    
    cifra=n
    
    cifra = list(map(int, cifra))
    
    
    iniziale= ricorsiva(cifra)
    iniziale=int(iniziale[0])
    cifra2=str(iniziale)*k
    
    cifra2 = list(map(int, cifra2))
    finale=ricorsiva(cifra2)
    
    finale=int(finale[0])
    return finale
    
    
def ricorsiva(cifra):
    totale=0
    if len(cifra)==1:
        return cifra
    totale=sum(cifra)
    totale = list(map(int, str(totale)))
    
    return ricorsiva(totale)
       
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()






#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    
    numerino=arr[n-1]
    for i in range(len(arr)-2,-1,-1):
        
        if arr[i]<numerino:
            arr[i+1]=numerino
            parola=""
            for p in range(len(arr)):
                parola=parola+str(arr[p])+" "
            print(parola)
            break
        if arr[i]>numerino:
            arr[i+1]=arr[i]
            if i==0:
                parola=""
                for o in range(len(arr)):
                    parola=parola+str(arr[o])+" "
                print(parola)
                arr[i]=numerino
        parola=""
        
        for a in range(len(arr)):
            parola=parola+str(arr[a])+" "
        print(parola)
    
    return True
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)







#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(len(arr)-1):
        if arr[i]<=arr[i+1]:
            parola=""
                
            for a in range(len(arr)):
                parola=parola+str(arr[a])+" "
            print(parola)
            continue
        else:
            for o in range(i,-1,-1):
                if arr[o]<arr[o+1]:
                    
                    break
                   
                if arr[o]>=arr[o+1]:
                   vecchio=arr[o]
                   arr[o]=arr[o+1]
                   arr[o+1]=vecchio
                
                
        parola=""
            
        for a in range(len(arr)):
            parola=parola+str(arr[a])+" "
        print(parola)                
    
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)








def swap_case(s):
    s=list(s)
    for e in range(len(s)):
      s[e]=s[e].swapcase()
    s=''.join(s)
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)









def print_formatted(number):
    
    bina=0
    ex=0
    octa=0
    lunghezza=0
    max=len(str(bin(number)[2:]))
    
    for i in range(1,number+1):
        bina=bin(i)[2:]
        octa=str(oct(i)[2:])
        ex=str(hex(i)[2:]).upper()
        
        lunghezza=max
        print(" "*(lunghezza-len(str(i)))+str(i)+" "*(lunghezza-len(octa)+1)+octa+" "*(lunghezza-len(ex)+1)+ex+" "*(lunghezza-len(str(bina))+1)+str(bina))
        
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)











#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s=list(s)
    print(s)
    for i in range(len(s)):
        print(s[i])
        if s[i]==' ':
            s[i+1]=s[i+1].upper()
    s[0]=s[0].upper()
    s=''.join(s)
    print(s)
    return s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)










def minion_game(string):
    lista=list(string)

    totalevocali=0
    totaleconsonanti=0
    for i in range(len(lista)):
        if lista[i].lower() in "aeiou":
            totalevocali=totalevocali+(len(lista)-i)
        else:
            totaleconsonanti=totaleconsonanti+(len(lista)-i)
    if totalevocali>totaleconsonanti:
        print("Kevin"+" "+str(totalevocali))
    else:
        if totalevocali==totaleconsonanti:
            print("Draw")
        else:
            print("Stuart "+ str(totaleconsonanti))
    
    
if __name__ == '__main__':
    s = input()
    minion_game(s)










def print_rangoli(size):
    
    alfabeto=["a","b","c","d","e","f","g","h","i","j","k",
    "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    parola=[]
    zero=0
    conta=0
    lunghezza=size+size-1+(size*2-2)
    size=size-1
    
    numero=0
    for riga in range(size*2+1):
        zero=0
        conta=0
        if riga<size+1:
          numero=numero+1
        else:
            numero=numero-1
        
        for element in range(lunghezza):
           
           if element<((lunghezza-(4*numero-3))/2):
              parola.append("-")
              continue
           if element>((lunghezza-(4*numero-3))/2)+(4*numero-3):
              parola.append("-")
              continue
           
           if element%2==0:
                    if zero==1:
                        conta=conta-1
                        parola.append(alfabeto[size-conta])
                    else:
                        parola.append(alfabeto[size-conta])
                        conta=conta+1
                        if conta==numero:
                            conta=conta-1
                            zero=1
                    
           else:
                    parola.append("-")
        parola="".join(parola)
        print(parola)
        parola=[]

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)













def average(array):
    sette=set(array)
    
    media=round(sum(sette)/len(sette), 3)
    return media

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)





# Enter your code here. Read input from STDIN. Print output to STDOUT
M=input()
numeriM=input()
set1=list(map(int, numeriM.split()))
set1=set(set1)

N=input()
numeriN=input()
set2=list(map(int, numeriN.split()))
set2=set(set2)

unici1=set1.difference(set2)
unici2=set2.difference(set1)
finale=unici1.union(unici2)
finale=list(finale)
finale.sort()
for element in range(len(finale)):
    print(finale[element])









# Enter your code here. Read input from STDIN. Print output to STDOUT
lunghezze=input()
lista=input()
set1=input()
set2=input()
lista=list(map(int,lista.split()))
set1=set(map(int,set1.split()))
set2=set(map(int,set2.split()))
felicita=0
for element in range(len(lista)):
    if lista[element] in set1:
        felicita=felicita+1
    if lista[element] in set2:
        felicita=felicita-1
print(felicita)        










N, M = map(int, input().split())


for i in range(N // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))


print("WELCOME".center(M, "-"))


for i in range(N // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))












def merge_the_tools(string, k):
    
    for i in range(0, len(string), k):
        blocco = string[i:i+k]

        risultato = ""

        for carattere in blocco:
            if carattere not in risultato:
                risultato += carattere

        print(risultato)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)












import calendar
nomegiorni=calendar.day_name
lista=input()
lista=list(map(int, lista.split()))
mese=lista[0]
giorno=lista[1]
anno=lista[2]
numero=calendar.weekday(anno,mese,giorno)
print(nomegiorni[numero].upper())















#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    formato = "%a %d %b %Y %H:%M:%S %z"

    data1 = datetime.strptime(t1, formato)
    data2 = datetime.strptime(t2, formato)

    differenza = abs(data1 - data2)
    

    return str(int(differenza.total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()










# Enter your code here. Read input from STDIN. Print output to STDOUT
numero=input()
numero=int(numero)
for i in range(numero):
  valore=input()
  valore=list(map(str,valore.split()))
  valore1=valore[0]
  valore2=valore[1]
  
  try:
    valore1=int(valore1)
    valore2=int(valore2)
    divisione=valore1/valore2
    print(int(divisione))
  except ValueError as e:
    print("Error Code:",e)
  except ZeroDivisionError as e:
    print("Error Code: integer division or modulo by zero")
    










cube = lambda x: x*x*x

def fibonacci(n):
    lista=[]
    if n==0:
        return lista
    lista.append(0)
    if n==1:
        return lista
    lista.append(1)
    
    for e in range(n-2):
      valore=lista[e]+lista[e+1]
      lista.append(valore)
    
    return lista
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))










# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X= input()
sizes= input()
sizes=list(sizes.split())
conta=Counter(sizes)

N=input()

clienti=[]
for e in range(int(N)):
  clienti.append(input())

for o in range(len(clienti)):
    clienti[o]=clienti[o].split()

guadagno=0
for element in range(len(clienti)):
    numero=clienti[element][0]
    try:
        if conta[numero]>0:
            
            guadagno=guadagno+int(clienti[element][1])
            conta[numero]=conta[numero]-1
    except:
        continue
        
print(guadagno)










from collections import defaultdict
d = defaultdict(lambda: 0)
n=input()
n=n.split(" ")

m=int(n[1])
n=int(n[0])


parole1=[]

parole2=[]
for e in range(n):
    parole1.append(input())
    d[parole1[e]]+=1

d.default_factory = lambda: -1
for i in range(m):
    parole2.append(input())
    if d[parole2[i]]==-1:
        print(-1)
        continue
    for element in range(len(parole1)):
        
        if parole1[element]==parole2[i]:
            print(element+1,end=" ")
    print()










# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
english=input()
b=input()
french=input()
english=list(map(int, english.split(" ")))

french=list(map(int, french.split(" ")))
conta=0
for element in range(len(french)):
    if french[element] in english:
        conta+=1
print(conta)         










if __name__ == '__main__':
    N = int(input())
    comandi=[]
    for i in range(N):
        comandi.append(input())
    
lista=[]
for element in range(len(comandi)):
    comandi[element]=comandi[element].split(" ")
    
    if comandi[element][0]=="insert":
        lista.insert(int(comandi[element][1]),int(comandi[element][2]))
    if comandi[element][0]=="print":
        print(lista)
    if comandi[element][0]=="remove":
        lista.remove(int(comandi[element][1]))
    if comandi[element][0]=="append":
        lista.append(int(comandi[element][1]))
    if comandi[element][0]=="sort":
        lista.sort()
    if comandi[element][0]=="pop":
        lista.pop()
    if comandi[element][0]=="reverse":
        lista.reverse()
    









N=int(input())
countries=[]
conta=set()
for i in range(N):
    countries.append(input())
    conta.add(countries[i])
print(len(conta))  














n = int(input())
s = set(map(int, input().split()))
N=int(input())
azioni=[]
for i in range(N):
    azioni.append(input())
for element in range(len(azioni)):
    comando=azioni[element].split()
    if comando[0]=="remove":
        s.remove(int(comando[1]))
    if comando[0]=="discard":
        s.discard(int(comando[1]))
    if comando[0]=="pop":
        s.pop()
        
print(sum(s))












n=int(input())
inglese=input()
inglese=inglese.split(" ")
b=int(input())
francese=input()
francese=francese.split(" ")
inglese=set(inglese)
francese=set(francese)    
finale=inglese.union(francese)
print(len(finale))        












n=int(input())
inglese=input()
inglese=inglese.split(" ")
b=int(input())
francese=input()
francese=francese.split(" ")
inglese=set(inglese)
francese=set(francese)    
finale=inglese.difference(francese)
print(len(finale))        















n=int(input())
inglese=input()
inglese=inglese.split(" ")
b=int(input())
francese=input()
francese=francese.split(" ")
inglese=set(inglese)
francese=set(francese)    
finale=inglese.symmetric_difference(francese)
print(len(finale))        











T=int(input())
for i in range(T):
    A=int(input())
    primo=input()
    primo=primo.split(" ")
    B=int(input())
    secondo=input()
    secondo=secondo.split(" ")
    primo=set(primo)
    secondo=set(secondo)
    print(primo.issubset(secondo))






capo=input()
capo=capo.split(" ")
capo=set(capo)
n=int(input())
altri=[]
for e in range(n):
    modifica=input()
    modifica=modifica.split(" ")
    modifica=set(modifica)
    altri.append(modifica)
conta=0    
for element in range(len(altri)):
    if (capo>altri[element]):
        conta+=1
if conta==len(altri):
    print(True)
    
else:
    print(False)











K = int(input())
stanze = list(map(int, input().split()))

singole = set(stanze)

capitano = (sum(singole)*K - sum(stanze))//(K - 1)

print(capitano)






n = int(input())
A = set(map(int, input().split()))

N = int(input())

for i in range(N):
    operation, length = input().split()
    other_set = set(map(int, input().split()))

    if operation == "intersection_update":
        A.intersection_update(other_set)

    if operation == "update":
        A.update(other_set)

    if operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

    if operation == "difference_update":
        A.difference_update(other_set)

print(sum(A))









T = int(input())

for _ in range(T):
    a, b = input().split()

    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)






N,X=input().split()
N=int(N)
X=int(X)

voti=[]
for element in range(X):
    voti.append(map(float,input().split()))
zippate=zip(*voti)
zippate=list(zippate)
for e in range(len(zippate)):
    
    print(round(sum(list(zippate[e]))/X,1))
    
    





#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input())
    arr.sort(key=lambda x: x[k])
   
    
    for element in range(len(arr)):
        lista=list(map(str,arr[element]))
        print(" ".join(lista))













S = input()
S = list(S)


S.sort(key=lambda x: (
    0 if x.islower() else
    1 if x.isupper() else
    2 if x.isdigit() else 3,
    1- int(x) % 2 if x.isdigit() else 0,
    x
))
S = "".join(S)
print(S)










from collections import OrderedDict
N=int(input())
totale=OrderedDict()
for element in range(N):
    lista=input().split(" ")
    name=" ".join(lista[0:-1])
    prezzo=int(lista[-1])
    totale[name]=totale.get(name, 0)+prezzo
for chiave, valore in totale.items():
    print(chiave, valore)













n = int(input())
totale = {}

for _ in range(n):
    parola = input()
    totale[parola] = totale.get(parola, 0) + 1

print(len(totale))
print(*totale.values())










from collections import deque
N=int(input())
azioni=[]
d=deque()
for i in range(N):
    azioni.append(input())
for element in range(len(azioni)):
    comando=azioni[element].split()
    if comando[0]=="append":
        d.append(int(comando[1]))
    if comando[0]=="appendleft":
        d.appendleft(int(comando[1]))
    if comando[0]=="pop":
        d.pop()
    if comando[0]=="popleft":
        d.popleft()
        
print(" ".join(list(map(str,d))))





n = int(input())
s = set(map(int, input().split()))
N=int(input())
azioni=[]
for i in range(N):
    azioni.append(input())
for element in range(len(azioni)):
    comando=azioni[element].split()
    if comando[0]=="remove":
        s.remove(int(comando[1]))
    if comando[0]=="discard":
        s.discard(int(comando[1]))
    if comando[0]=="pop":
        s.pop()
        
print(sum(s))





#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    s=list(s)
    c=list(set(s))
    s.sort()
    d={}
  
    for element in range(len(c)):
        d[c[element]]=s.count(c[element])
    
    ordinato = sorted(d.items(), key=lambda x: (-x[1],x[0]))
    for n in range(3):
        print(ordinato[n][0],ordinato[n][1])








from collections import namedtuple

n = int(input())
columns = input().split()

Student = namedtuple('Student', columns)

total = 0

for _ in range(n):
    data = input().split()
    student = Student(*data)
    total += int(student.MARKS)

print(f"{total / n:.2f}")










from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))

    top = float('inf')
    possible = True

    while blocks:
        if blocks[0] >= blocks[-1]:
            cube = blocks.popleft()
        else:
            cube = blocks.pop()

        if cube > top:
            possible = False
            break

        top = cube

    print("Yes" if possible else "No")









import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    
    
    score=0
    for element in node.iter():
        score += len(element.attrib)
        

    return score

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))















import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    level=level+1
    global maxdepth
    maxdepth=max(level,maxdepth)
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)









def wrapper(f):
    def fun(l):
        tutti=[]
        for e in range(len(l)):
           utile= l[e][-10:]
           tutti.append("+91"+" "+utile[:5]+" "+utile[5:])
           
        return f(tutti)   
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 









import operator

def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        return [f(person) for person in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')








import numpy

def arrays(arr):
    arr=list(map(float,arr))
    arr.reverse()
    
    arr=numpy.array(arr)
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)





import numpy
lista=input().split()
lista=list(map(int,lista))

lista=numpy.array(lista)
print(numpy.reshape(lista,(3,3)))





import numpy
N,M=input().split()
lista=[]
for element in range(int(N)):
    lista.append(list(map(int, input().split())))
lista=numpy.array(lista)    
    
    

print(numpy.transpose(lista))
print(lista.flatten())





import numpy



M,N,P=input().split()
array1=[]
array2=[]
for element in range(int(N)):
    array1.append(list(map(int,input().split())))
for element in range(int(M)):
    array2.append(list(map(int,input().split())))
array1=numpy.array(array1) 
array2=numpy.array(array2)
 
print(numpy.concatenate((array1,array2),axis=0))













import numpy

array=list(map(int,input().split()))
if len(array)==4:
    L=array[0]
    H=array[1]
    P=array[2]
    Q=array[3]
    print(numpy.zeros((int(L),int(H),int(P),int(Q)),int))
    print(numpy.ones((int(L),int(H),int(P),int(Q)),int))
if len(array)==3:
    L=array[0]
    H=array[1]
    P=array[2]
    print(numpy.zeros((int(L),int(H),int(P)),int))
    print(numpy.ones((int(L),int(H),int(P)),int))
if len(array)==2:
    L=array[0]
    H=array[1]
    
    print(numpy.zeros((int(L),int(H)),int))
    print(numpy.ones((int(L),int(H)),int))
    
if len(array)==1:
    L=array[0]
    
    
    print(numpy.zeros((int(L)),int))
    print(numpy.ones((int(L)),int))





import numpy
numpy.set_printoptions(legacy='1.13')
N,M=input().split()
N=int(N)
M=int(M)
print(numpy.eye(N,M))










import numpy
N,M=input().split()
N=int(N)
M=int(M)
A=[]
B=[]
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))

A=numpy.array(A)
B=numpy.array(B)










import numpy
numpy.set_printoptions(legacy='1.13')
A=list(map(float,input().split()))
A=numpy.array(A)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))










import numpy

N,M=input().split()
N=int(N)
M=int(M)
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))
A=numpy.array(A)
somma=numpy.sum(A,axis=0)

print(numpy.prod(somma))











import numpy

N,M=input().split()
N=int(N)
M=int(M)
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))
A=numpy.array(A)
somma=numpy.sum(A,axis=0)

print(numpy.prod(somma))







import numpy

N,M=input().split()
N=int(N)
M=int(M)
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))
A=numpy.array(A)
minimo=numpy.min(A,axis=1)

print(numpy.max(minimo))













import numpy

N,M=input().split()
N=int(N)
M=int(M)
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))
A=numpy.array(A)


print(numpy.mean(A,axis=1))
print(numpy.var(A,axis=0))
print(round(numpy.std(A,axis=None),11))










import numpy

N=input()
N=int(N)
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))
A=numpy.array(A)
B=[]
for i in range(N):
    B.append(list(map(int,input().split())))
B=numpy.array(B)

print(numpy.dot(A,B))










import numpy


A=list(map(int,input().split()))
A=numpy.array(A)
B=list(map(int,input().split()))
B=numpy.array(B)

print(numpy.inner(A,B))
print(numpy.outer(A,B))















import numpy


A=list(map(float,input().split()))
A=numpy.array(A)
x=int(input())
print(numpy.polyval(A,x))











import numpy
N=input()
N=int(N)

A=[]
for i in range(N):
    A.append(list(map(float,input().split())))
A=numpy.array(A)



print(round(numpy.linalg.det(A),2))








regex_pattern = r"[,.]"

import re
print("\n".join(re.split(regex_pattern, input())))









import re

m = re.search(r'([a-zA-Z0-9])\1', input())
print(m.group(1) if m else -1)










import re
s=input()
m=re.findall(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])',s)
if m:
    print(*m,sep="\n")
else:
    print(-1)









import re

S = input()
k = input()

matches = re.finditer(r'(?=(' + re.escape(k) + r'))', S)

for m in matches:
    print((m.start(1), m.end(1) - 1))

if not re.search(re.escape(k), S):
    print((-1, -1))











import re
N=input()
S=''
for i in range(int(N)):
    S=S+input()+'\n'

S = re.sub(r"(?<=\s)&&(?=\s)", "and", S)

S=re.sub(r"(?<=\s)\|\|(?=\s)","or",S)

print(S)









regex_pattern = r"^M{0,3}(CM|CD|C{0,3}|DC{0,3})(XL|LX{0,3}|X{0,3}|XC)(IX|IV|VI{0,3}|XI{0,3}|I{0,3})$"	

import re
print(str(bool(re.match(regex_pattern, input()))))











regex_pattern = r"^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"    

import re
import email.utils
N=int(input())
for i in range(N):
    iniziale=input()
    mail=email.utils.parseaddr(iniziale)
    
    if re.match(regex_pattern, mail[1]):
        print(email.utils.formataddr(mail))
    






regex_pattern = r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\b"   

import re
inside_css = False
N=int(input())
S=[]
for i in range(N):
    S=input()
    
    if "{" in S:
        inside_css = True
        S = S.split("{", 1)[1]
        
    colors=re.findall(regex_pattern, S[1:])
    
    if colors:
      print(*colors,sep="\n")
    if "}" in S:
        inside_css = False
    










from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

parser = MyHTMLParser()

N = int(input())
html = ""

for _ in range(N):
    html += input() + "\n"

parser.feed(html)











from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()










from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

N = int(input())
html = ""

for _ in range(N):
    html += input() + "\n"

parser = MyHTMLParser()
parser.feed(html)
parser.close()










regex_pattern = r"^(?=(?:.*[A-Z]){2})(?=(?:.*[0-9]){3})(?=[A-Za-z0-9]{10}$).*$"

import re
N=int(input())
for i in range(N):
    codice=input()
    if re.match(regex_pattern, codice):
        
        if len(list(codice))==len(set(codice)):
            print("Valid")
        else:
            print("Invalid")
    else:
            print("Invalid")     










regex_pattern =r"^(?!.*(\d)(?:-?\1){3})(?:[4-6][0-9]{3}(?:-[0-9]{4}){3}|[4-6][0-9]{15})$"

import re
N=int(input())
for i in range(N):
    codice=input()
    if re.match(regex_pattern, codice):
      
            print("Valid")
        
    else:
            print("Invalid")        












regex_pattern = r"^[+-]?[0-9]*\.[0-9]+$"    

import re
N=int(input())
for i in range(N):
    if re.match(regex_pattern, input()):
        print("True")
    else:
        print("False")











#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)













regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

