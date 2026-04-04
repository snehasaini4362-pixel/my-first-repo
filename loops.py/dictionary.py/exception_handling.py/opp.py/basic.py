# A method that changes a property value:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

# Create multiple methods in a class:

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()


# Why Use Encapsulation?
# Encapsulation provides several benefits:

# Data Protection: Prevents accidental modification of data
# Validation: You can validate data before setting it
# Flexibility: Internal implementation can change without affecting external code
# Control: You have full control over how data is accessed and modified
# Example
# Use encapsulation to protect and validate data:

class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())

# Private Methods
# You can also make methods private using the double underscore prefix:

# Example
# Create a private method:

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error






# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

# Example
# Different classes with the same method:

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()




# Inheritance Class Polymorphism
# What about classes with child classes with the same name? Can we use polymorphism there?

# Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

# Example
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

