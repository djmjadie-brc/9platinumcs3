# created the parent class
class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print(self.name, "makes a sound")

  def eat(self):
    print(self.name, "eats food")

# created a child class "Lion"
class Lion(Animal):
  def make_sound(self):  # overrides the inherited method make_sound()
    print(self.name, "roars loudly")

  def eat(self):  # overrides the inherited method eat()
    print(self.name, "eats fresh meat")

# created a child class "Elephant"
class Elephant(Animal):
  def make_sound(self):  # overrides the inherited method make_sound()
    print(self.name, "trumpets")

  def eat(self):  # overrides the inherited method eat()
    print(self.name, "eats grass and fruits")

# created a child class "Monkey"
class Monkey(Animal):
  def make_sound(self):  # overrides the inherited method make_sound()
    print(self.name, "chatters")

  def eat(self):  # overrides the inherited method eat()
    print(self.name, "eats bananas")

# created objects for each child class
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

# output of the code
(lion.make_sound())
(lion.eat())
print("-----")

(elephant.make_sound())
(elephant.eat())
print("-----")

(monkey.make_sound())
(monkey.eat())
print("-----")
    
    
  
    
