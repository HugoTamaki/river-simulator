from animal import Animal

class Fish(Animal):
  MAX_AGE = 5

  def __init__(self, age=None, gender=None):
    super().__init__(age, gender)

  def max_age(self):
    return self.MAX_AGE == self.__age__