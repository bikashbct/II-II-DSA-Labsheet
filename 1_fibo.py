# QN1 nth Fibonacci number using tail recursion in python 
def tail_fibo(n , a = 0, b = 1):
    if n == 0:
        return a
    if n == 1:
        return b
    return tail_fibo(n-1, b, a+b)

if __name__=="__main__":

    try:
        user_input = int(input("Enter a non-negative integer (n) to find the nth Fibonacci number: ")) 

        n = int(user_input)
        
        if n < 0:
            print("Negative numbers are invalid. Using the absolute value instead.")
            n = abs(n) 
            print(f"The {n}th Fibonacci number is: {tail_fibo(n)}")
        else:
            print(f"The {n}th Fibonacci number is: {tail_fibo(n)}")
    except ValueError:
        print("Invalid input! Please enter a valid non-negative integer.")