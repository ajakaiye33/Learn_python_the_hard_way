## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self, address):
        self.address = address
    def print_add(self):
        print("My address is:", self.address)
#
# ##? = is-a relationship
# class Dog(Animal):
#     def __init__(self,name):
#         ##? = has-a relationship
#         self.name = name
#
# ## ? is-a relationship
# class Cat(Animal):
#
#
#     def __init__(self,name):
#
#         ##? has-a relationship
#         self.name = name
#
#         ##Person has-a pet of some kind
#         self.pet = None
#
#
# ##? is-a relationship
#
# class Person(object):
#
#     def __init__(self,name):
#         ##?? has-a relationship
#         self.name = name
#
#         ## Person has-a pet of some kind
#         self.pet = None
#
#
# ##?? is-a relationship
#
# class Employee(Person):
#
#     def __init__(self, name, salary):
#         ## ?? hmm what is this strange magic? is-a relationship
#         super(Employee, self).__init__(name)
#         ## ?? has-a relationship
#         self.salary = salary
#
#
#
# ## ?? is-a class relationship
# class Fish(object):
#     pass
#
# ##?? = Salmon is-a Fish relationship
# class Salmon(Fish):
#     pass
# ## Halibt is-a fish relationship
# class Halibut(Fish):
#     pass
#
# ## rover is-a Dog
# rover = Dog('Rover')
#
# ## ?? = satan is-a cat
# satan = Cat("Satan")
#
# ##?? mary is-a Person
# mary = Person("Mary")
#
# ##? mary has-a pet named satan
# mary.pet = satan
#
# ##?? frank is-a(an) employee
# frank = Employee("Frank", 120000)
#
# ##??
# frank.pet = rover
#
# ##?? fliper is-a Fish
# flipper = Fish()
#
# ##?? crouse is-a Salmon
# crouse = Salmon()
#
# ##? harry is-a Halibut
# harry = Halibut()

##drills
show = Animal('Sub sahara forest')
show.print_add()
