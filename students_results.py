print("students results system")
Name = input("Enter students Name: ")
math = float(input("Enter math: "))
english = float(input("Enter english"))
chemistry =float(input("Enter chemistry"))
average  =(math  + english + chemistry)/3
def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"
grade = calculate_grade =(average)
print("/n---resulte---")
print("Name" , Name)
print("avarage" , average)
print("Grade" , grade)



