from functools import reduce
import random
from fish import Fish
from bear import Bear
from nature_force import NatureForce

class River(object):
  LEFT = 0
  RIGHT = 1

  def __init__(self, arg, seed=None):
    self.__river__ = []

    if arg.__class__.__name__ == 'int':
      self.__generate_random_river__(arg)
    else:
      self.__generate_river_from_file__(arg)

  def get_length(self):
    return len(self.__river__)

  def set_seed(self, seed):
    pass

  def num_empty(self):
    return len(list(filter(lambda x: x == None, self.__river__)))

  def get_null_positions(self, river):
    nulls = []

    for index, val in enumerate(river):
      if val == None:
        nulls.append(index)

    return nulls

  def add_random(self, animal):
    if self.num_empty() == 0:
      return False
    else:
      null_positions = self.get_null_positions(self.__river__)
      random_gender = random.randint(1, 2)
      class_name = animal.get_class_name()

      new_animal = self.__create_random_animal__(random_gender, animal)

      random_position = random.choice(null_positions)

      self.__river__[random_position] = new_animal

      return new_animal

  def update_cell(self, i):
    animal = self.__river__[i]

    if animal and not animal.moved():
      if animal.max_age():
        self.__river__[i] = None
        return False
      else:
        random_direction = random.randint(0, 1)
        if random_direction == self.RIGHT:
          next_animal = self.__get_animal_to_right__(i)
          next_position = self.__get_right_position__(i)
        else:
          next_animal = self.__get_animal_to_left__(i)
          next_position = self.__get_left_position__(i)

      status = self.__check_interaction__(animal, next_animal)

      if status == 'do_nothing':
        animal.set_as_moved()
        return True

      if status == 'next_animal_death':
        self.__river__[next_position] = animal
        self.__river__[i] = None
        animal.set_as_moved()
        return True

      if status == 'self_animal_death':
        self.__river__[i] = next_animal
        self.__river__[next_position] = None
        return True

      if status == 'reproduce':
        new_animal = self.add_random(animal)
        if new_animal:
          new_animal.set_as_moved()
        return True

      if status == 'move':
        self.__river__[next_position] = animal
        animal.set_as_moved()
        self.__river__[i] = None
        return True

  def update_river(self):
    for i in range(0, len(self.__river__)):
      animal = self.__river__[i]
      if animal:
        animal.incr_age()

    for i in range(0, len(self.__river__)):
      self.update_cell(i)

    for i in range(0, len(self.__river__)):
      animal = self.__river__[i]
      if animal:
        animal.set_as_unmoved()

  def __generate_random_river__(self, qty):
    for i in range(0, qty):
      random_num = random.randint(0, 2)

      if random_num == 0:
        self.__river__.append(None)
      elif random_num == 1:
        self.__river__.append(Fish(0, random.randint(1, 2)))
      elif random_num == 2:
        self.__river__.append(Bear(0, random.randint(1, 2), 0))

  def __generate_river_from_file__(self, path):
    try:
      river_file = open(path, 'r')
      river_string = river_file.read()
      river_splited = river_string.split()

      def prepare_values(item):
        if item == '---':
          return None
        elif item[0] == 'B':
          gender = 1 if item[1] == 'F' else 2
          age = int(item[2])
          return Bear(age, gender, 0)
        elif item[0] == 'F':
          gender = 1 if item[1] == 'F' else 2
          age = int(item[2])
          return Fish(age, gender)

      self.__river__ = list(map(prepare_values, river_splited))

    except FileNotFoundError as e:
      print("File not found")

  def __create_random_animal__(self, gender, animal):
    class_name = animal.get_class_name()

    if class_name == 'Bear':
      new_animal = eval(class_name)(0, gender, 0)
    else:
      new_animal = eval(class_name)(0, gender)

    return new_animal

  def __get_animal_to_right__(self, i):
    right_position = self.__get_right_position__(i)
    return self.__river__[right_position]

  def __get_animal_to_left__(self, i):
    left_position = self.__get_left_position__(i)
    return self.__river__[left_position]

  def __get_right_position__(self, i):
    if i == (len(self.__river__) - 1):
      return 0
    else:
      return i + 1

  def __get_left_position__(self, i):
    if i == 0:
      return len(self.__river__) - 1
    else:
      return i - 1

  def __check_interaction__(self, animal, next_animal):
    nature_force = NatureForce()
    return nature_force.get_interaction_between_animals(animal, next_animal)

  def __repr__(self):
    def print_item(sum, item):
      if item == None:
        return sum + " --- "
      else:
        return sum + " {0} ".format(str(item))

    return reduce(print_item, self.__river__, "")
