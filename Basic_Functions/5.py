# Create a function to check if a given number is prime.
def prime(n):
    if n<=1:
        print("Enter a valid number")
    else:
        for num in range(2,int(n**0.5)+1):
            if n%num==0:
                return " number is not a prime.."
        return " number is a prime.."
        
a=int(input("Check the prime number"))
func=prime(a)
print(func)
            
