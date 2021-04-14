from game_entry import GameEntry
from scoreboard import ScoreBoard


a = GameEntry("Mike", 1105)
b = GameEntry("Rob", 750)
c = GameEntry("Jill", 740)
d = GameEntry("Paul", 720)
e = GameEntry("Anna", 660)
f = GameEntry("Rose", 590)
g = GameEntry("Jack", 510)

s = ScoreBoard()
s.add(g)
print(str(s))
s.add(a)
print(str(s))
s.add(f)
print(str(s))
s.add(b)
print(str(s))
s.add(c)
print(str(s))

