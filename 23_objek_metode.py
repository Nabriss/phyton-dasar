class person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("haloo my name is" + self.name)

p1 = person("jhon", 36)
p1.myfunc()