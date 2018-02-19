class NatureForce(object):

  def get_interaction_between_animals(self, animal, next_animal):
    if animal != None and next_animal != None:
      """ Old age interaction """
      if animal.max_age():
        return 'self_animal_death'


      """ Predation interaction """
      if animal.get_class_name() == 'Bear' and next_animal.get_class_name() == 'Fish':
        return 'next_animal_death'
      elif animal.get_class_name() == 'Fish' and next_animal.get_class_name() == 'Bear':
        return 'self_animal_death'
      elif self.__two_equals__('Fish', animal, next_animal):
        if self.__same_gender__(animal, next_animal):
          return 'do_nothing'
        else:
          return 'reproduce'
      elif self.__two_equals__('Bear', animal, next_animal):
        if self.__same_gender__(animal, next_animal):
          if self.__same_strength__(animal, next_animal):
            return 'do_nothing'
          elif self.__same_gender__(animal, next_animal) and animal.get_strength() > next_animal.get_strength():
            return 'next_animal_death'
          else:
            return 'self_animal_death'
        else:
          return 'reproduce'

    if next_animal == None:
      return 'move'

  def __two_equals__(self, class_name, animal, next_animal):
    return animal.get_class_name() == class_name and animal.get_class_name() == next_animal.get_class_name()

  def __same_gender__(self, animal, next_animal):
    return animal.get_gender() == next_animal.get_gender()

  def __same_strength__(self, animal, next_animal):
    return animal.get_strength() == next_animal.get_strength()
