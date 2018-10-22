import random
names = ["Munir", "Trisha", "Mustakim", "YOusef", "Will", "Mahamed", "Mubeen", "Gyanedra", "Ilyas", "Sabeehah", "Parbhat", "Zain", "Enrico", "Mohammed", "Fayaz"]
group1 = []
group2 = []
group3 = []

while len(names) > 0:
    num = random.randrange(0, len(names), 1)
    group1.append(names[num])
    names.remove(names[num])
    num = random.randrange(0, len(names), 1)
    group2.append(names[num])
    names.remove(names[num])
    num = random.randrange(0, len(names), 1)
    group3.append(names[num])
    names.remove(names[num])
print(group1)
print(group2)
print(group3)
