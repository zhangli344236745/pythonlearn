__author__ = '0138695'
class Foo:
    def __init__(self):
        self.name = "wopeiqi"

    def func(self):
        return "func"

obj = Foo()
print hasattr(obj,"name")
print hasattr(obj,"func")

print getattr(obj,"name")
print getattr(obj,"func")

setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)

print getattr(obj,"age")
print getattr(obj, 'show')