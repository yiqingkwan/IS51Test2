

"""
The program is trying to show student grades from a final exam.
A text file called "Final.txt" has 24 student grades
It is required to calculate the number of grades, the average grades and the grades that are above average
Then print the outputs, "Number of Grades", "Average Grades", and "Percentage of grades above average".
"""


"""
infile = open("filename", 'r')
L = [line.rstrip() for line in infile]
infile.close
input: student's grade
output: number of grades, average grades, percentage of grades above average
list of grades = lens(grades)
sum = sum of all grades
average = sum of grades / number of grades in list
Percentage of grade above average = 100 * num / lens (grades)

    if grade > average
    "Percentage of grades above average: 100 * grade / lens (grades)"

main
"""


infile = open("Final.txt", 'r')
grades = [line.rstrip () for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0   
for grade in grades:
    if grade > average:
        num +=1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:.02f}%".format(100 * num / len(grades)))
