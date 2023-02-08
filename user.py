class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        """ func that prints out all of User's attributes """
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_reward_member)
        print(self.gold_card_points)

    def enroll(self):
        """ enroll a user if they are not already enrolled """
        if self.is_reward_member:
            print(f"{self.first_name} is already a member")
            return False
        self.is_reward_member = True
        self.gold_card_points = 200
        return True

    def spend_points(self, amount):
        """ spend a user's points if they have enough points to spend """
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print(f"{self.first_name} does not have enough points.")

# create user 1
john_doe = User("John", "Doe", "jdoe@email.com", 25)

# display info of user 1
john_doe.display_info()

# enroll user 1 and display info
john_doe.enroll()
john_doe.display_info()

# create user 2 and 3
jack_smith = User("Jack", "Smith" , "jsmith@email.com", 40)
jane_williams = User("Jane", "Williams" , "jwilliams@email.com", 30)

# have user 1 spend 50 points
john_doe.spend_points(50)

# user 2 enrolls and spents 80 points
jack_smith.enroll()
jack_smith.spend_points(80)

# display info of user 1, 2, and 3
john_doe.display_info()
jack_smith.display_info()
jane_williams.display_info()

# check if a user can re-enroll or spend over their limit
jack_smith.enroll()
jane_williams.spend_points(40)
