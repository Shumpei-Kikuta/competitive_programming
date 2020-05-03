import sys
sys.setrecursionlimit(10000000)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    
    return sorted(divisors)


def main():
    X = int(input())
    divisors = make_divisors(X)
    root_X = int(X ** 0.5)
    for d in divisors:
        lim = int(X ** 0.25)
        for b in range(-lim, lim+1):
            a = b + d
            if a ** 4 + (a**3) * b + (a ** 2) * (b** 2) + (a) * (b ** 3) + b ** 4 == X // d:
                print(a, b)
                sys.exit()
        

if __name__ == '__main__':
    main()
