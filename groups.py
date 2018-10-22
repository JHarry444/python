import random
names = ["Abidul", "Jon", "Nazim", "Vinul", "Munir", "Trisha", "Mustakim", "YOusef", "Will", "Mahamed", "Mubeen", "Gyanedra", "Ilyas", "Sabeehah", "Parbhat", "Zain", "Enrico", "Mohammed", "Fayaz"]
group1, group2, group3, group4 = [], [], [], []
groups = [group1, group2, group3, group4]

while len(names) > 0:
    for group in groups:
        if len(names) == 0:
            break
        num = random.randrange(0, len(names), 1)
        group.append(names[num])
        names.remove(names[num])
print(group1, "\n", group2, "\n", group3, "\n", group4)
