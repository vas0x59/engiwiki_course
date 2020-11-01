import utils as u

W = 10
H = 10

# p1_map = u.Map(W, H)
# p2_map = u.Map(W, H)




# print(p1_map)
# print(p2_map)



p1 = u.Player_stdio(u.Map(W, H, "p1"))
p2 = u.Player_dummy(u.Map(W, H, "p2"))

print(p1.map)

p1.gen_ships()

print(p1.map)

print(p2.map)

p2.gen_ships()

print(p2.map)

while True:
    p1.out_fight_res(p2.in_fight(p1.out_fight()))
    p2.out_fight_res(p1.in_fight(p2.out_fight()))