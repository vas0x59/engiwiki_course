from typing import Tuple, List, Dict
import random


def ch_xy_wh(x, y, w, h):
    return (x >= 0) and (y >= 0) and (x < w) and (y < h)


# MAP_ = ' '

class Ship:
    def __init__(self, type: int, begin: Tuple[int], end: Tuple[int]):
        self.type = type
        self.begin = begin
        self.end = end
        self.health = type

CELL_TYPE_EMPTY = ' '
CELL_TYPE_SHIP = '#'
CELL_TYPE_TRY = '*'

class Cell:
    def __init__(self, type, ship_type = 0, health = 1, ship_id = 0):
        self.health = health
        self.type = type
        self.ship_type = ship_type
        self.ship_id = ship_id
    def __str__(self):
        if self.type == CELL_TYPE_SHIP and self.health > 0:
            return "\u2589"
        elif self.type == CELL_TYPE_SHIP and self.health == 0:
            return "\u2592"
        elif self.type == CELL_TYPE_TRY:
            return "\u2591"
        elif self.type == CELL_TYPE_EMPTY:
            return " "

MAP_EMPTY = Cell(CELL_TYPE_EMPTY)
MAP_SHIP = Cell(CELL_TYPE_SHIP)


# class Fight_res:
#     def __init__(self, ):
        

class Map:
    def __init__(self, w: int, h:int, id_s: str):
        self.w = w
        self.h = h
        self.map = [[MAP_EMPTY for i in range(w)] for j in range(h)]
        self.ships = []
        self.id_s = id_s
    def place_ship(self, ship: Ship):
        self.ships.append(ship)
        for x in range(ship.begin[0], ship.end[0]+1):
            for y in range(ship.begin[1], ship.end[1]+1):
                self.set(x, y, Cell(CELL_TYPE_SHIP, ship.type, 1, len(self.ships) - 1))

    def fight_ship(self, x: int, y:int):
        x_, y_ = x-1, y-1
        if ch_xy_wh(x_, y_, self.w, self.h):
            if self.map[y_][x_].type == CELL_TYPE_SHIP:
                if self.map[y_][x_].health != 0:
                    self.map[y_][x_].health = 0
                    self.ships[self.map[y_][x_].ship_id].health -=1
                    return self.map[y_][x_].health
                else:
                    # # cell = self.get()
                    # self.set(x_, y_, Cell(CELL_TYPE_TRY))
                    return -1
            elif self.map[y_][x_].type == CELL_TYPE_EMPTY:
                self.set(x_, y_, Cell(CELL_TYPE_TRY))
                return None
            else:
                return None
        else:
            return None

    def get(self, x: int, y: int):
        x_, y_ = x-1, y-1
        if (ch_xy_wh(x_, y_, self.w, self.h)):
            return self.map[y_][x_]
        else:
            return None
    def set(self, x: int, y: int, v):
        # print("x y", x, y)
        x_, y_ = x-1, y-1
        if (ch_xy_wh(x_, y_, self.w, self.h)):
            self.map[y_][x_] = v
            # print(self.map)
            return True
        else:
            return False
        
    def __str__(self) -> str:
        out = self.id_s + "\t  " + " ".join([chr(i) for i in range(ord("A"), ord("A")+self.w)]) + "\n"
        out +=  "\t\u250C" + "\u2504"*(self.w*2+1) + "\n"
        # for i, row in enumerate(self.map):
        #     out += str(i) + " " 
        #     for el in row:
        #         out += (str(el)  + " ")
        #     out += "\n"
        for y in range(self.h):
            out += str(y+1) + "\t\u250A " 
            for x in range(self.w):
                out += (str(self.get(x+1, y+1))*2)
            out += "\n"
        return out

class FightReq:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

class FightRes:
    def __init__(self, res):
        self.res = res
    def __str__(self):
        return str(self.res)
        

class Player:
    def __init__(self, map: Map):
        self.map = map
    def gen_ships(self):
        pass
    def in_fight(self, req: FightReq) -> FightRes:
        pass
    def out_fight(self) -> FightReq:
        pass
    def out_fight_res(self, res:FightRes):
        pass



class Player_stdio(Player):
    def gen_ships(self):
        print("gen_ships")
        print("example [1 1 u]")
        for i in range(0, 4):
            print("Please enter coordinates of your", i+1, "ships")
            st = input(": ")
            if len(st) == 0:
                continue
            ships = [i.strip() for i in st.split(",")]
            for ship_st in ships:
                x, y, d = map(str.strip, ship_st[1:-1].split())
                x = int(x); y = int(y); d = str(d).lower()
                if d == "u":
                    self.map.place_ship(Ship(i, (x, y-i), (x, y)))
                elif d == "d":
                    self.map.place_ship(Ship(i, (x, y), (x, y+i)))
                elif d == "l":
                    self.map.place_ship(Ship(i, (x-i, y), (x, y)))
                elif d == "r":
                    self.map.place_ship(Ship(i, (x, y), (x+i, y)))
    def in_fight(self, req: FightReq) -> FightRes:
        res = FightRes(self.map.fight_ship(req.x, req.y))  
        print(self.map)
        print(res)
        return res
    def out_fight(self) -> FightReq:
        x, y = map(int, input("Entre x y : ").split())

        return FightReq(x, y)     
    def out_fight_res(self, res:FightRes):
        print(str(res))

class Player_dummy(Player):
    def gen_ships(self):
        print("gen_ships")
        self.map.place_ship(Ship(1, (4, 4), (4, 4)))
        # print("example [1 1 u]")
        # for i in range(0, 4):
        #     print("Please enter coordinates of your", i+1, "ships")
        #     st = input(": ")
        #     if len(st) == 0:
        #         continue
        #     ships = [i.strip() for i in st.split(",")]
        #     for ship_st in ships:
        #         x, y, d = map(str.strip, ship_st[1:-1].split())
        #         x = int(x); y = int(y); d = str(d).lower()
        #         if d == "u":
        #             self.map.place_ship(Ship(i, (x, y-i), (x, y)))
        #         elif d == "d":
        #             self.map.place_ship(Ship(i, (x, y), (x, y+i)))
        #         elif d == "l":
        #             self.map.place_ship(Ship(i, (x-i, y), (x, y)))
        #         elif d == "r":
        #             self.map.place_ship(Ship(i, (x, y), (x+i, y)))
    def in_fight(self, req: FightReq) -> FightRes:
        return FightRes(self.map.fight_ship(req.x, req.y))  
    def out_fight(self) -> FightReq:
        # x, y = map(int, input("Entre x y : ").split())

        # return FightReq(random.randint(1, self.map.w), random.randint(1, self.map.h))     
        return FightReq(1, 1)
    def out_fight_res(self, res:FightRes):
        # print(FightRes)
        pass

# def gen_random_ships(map):
