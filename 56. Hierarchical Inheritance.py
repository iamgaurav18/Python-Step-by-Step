class A:                                              #              A
    pass                                              #           |     |
class B(A):                                           #           B     C
    pass                                              #         |   | |   |
class C(A):                                           #         D   E F   G
    pass

a=C()

# This is how a Hierarchucal Inheritance looks like.
# Combination of more than one type of inheritance can be considered as Hybrid inheritance