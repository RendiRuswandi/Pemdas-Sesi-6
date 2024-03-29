#Latihan Looping, While, Nested if & Fibonaci

# 1)
print ("No 1")
for i in range(1,6):
    for j in range(1,6):
        print(i*j, end=" ")
    print()
    
# 2)  
print ("No 2")
for i in range(1,6):
    for j in range(i,i+i):
        print(j, end=" ")
    print( )
    
# 3)
print ("No 3")
for i in range(1,6):
    for j in range(i,6):
        print(j, end=" ")
    print( )
    
# 4)
print ("No 4")
for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
        i += 2
    print( )
    
# 6)   
print ("No 6")
baris = 5
kolom = 5
for i in range (baris, 0, -1):
    for j in range (1, kolom, +1):
        if j < i :
            print ("+", end =" ")
        else :
            print(j, end =" ")
    print ( )
    
# 7)
print ("No 7")    
baris = 4
kolom = 5
char = ["A","B"]
for i in range (baris):
    for j in range (kolom):
        print(char[(i + j) % 2], end=" ")
    print ( )
    
# 8)
print ("No 8")    
row = 5 
char = ["S","O"]
for i in range (row):
    for j in range (row - i):
        print (char[(i + j)% 2], end=" ")
    print ( )
    
# 9)
print ("No 9")
a = 1
b = 1
c = 0
for i in range (10):
    print("*"*a)
    c = a + b
    a = b
    b = c