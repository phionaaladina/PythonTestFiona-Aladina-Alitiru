# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F



def student_grade():
    Percentage = int(input('Please enter your marks:'))


    if Percentage >=90:
        print('Grade: A') 
    elif Percentage >= 80:
        print('Grade B')
    elif Percentage >= 70: 
        print('Grade C')

    elif Percentage >= 60: 
        print('Grade D')
    elif Percentage >= 40: 
        print('Grade E')
    else:
        print('Grade F') 

student_grade()
