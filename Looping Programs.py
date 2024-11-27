#program to print the numbers from 1 to 10
'''
i=1
while i<11:
    print(i)
    i+=1
'''
#typecasting
'''
r1=range(1,11)
print(list(r1))
'''
#for loop
'''
r1=range(1,11)
for n in r1:
    print(n,end='')
'''
#program to print the numbers from 10 to 1
'''
for n in range(10,0,-1):
    print(n,end='')
'''
#program to print the umbers from -10 to -1
'''
for n in range(-10,0):
    print(n,end='')
'''
#program to print numbers from -10 to 5
'''
for n in range(-10,6):
    print(n,end='')
'''
#program to print numbers from -20 to -15
'''
for n in range(-20,-14):
    print(n,end='')
'''
#program to print numbers from 20 to -15
'''
for n in range(20,-16,-1):
    print(n,end='')
'''
#program to get even numbers from user input
'''
a=int(input("Enter start-range:"))
b=int(input("Enter end-range:"))
i=1
for i in range(a,b):
    if i%2==0:
        print(i)
    i=i+1
'''
'''
start_v=int(input("Enter the start_num:"))
end_v=int(input("Enter the end_num:"))
for num in range(start_v,end_v):
    if num%2==0:
        print(num,end='')
'''
#program to get the word and index using for loop
'''
str1=input("Enter the words:").split()
for index_ in range(len(str1)):
    print(index_,str1[index_])
'''
#to pack in a tuple
'''
str1=input("Enter the words:").split()
t_=()
for index_ in range(len(str1)):
    t_+=((index_,str1[index_]),)
print(t_)
'''
#enumerate
'''
str1=input("Enter the words:").split()

print(tuple(enumerate(str1)))
print(list(enumerate(str1)))
print(enumerate(str1))

for t in enumerate(str1,1):
    print(t)
'''
#create a tuple with index and length of each words
'''
str_='hello guys see on the screen to see this program'
t_=()
for i,word in enumerate(str_.split()):
    t_+=((i,len(word)),)
print(t_)
'''
#create a set with index and word with even length only
'''
str_='sharing is caring always'
set_=set()
for i,word in enumerate(str_.split()):
    if len(word)%2==0:
        set_.add(word)
print(set_)
'''     

#program to check a number is prime or not
#condition---->number divisible by 1 and itself
'''
number=int(input("Enter a number:"))
for n in range(2,number):
    if number%2==0:
        print('It is not a prime number')
        break
else:
    print('It is a prime number')
 '''
