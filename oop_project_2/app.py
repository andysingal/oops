

def create_student():
    name = input("Please enter the new student's name: ")  #Ask the user for the student's name
    student_data = {
        'name': name,
        'marks': []
    }                                                      #Create the dictionary in the format {'name': <student_name>, 'marks':[]}
    return student_data

def add_mark(student, mark):
    student['marks'].append(mark)     # Append a mark to the student dictionary


def calculate_average_mark(student):
    number = len(student['marks'])    #add together all of the student["marks"]
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number

def print_student_details(student):
    print("{}, average mark: {}.".format(student['name'],
                                         calculate_average_mark(student)))

def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)