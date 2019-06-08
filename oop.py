class Animal(object):
   def __init__(self, name, legs=4):
       self.name = name
       self.sound = self.get_sound()
       self.food = self.get_food()
       self.legs = legs

   def show(self):
       print "name: {0}, sound:{1}, food:{2}, legs:{3}".format(self.name,
                                                               self.sound,
                                                               self.food,
                                                               self.legs)

   def get_sound(self):
       return None

   def get_food(self):
       return None

animal = Animal("some animal")
animal.show()

class Dog(Animal):
   def __init__(self):
       super(Dog, self).__init__("Dog")

   def get_sound(self):
       return 'bark'

   def get_food(self):
       return 'pedigree'


dog = Dog()
dog.show()
