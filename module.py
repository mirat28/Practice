class Parent():
    def myself(self):
        print("I am a mom")

class Child(Parent):
    def play(self):
        print("Hello, world")

    def myself(self):
        print("I am a baby")


parent = Parent()
parent.myself()
child = Child()
child.myself()
