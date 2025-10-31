def divide(n, i):
    if n % i == 0:
        return True
    else:
        return False

def is_prime(n):
    for i in range(2, n//2):
        divide(n, i)
    if is_prime == True:
        print("should be prime")
    else: 
        print("not prim?")


is_prime(67)