#hybrid inheritance
#combaining multilevel and hierachical inheritance
class A:
    def method_a(self):
        print("method from class A")

class B:
    def method_b(self):
        print("method from class B")

class C:
    def method_c(self):
        print("method from class C")

class D(A,B,C):
    def method_d(self):
        print("method from class d")

d = D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()