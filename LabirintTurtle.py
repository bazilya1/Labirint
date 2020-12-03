class LabirintTurtle:
    def __init__(self):
        self.f = 0
        self.map = [[0], [0]]
        self.line = 0
        self.lines = 0
        self.col = 0
        self.cols = 0
        self.tur = 'A'
        self.map2 = [0]
        self.val = True


    def load_map(self, name):
        self.f = open(name, 'r')
        self.map = [line.replace('\n', '').split(' ') for line in self.f]
        self.map2 = self.map
        self.lines = len(self.map)
        self.cols = len(self.map[0])
        self.line = int((self.map[-2][0]))
        self.col = int((self.map[-1][0]))
        self.map.pop(-1)
        self.map.pop(-1)

    def show_map(self, turtle=None):
        if turtle==None:
            for i in self.map:
                print(*i)
        elif turtle==True:
            self.map2[self.line][self.col] = self.tur
            self.map2[self.line].pop(self.col + 1)
            for i in self.map2:
                print(*i)


#    def check_map(self):


#    def exit_count_step(self):

#    def exit_show_step(self):

Lab = LabirintTurtle()
Lab.load_map("lab.txt")
Lab.show_map(turtle=True)
