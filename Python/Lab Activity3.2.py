name = (input("Name: "))
course = (input("Course: "))
year_level = (input("Year Level (1/2/3): "))
CC1_Grade = float (input("Input grade for CC1: "))
CC2_Grade = float (input("Input grade for CC2: "))
CC7_Grade = float (input("Input grade for CC7: "))
average_grade = ((CC1_Grade + CC2_Grade + CC7_Grade) / 3)
print(f"Hello", name, "of", course, year_level, "Here are your grades and average: ")
print("CC1 Grade: ",CC1_Grade)
print("CC2 Grade: ", CC2_Grade)
print("CC7 Grade: ", CC7_Grade)
print("Average: ", average_grade)