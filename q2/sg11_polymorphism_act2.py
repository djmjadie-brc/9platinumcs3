"""
a. What is duck typing, as explained in the video?

- Duck typing is another way to achieve polymorphism other than inheritance where objects must have the minimum attributes/methods. And an analogy is shown in a video that "If it looks like a duck and quacks like a duck, then it must be a duck."

b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

- The car class needs to have the same method as the Dog and Cat class as objects must have the minimum attributes/methods for duck typing to work.

3.) How does the code in 2.2 demonstrate polymorphism?

- The code demonstrates polymorphism by having many forms when the same method is called for each object, with each vehicle having a different output when start_trip() is called.
""" 
# created a class called "Car"
class Car():
  def move(self):  # prints where and how the car moves
    print("The car drives on the road.")

# created another class called "Boat" with the same method as the car
class Boat():
  def move(self): # also prints where and how the boat moves
    print("The boat sails on water.")

# created a new class called "Drone" with also the same method as the car and boat
class Drone():
  def move(self): # prints again where and how the drone moves
    print("The drone flies in the sky.")

def start_trip(vehicle):  # a function that calls the move method
  vehicle.move()

# created objects for each class
car = Car()
boat = Boat()
drone = Drone()

# calls the start_trip method for each object
start_trip(car)
start_trip(boat)
start_trip(drone)
