#Problem 1
def prime_number(n):
    if n <= 1: #Bilangan kurang dari 2 maka bukan dari bilangan prima
        return False
    if n <= 3: #Jika bilangannya 2 dan 3 bilangan prima
        return True
    if n % 2 == 0 or n % 3 == 0: #Jika bilangan genap atau bilangannya habis dibagi 3, maka bilangan itu bukan bilangan prima 
        return False
    i = 5 #Mengecek faktor dari 5 hingga sqrt(n)
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    print(prime_number(1000000007)) # True
    print(prime_number(1500450271)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(10000000019)) # True
    print(prime_number(10000000033)) # True
