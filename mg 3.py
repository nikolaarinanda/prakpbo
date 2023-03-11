# Tugas praktikum 3 kelas RA
class Robot:
    def __init__(self, name, health, skill, armor):
        self.name = name
        self.health = health
        self.skill = skill
        self.armor = armor

    def Attack(self, damage, defense):
        if (defense == True):
            self.health -= damage / 2 - self.armor
        else:
            self.health -= damage - self.armor

    def Mute(self):
        self.defense = False

    def Defense(self):
        self.defense = True

    def GiveUp(self, diri, musuh):
        if musuh[1] >= diri[1] and musuh[2] >= diri[2] and musuh[3] >= diri[3]:
            return True
        else:
            return False
        
print("Masukan informasi robot 1: ")
robot_1 = Robot(input(), input(), input(), input())\

while True:
    mode_robot_1 = (input("Masukan mode robot (1.Mute 2.Defense): "))
    if mode_robot_1 == 1:
        robot_1.Mute()
        break
    elif mode_robot_1 == 2:
        robot_1.Defense()
        break
    else:
        print("Mode yang anda masukan tidak ada, coba masukan kembali !!")

print("Masukan informasi robot 2: ")
robot_2 = Robot(input(), input(), input(), input())
while True:
    mode_robot_2 = (input("Masukan mode robot (1.Mute 2.Defense): "))
    if mode_robot_2 == 1:
        robot_2.Mute()
        break
    elif mode_robot_2 == 2:
        robot_2.Defense()
        break
    else:
        print("Mode yang anda masukan tidak ada, coba masukan kembali !!")

info_robot_1 = (robot_2.health, robot_2.skill, robot_2.armor)
info_robot_2 = (robot_1.health, robot_1.skill, robot_1.armor)

if robot_1.GiveUp(info_robot_1, info_robot_2):
    print("Robot {} menyerah, pemenangnya adalah robot {} !!!".format(robot_1.name, robot_2.name))
elif robot_2.GiveUp(info_robot_2, info_robot_1):
    print("Robot {} menyerah, pemenangnya adalah robot {} !!!".format(robot_2.name, robot_1.name))
else:
    while True:
        robot_1.Attack(robot_2.skill, robot_1.defense)
        if robot_1.health > 0:
            print("Healt robot {}: {}".format(robot_1.name, robot_1.health))
        elif robot_1.health <= 0:
            robot_1.health = 0
            print("Healt robot {}: {}".format(robot_1.name, robot_1.health))
            print("Robot {} berhasil dikalahkan oleh robot {} !!!".format(robot_1.name, robot_2.name))
            break

        robot_2.Attack(robot_1.skill, robot_2.defense)
        if robot_2.health > 0:
            print("Healt robot {}: {}".format(robot_2.name, robot_2.health))
        elif robot_2.health <= 0:
            robot_2.health = 0
            print("Healt robot {}: {}".format(robot_2.name, robot_2.health))
            print("Robot {} berhasil dikalahkan oleh robot {} !!!".format(robot_2.name, robot_1.name))
            break