#program to get prime number in a range
'''
s_v=int(input("Enter a number:"))
e_v=int(input("Enter a number:"))
for i in range(s_v,e_v+1):
    if i<=1:
        pass
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=' ')
'''    
#program to get factorial of a number
'''
number=int(input("Enter a number:"))
fact=1
for i in range(number,1,-1):
    fact=fact*i
print(f"Factorial of {number}:{fact}")
'''
#program to print fibanocci series
'''
number=int(input("Enter a number:"))
a=0
b=1
if number<=1:
    print(0)
else:
    print(a)
    print(b)
    for _ in range(2,number):
        c=a+b
        a=b
        b=c
        print(c)
''' 
#program to check armstrong number
#condition--->153->(1^3+5^3+3^3=153) #here 3 is length of given number
'''
n=int(input("Enter a number:"))
len_=len(str(n))
sum_=0
for digit in str(n):
    sum_+=int(digit)**3
if sum_==n:
    print(f'{n} is a armstrong number')
else:
    print(f'{n} is not an armstrong number')
'''
#write a program to find the sum of the first 10 natural numbers
'''
n=int(input("Enter a number:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print(sum)
'''
#write a program to print all even numbers between 1 and 20
'''
i=1
for i in range(1,21):
    if i%2==0:
        print(i,end=' ')
    i=i+1
'''
#program to reverse a give number
'''
n=input("Enter a number:")
print(''.join(list(reversed(n))))
'''
#write a program to find the sum of the digits of a given number
'''
n=int(input("Enter a number:"))
sum=0
while n>0:
    dig=n%10
    sum=sum+dig
    n=n//10
print(sum)
'''
#program to count the number of digits of a given number
'''
n=int(input("Enter a number:"))
count=0
while n>0:
    count=count+1
    n=n//10
print(count)
'''
#print all prime numbers between 1 and 100
'''
for i in range(1,100):
    if i<=1:
        pass
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=' ')
'''
#program to find sum of even digits in a given number
'''
n=int(input("Enter a number:"))
sum=0
while n>0:
    dig=n%10
    if dig%2==0:
        sum=sum+dig
    n=n//10
print(sum)
'''
#program to find sum of squares of the digits in a given number
'''
n=int(input("Enter a number:"))
sum=0
while n>0:
    dig=n**2
    sum=sum+dig
    n=n//10
print(sum)
'''
#zip function
#program to add the numbers in same indexes
'''
n=input("Enter numbers:").split()
m=input("Enter numbers:").split()
from itertools import zip_longest
for i,j in zip_longest(n,m,fillvalue=10):
    print(f'{int(i)}+{int(j)}={int(i)+int(j)}')
'''
#program to square the numbers in 1st and cube the numbers 2nd tuple and print in tuple
'''
n=input("Enter numbers:").split()
m=input("Enter numbers:").split()
from itertools import zip_longest
for i,j in zip_longest(tuple(n),tuple(m),fillvalue=10):
    print(f'square{int(i)}={int(i)**2} and cube {int(j)}={int(j)**3}')
    print((int(i)**2,int(j)**3))
'''
#function
#program to get the length of any iterable with method
'''
def length_(iterable):
    print(len(iterable))


length_([5,6,7,7])
length_((4.5,6.7))
length_('hai')
'''
#program to get the length of any iterable without method
'''
def length_(iterable):
    count_=0
    for _ in iterable:
        count_+=1
    print(count_)


length_([5,6,7,7])
length_((4.5,6.7))
length_('hai')
'''
#variablescope
# global variable
'''
a=10
def f1():
    print(a,"inside the function")


f1()
print(a,"outside the function")
'''
#local variable
'''
a=10
def f1():
    a=20
    print(a,"inside the function")


f1()
print(a,"outside the function")
'''
#convert local to global by using global keyword
'''
a=10
def f1():
    global a
    a=20
    print(a,"inside the function")


f1()
print(a,"outside the function")
'''
#return function
'''
def f1():
    n=10
    return n


print(f1())
z=f1()
print(z)
'''
'''
a=10
def f1():
    a=10
    return a
a1=f1()
print(a)
'''
'''
def operation(a,b):
    return a+b,a*b


op=operation(10,20)
print(op)
'''
#non local variable
'''
def f1():
    num=100
    def f2():
        num=100
        print(num)
    f2()
    print(num)
f1()
'''
'''
def f1():
    num=100
    def f2():
        nonlocal num
        num=200
        print(num,"Inside nested function")
    f2()
    print(num,"Outside nested function")
f1()
'''
#arguments
'''
def f1(name,age,id):
    return f"name:{name}\nage:,id
print("pushkar",24,2)
'''
#keyword argument
'''
def f1(name,age,id):
    return f"name:{name}\nage:{age}\nregister_no:{id}\n"
print(f1(name='rani',age=34,id=4))
'''
#combination of positional andkeyword argument
'''
def f1(name,age,id):
    return f"name:{name}\nage:{age}\nregister_no:{id}\n"
print(f1('rani',34,4))
print(f1(name='rani',age=34,id=4))
'''
#only positional and keyword argument
'''
#only positional argument
def f1(a,b,/,c,d):
    print(a,b,c,d)
f1(10,20,45,45)
'''
#only keyword arguments
'''
def f1(a,b,*,c,d):
    print(a,b,c,d)
f1(a=10,b=34,c=45,d=45)
f1(10,34,c=45,d=45)
f1(10,b=34,c=45,d=45)
'''
#variable positional arguments
'''
def func(*args):
    print(args)
func(3,4,5)
func('hai',[4,5,6],True)
'''
#variable keyword arguments
'''
def func(**kwargs):
    print(kwargs)
func(a=34,b=3.6,c=False,d='python',e=[False,True])
'''
'''
def func(string_,list_,*args,**kwargs):
    print("\n",string_,"\n",list_,"\n",args,"\n",kwargs)
func(3.4,4,5,6,c=False,d='python',e=[False,True])
'''
#default argument
'''
def func(a=2,b=10):
    return a**2,b**3
print(func(3,5))
print(func(4))
print(func())
'''
#programs
#A function takes variable no.of positional arguments as input.
#How to check if the arguments that are passes more than 5
#without user input
'''
def f1(*a):
    if len(a)>5:
        return True
    else:
        return False
print(f1(3,4,5,6))
print(f1(45,23,4.5,56,2.4,78))
'''
'''
def f1(a=input("Enter a number:")):
    if len(a.split())>5:
        return True
    else:
        return False
print(f1())
'''
