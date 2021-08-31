#python script for checking whether a given number is perfect number or not.
n=int(input("enter a number:"))
temp=n
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==temp:
    print("perfect number")
else:
    print("not perfect number")
