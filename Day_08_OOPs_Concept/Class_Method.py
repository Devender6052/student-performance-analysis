# A class method is bound to the class & receives the class as an implicit first Argument.
# Note- static method can't access or modidfy class state & generally for uitility

class person:
    name="Unknown"

    @classmethod
    def Change_name(cls, name):
        cls.name=name

p1=person()
p1.Change_name("Rahul kumar")
print(p1.name)
print(person.name)