class Doit:
    def __call__(self):
        print("CALLING")

    def yell(self):
        print("YELLING")

d = Doit()

#  d.some_method()
d()  # d.__call__(...)
d.yell()
# d.__call__()