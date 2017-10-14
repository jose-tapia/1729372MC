memo={}

def fibonacci(n):
    global memo
    if n==0 or n==1:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n]=fibonacci(n-2)+fibonacci(n-1)
        return memo[n]

print(fibonacci(10))
print(fibonacci(15))
