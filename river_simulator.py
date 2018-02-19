from river import River

class RiverSimulator(object):

  def run(self):

    input_num = None
    trial_num = 1

    while (input_num != 3):
      print("keys: 1 (random river) 2 (file input) 3 (exit)")

      input_num = None

      trial_label = "Trial {0}: ".format(trial_num)
      input_num = input(trial_label)

      if input_num == "3":
        print("Adieu!")
        return False

      if input_num == "2":
        river_file_path = input("Input the path to your file: ")

        river = River(river_file_path)

        print("River from file")
        cycles_number = input("Enter the number of cycles: ")

        print("Initial river:")
        print(river)

        for i in range(0, int(cycles_number)):
          print("After cycle {0}".format(i + 1))
          river.update_river()
          print(river)

        trial_num += 1

      if input_num == "1":
        print("Random river")

        river_length = input("Enter river length: ")
        cycles_number = input("Enter the number of cycles: ")

        river = River(int(river_length))
        print("Initial river:")
        print(river)

        for i in range(0, int(cycles_number)):
          print("After cycle {0}".format(i + 1))
          river.update_river()
          print(river)

        trial_num += 1
