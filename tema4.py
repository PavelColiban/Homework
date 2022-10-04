note = []
elev = []
subject = []
med_tot = []

st_num = input("Inroduce numele elevului: ")
elev.append(st_num)

obj_num = input("Cate obiecte are: ")
subject.append(obj_num)

ob1_num = float(input("Ce medii ai: "))
note.append(ob1_num)

ob2_num = float(input("Ce medii ai: "))
note.append(ob2_num)

ob3_num = float(input("Ce medii ai: "))
note.append(ob3_num)

ob4_num = float(input("Ce medii ai: "))
note.append(ob4_num)

med_tot = (note[0] + note[1] + note[2] + note[3]) / 4

# print("Media totala e egala cu " + str(med_tot))

print("Elevul(a) " + str(elev) + " la obiectele " + str(subject) + " are mediile " + str(note) + " si media totala e " + str(med_tot))





