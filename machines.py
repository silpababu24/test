



  # Program to Check Prime Numberg


num=13
if num ==1:
    print(num,"is not a prime number")
elif num > 1:
    for i in range(2,num):
        if (num % i) ==0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number" )   

#Python program finds the factorial of a number using a loop.

num=8
factorial=1
if num<0:
    print("factorial doesn't exist for negative numbers")        
elif num ==0:
    print("factorial of 0 is ")
else:
    for x in range(1,num + 1):
        factorial=factorial*i
    print("factorial of", num, "is",factorial)                 

#Check if a String is a Palindrome or not.
x="silpa"
y="n"
for i in x:
    y=i+y
if(x==y):    
    print("yes") 
else:
    print("no")           

#Python Program to Display the multiplication Table of 6

num=6
for i in range(1,7):
    print(num,'*',i,'=',num*i)

#The program takes a string and counts the number of vowels in a string.
n="count number"
count=0
vowels=["a","e","i","o","u","A","E"]
for i in range(len(n)):
    if n[i] in vowels:
         count+= 1
print("number of vowels in the given string is:",count)        
