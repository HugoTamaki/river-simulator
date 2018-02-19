from animal import Animal

class Bear(Animal):
  MAX_AGE = 10

  def __init__(self, age=None, gender=None, strength=None):
    self.__strength__ = strength
    super().__init__(age, gender)

  def get_strength(self):
    return self.__strength__

  def max_age(self):
    return self.MAX_AGE == self.__age__

  def incr_age(self):
    self.__strength__ += 1
    super().incr_age()
