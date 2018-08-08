# this program is supposed to be able to factor a polynomial
# x**2+4x-12 will be the first test, answer is (x-2)(x+6)
# also can't go higher than x**2 or do equations with coefficients for x**2

# take coefficients from user
coeX = int(input('What is the coefficient for power x?'))
coe1 = int(input('What is the coefficient for power 1?'))

# coe1 is the higher power, coe2 is the lower power
zero1 = 'x'
zero2 = 'y'

# finds the zeros of the equation
for i in range(-50, 50):
    if i**2 + coeX*i + coe1 == 0:
        zero1 = i
        break
for i in range(zero1+1, 50):
    if i**2 + coeX*i + coe1 == 0:
        zero2 = i
        break


def answer():
    # Prints answer based on zeros.
    if zero2 != 'y':
        print('(x + ' + str(-zero1) + ')(x + ' + str(-zero2) + ')')
    else:
        print('(x + '+ str(-zero1) + ') ** 2')


answer()
