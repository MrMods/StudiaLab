import math
import keyword

def nazwyfuncjimodulow():

    funkcje_math= [func for func in dir(math)]
    funkcje_tuple= [func for func in dir(tuple)]
    funkcje_keyword= [func for func in dir(keyword)]

    print("Nazwy funkcji zawarte w module Math: ")
    for f in funkcje_math:
        print(f)
    print("Nazwy funkcji zawarte w module Tuple: ")
    for f in funkcje_tuple:
        print(f)
    print("Nazwy funkcji zawarte w module Keyword: ")
    for f in funkcje_keyword:
        print(f)

nazwyfuncjimodulow()


'''
Nazwy funkcji zawarte w module Math: 
__doc__
__loader__
__name__
__package__
__spec__
acos
acosh
asin
asinh
atan
atan2
atanh
cbrt
ceil
comb
copysign
cos
cosh
degrees
dist
e
erf
erfc
exp
exp2
expm1
fabs
factorial
floor
fma
fmod
frexp
fsum
gamma
gcd
hypot
inf
isclose
isfinite
isinf
isnan
isqrt
lcm
ldexp
lgamma
log
log10
log1p
log2
modf
nan
nextafter
perm
pi
pow
prod
radians
remainder
sin
sinh
sqrt
sumprod
tan
tanh
tau
trunc
ulp
Nazwy funkcji zawarte w module Tuple: 
__add__
__class__
__class_getitem__
__contains__
__delattr__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__getnewargs__
__getstate__
__gt__
__hash__
__init__
__init_subclass__
__iter__
__le__
__len__
__lt__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__rmul__
__setattr__
__sizeof__
__str__
__subclasshook__
count
index
Nazwy funkcji zawarte w module Keyword: 
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
iskeyword
issoftkeyword
kwlist
softkwlist
'''