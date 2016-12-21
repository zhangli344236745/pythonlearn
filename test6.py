class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

class E(C,B):
    pass

print(D.__mro__)
print(E.__mro__)