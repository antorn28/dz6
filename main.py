class A:
    def __init__(self, a_attr):
        self.a_attr = a_attr

    def method_A(self):
        print("Метод класса A")


class B:
    def __init__(self, b_attr):
        self.b_attr = b_attr

    def method_B(self):
        print("Метод класса B")


class ComplexClass(A, B):
    def __init__(self, a_attr, b_attr, c_attr):
        A.__init__(self, a_attr)
        B.__init__(self, b_attr)
        self.c_attr = c_attr

    def method_C(self):
        print("Метод класса ComplexClass")


obj = ComplexClass("Атрибут A", "Атрибут B", "Атрибут C")

print(obj.a_attr)
print(obj.b_attr)
obj.method_A()
obj.method_B()

print(obj.c_attr)
obj.method_C()