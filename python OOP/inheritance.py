## inheritance ###
class father:
    def land(self):
        print("havin 50 akrs land")

    def home(self):
        print("havin 5 home in thier own town")


class son(father):
    def money(self):
        print("havi 20 lac money")


obj = son()
obj.land()
obj.money()
obj.home()
