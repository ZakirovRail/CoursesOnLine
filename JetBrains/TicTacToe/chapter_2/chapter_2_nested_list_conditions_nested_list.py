students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]
list_a = []

for student in students:
    if student[1] == 'A':
        list_a.append(student[0])
print(list_a)
