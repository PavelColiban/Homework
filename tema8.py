import add_data
import read_data


print("""....Registru....
    1.Adaugare a datelor
    2.Citirea datelor
        """)
a = int(input("Ce varianta alegi: "))


if a == 1:
    add_data.addData("Pavel", 9, "History, Maths, Deutsch, Englisch", 10)
else:
    read_data.readData()