class Dog:
  
    def describe_dog(self):
        print(f"Arm length: {self.arm_length} meters")
        print(f"Leg_length: {self.leg_length} meters")
        print(f"Number_eyes: {self.number_eyes} meters")
        print(f"has_tail: {'yes' if self.has_tail else 'no'}")
        print(f"is_furry: {'yes' if self.is_furry else 'no'}")

    def __init__(self, arm_length, leg_length, number_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.number_eyes = number_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

my_favorite_animal = Dog(0.5, 0.9, 2, True, True)
            

my_favorite_animal.describe_dog()