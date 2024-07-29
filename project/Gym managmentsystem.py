class Member:
    def __init__(self, name, member_id, membership_type):
        self.name = name
        self.member_id = member_id
        self.membership_type = membership_type
        self.enrolled_classes = []


class Trainer:
    def __init__(self, name, trainer_id, specialty):
        self.name = name
        self.trainer_id = trainer_id
        self.specialty = specialty
        self.assigned_members = []

    def assign_member(self, member):
        self.assigned_members.append(member)


class GymClass:
    def __init__(self, class_name, schedule):
        self.class_name = class_name
        self.schedule = schedule
        self.enrolled_members = []

    def add_member(self, member):
            self.enrolled_members.append(member)
            print(f"Member added successfully to class {self.class_name}")


class Gym:
    def __init__(self):
        self.members = []
        self.trainers = []
        self.classes = []

    def add_member(self, member):
            self.members.append(member)
            print(f"Added member  successfully")
        

    def add_trainer(self, trainer):
            self.trainers.append(trainer)
            print(f"Added trainer  successfully")
       

    def schedule_class(self, gym_class):
            self.classes.append(gym_class)
            print(f"Scheduled class  successfully")

    def enroll_member_in_class(self, member, gym_class):
        if member in self.members and gym_class in self.classes:
            gym_class.add_member(member)
        else:
            if member not in self.members:
                print("Member not found in gym.")
            if gym_class not in self.classes:
                print("Class not found in gym.")

gym = Gym()

member1 = Member("Ali", 1, "membership_type1")
gym.add_member(member1)

trainer1 = Trainer("Hamza", "T001", "trainer specialty")
gym.add_trainer(trainer1)

gym_class1 = GymClass("abc", "10pm")
gym.schedule_class(gym_class1)

gym.enroll_member_in_class(member1, gym_class1)
