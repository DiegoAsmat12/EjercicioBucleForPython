#Ejercicio 1 
for i in range(150):
    print(i)

#Ejercicio 2
for i in range(5,1000,5):
    print(i)

#Ejercicio 3
for i in range(100):
    dojo = ""
    if i%5==0: 
        dojo+="Coding"
        if i%2==0: 
            dojo+=" Dojo"
        print(dojo)
    else:
        print(i)

#Ejercicio 4
suma = 0
for i in range(500000):
    if(i%2==1): 
        suma+=i
print(suma)

#Ejercicio 5
for i in range(2018,0,-4):
    print(i)

#Ejercicio 6
lowNum=2
highNum=9
mult=3
for i in range(lowNum,highNum+1):
    if(i%mult==0):
        print(i)