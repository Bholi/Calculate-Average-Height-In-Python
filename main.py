print('Welcome to the program that calculates average height without using any inbuilt functions')

student_heights = input('Enter the heights separated by comma : ').split(',')
for n in range(0, len(student_heights)):
    student_heights[n] = student_heights[n]
print(student_heights)
d = 0
s = 0
for i in student_heights:
    d += 1

for j in student_heights:
    s += int(j)
print(round(s / d))
