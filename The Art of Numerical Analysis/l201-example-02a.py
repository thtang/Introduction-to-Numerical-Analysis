import math

pi = 0.
numerator = 1./3.**0.5

for n in range(31):
    pi += numerator/(2.*n+1.)*6.
    numerator *= -1./3.
                
    print('-'*30)
    print('Sum up to',n,'step:')
    print('pi(calc) = %.15f' % pi)
    print('diff = %.15f' % abs(math.pi-pi))
