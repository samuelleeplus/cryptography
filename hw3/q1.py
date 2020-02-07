import itertools
from functools import reduce

# constants used in the multGF2 function
mask1 = mask2 = polyred = None


def setGF2(degree, irPoly):
    """Define parameters of binary finite field GF(2^m)/g(x)
       - degree: extension degree of binary field
       - irPoly: coefficients of irreducible polynomial g(x)
    """

    def i2P(sInt):
        """Convert an integer into a polynomial"""
        return [(sInt >> i) & 1
                for i in reversed(range(sInt.bit_length()))]

    global mask1, mask2, polyred
    mask1 = mask2 = 1 << degree
    mask2 -= 1
    polyred = reduce(lambda x, y: (x << 1) + y, i2P(irPoly)[1:])


def multGF2(p1, p2):
    """Multiply two polynomials in GF(2^m)/g(x)"""
    p = 0
    while p2:
        if p2 & 1:
            p ^= p1
        p1 <<= 1
        if p1 & mask1:
            p1 ^= polyred
        p2 >>= 1
    return p & mask2

  
 # Define binary field GF(2^8)/x^8+x^4+x^3+x+1. 
setGF2(8, 0b100011011)


#multiply the two different irreducible polynomial 
ses = multGF2(0b011011101, 0b010101110)
value = format(ses, "b")
print(value)

value = list(value)
print(value)
#(x7+ x6+ x4+x3+x2+1)  (x7+x5+ x3+ x2+x) 


#########################################
#part b


!pip install BitVector
from BitVector import *

def gf_divide(num, mod, n):

    if mod.length() > n+1:
        raise ValueError("Modulus bit pattern too long")
    quotient = BitVector( intVal = 0, size = num.length() )
    remainder = num.deep_copy()
    i = 0
    while 1:
        i = i+1
        if (i==num.length()): 
            break
        mod_highest_power = mod.length() - mod.next_set_bit(0) - 1
        if remainder.next_set_bit(0) == -1:
            remainder_highest_power = 0
        else:
            remainder_highest_power = remainder.length() - remainder.next_set_bit(0) - 1
        if (remainder_highest_power < mod_highest_power) or int(remainder)==0:
            break
        else:
            exponent_shift = remainder_highest_power - mod_highest_power
            quotient[quotient.length() - exponent_shift - 1] = 1
            quotient_mod_product = mod.deep_copy();
            quotient_mod_product.pad_from_left(remainder.length() - mod.length() )
            quotient_mod_product.shift_left(exponent_shift)
            remainder = remainder ^ quotient_mod_product
    if remainder.length() > n:
        remainder = remainder[remainder.length()-n:]
    return quotient, remainder

def gf_multiply(a, b):
    
    a_highest_power = a.length() - a.next_set_bit(0) - 1
    b_highest_power = b.length() - b.next_set_bit(0) - 1
    result = BitVector( size = a.length()+b.length() )
    a.pad_from_left( result.length() - a.length() )
    b.pad_from_left( result.length() - b.length() )
    for i,bit in enumerate(b):
        if bit == 1:
            power = b.length() - i - 1
            a_copy = a.deep_copy()
            a_copy.shift_left( power )
            result ^= a_copy
    return result



def gf_MI(num, mod, n):
    #’’’
    #Using the arithmetic of the Galois Field GF(2^n), this function returns the
    #multiplicative inverse of the bit pattern ’num’ when the modulus polynomial
    #is represented by the bit pattern ’mod’.
    #’’’
    NUM = num.deep_copy(); MOD = mod.deep_copy()
    x = BitVector( size=mod.length() )
    x_old = BitVector( intVal=1, size=mod.length() )
    y = BitVector( intVal=1, size=mod.length() )
    y_old = BitVector( size=mod.length() )
    while int(mod):
        quotient, remainder = gf_divide(num, mod, n)
        num, mod = mod, remainder
        x, x_old = x_old ^ gf_multiply(quotient, x), x
        y, y_old = y_old ^ gf_multiply(quotient, y), y
    if int(num) != 1:
        return "NO MI. However, the GCD of ", str(NUM), " and ", str(MOD), " is ", str(num)
    else:
        quotient, remainder = gf_divide(x_old ^ MOD, MOD, n)
        return remainder

###########################################

mod = BitVector(bitstring ='100011011')
a = BitVector( bitstring ='011011101' )
b= BitVector(bitstring= '010101110')
result = gf_MI( a, mod, 8 )
print("\nMI of %s is: %s" % (str(a), str(result)))
print("The inverse of x7+ x6+ x4+x3+x2+1 in GF(28) is x7+ x6+x5+x4+x3")

########################################

