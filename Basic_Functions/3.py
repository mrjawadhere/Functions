# Write a function to find the factorial of a number using recursion
def fac(n):
    if n<0:
        print("Enter Number is must be non-negative and grater than 0")
    elif n==1 or n==0 :
        return 1
    return n*fac(n-1)
num=int(input("Enter the number that you want to get find factorial:"))

print("The factorail of your number",num,"is =", fac(num))




        