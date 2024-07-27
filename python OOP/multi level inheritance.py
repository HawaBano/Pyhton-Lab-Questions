# multi level inheritance  ================================
class father:
    sur_name = "singh"


class son(father):
    def show(self):
        print("ankit", self.sur_name)


class G_son(son):
    def disp(self):
        print("ankush", self.sur_name)


s = son()
s.show()

g = G_son()
g.disp()
