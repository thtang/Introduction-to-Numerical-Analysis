import math
import decimal

nsides = 6
length = decimal.Decimal("1")

for i in range(20):
    length = (2. - (4. - length**2)**0.5)**0.5
    nsides *= 2		
    pi = length*nsides/2.

    print('-'*30)
    print('Polygon of',nsides,'slides:')
    print('pi(calc) = %.15f' % pi)
    print('diff = %.15f' % abs(math.pi-pi))
