"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    number=2
    while len(list)<number_of_primes:
        n=2
        while n*n<number:
            if number%n!=0:
                n+=1
            else:
                break
        if n*n>number:
            list.append(number)
        number+=1       
    return list