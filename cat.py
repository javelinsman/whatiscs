import random
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Board:
    def __init__(self, h, w):
        self.m = []
        self.h = h
        self.w = w
        for i in range(h):
            self.m.append([0] * w)
        self.cat_info = []

    def print_map(self):
        clear()
        print("  +" + "-" * len(self.m[0]) + "+")
        for i in range(len(self.m)):
            s = "  |"
            for j in range(len(self.m[i])):
                if self.m[i][j] == 0:
                    s += " "
                else:
                    s += "*"
            s += "|"
            print(s)
        print("  +" + "-" * len(self.m[0]) + "+")

    def clear_map(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                self.m[i][j] = 0

    def draw_cat(self):
        self.clear_map()
        det = False
        for (i, j, di, dj) in self.cat_info:
            if 0 <= i and i < len(self.m) and 0 <= j and j < len(self.m[0]):
                det = True
                self.m[i][j] = 1
        return det

    def proceed_cat(self):
        for i in range(len(self.cat_info)):
            self.cat_info[i][0] += self.cat_info[i][2]
            self.cat_info[i][1] += self.cat_info[i][3]

    def add_cat(self, x, y):
        self.cat_info.append([self.h//2-y, self.w//2+x])
        return len(self.cat_info) - 1

    def move_cat(self, n, dx, dy):
        if 0 <= n and n < len(self.cat_info) and len(self.cat_info[n]) == 2:
            self.cat_info[n] += [-dy, dx]

    def simulate(self):
        while True:
            det = self.draw_cat()
            self.print_map()
            self.proceed_cat()
            time.sleep(0.3)
            if not det:
                break
        print("\n\n\nAll cats are gone!\n\n\n")

b = Board(50, 100)

add_cat = b.add_cat
move_cat = b.move_cat
simulate = b.simulate
