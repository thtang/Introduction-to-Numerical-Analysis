import math

pi = 0.
numerator = 1.

for n in range(1001):
    pi += numerator/(2.*n+1.)*4.
    numerator = -numerator
                
    if n%100 == 0:
        print('-'*30)
        print('Sum up to',n,'step:')
        print('pi(calc) = %.15f' % pi)
        print('diff = %.15f' % abs(math.pi-pi))
