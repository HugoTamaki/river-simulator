import random

class Gender(object):
  FEMALE = 1
  MALE = 2

class Animal(object):
  def __init__(self, age=None, gender=None):
    if gender is None:
      self.__gender__ = random.randint(1, 2)
    else:
      self.__gender__ = gender
    self.__age__ = age
    self.__moved__ = False

  def get_age(self):
    return self.__age__

  def get_gender(self):
    return "M" if self.__gender__ == Gender.MALE else "F"

  def max_age(self):
    pass

  def incr_age(self):
    self.__age__ += 1

  def set_as_moved(self):
    self.__moved__ = True

  def set_as_unmoved(self):
    self.__moved__ = False

  def moved(self):
    return self.__moved__

  def get_class_char(self):
    return self.get_class_name()[0]

  def get_class_name(self):
    return self.__class__.__name__

  def __repr__(self):
    return "{0}{1}{2}".format(self.get_class_char(), self.get_gender(), self.get_age())
