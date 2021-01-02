def calculate_grade(line):
    line=line[:-1] # Bu her satirdaki boslugu kaldirmak icindi.

    list1=line.split(",")

    print(list1)

    name=list1[0]

    grade1=int(list1[1])
    grade2=int(list1[2])
    grade3=int(list1[3])
    last_grade=grade1 * (3/10) + grade1*(3/10) + grade3*(4/10)

    if last_grade>=90:
        letter="AA"
    elif last_grade>=85:
        letter="BA"
    elif last_grade >= 80:
        letter = "BB"
    elif last_grade >= 75:
        letter = "CB"
    elif last_grade >= 75:
        letter = "CC"
    elif last_grade >= 65:
        letter = "DC"
    elif last_grade >= 60:
        letter = "DD"
    elif last_grade >= 55:
        letter = "FD"
    else:
        letter="FF"

    return name + "------------->" + letter +"\n"


with open("dosya.txt","r",encoding="utf-8") as file:
    will_append_list=[]

    for i in file:
        will_append_list.append(calculate_grade(i))

    # print(will_append_list) Bu sekilde  ['Hatice Günday------------->FF\n' gorebiliyoruz bunu bir dosyaya ekleyelim.

with open("notlar.txt","w",encoding="utf-8") as file2:
    for i in will_append_list:
        file2.write(i)





