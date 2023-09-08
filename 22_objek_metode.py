class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.name})"
    
p1 = person("jhon", 36)
print(p1)
