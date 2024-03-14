file_path = "users.txt"

class Student:   #створення классу студент
  def __init__(self, surname, name, grade):
    self.surname = surname
    self.name = name
    self.grade = grade
    
  def __repr__(self):  #бачення обьекту програмою
    return f"{self.surname} {self.name} - {self.grade} "



def read_students():   #читання з файлу users.txt та добавлення в список students студентів
  with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
      line_list = line.split(" ")
      student = Student(line_list[0],line_list[1],int(line_list[2]))
      students.append(student)



def search_student(student_surname): #функція пошуку студента по прізвищу
  for student in students:
    if student_surname == student.surname:
      print(student)
      break
  else:
    print("Такого студента немає в списку\n")
    
    
  
def average_grade(students):  #рахування середньоі оцінки студентів
  grades = []
  for student in students:
    grades.append(student.grade)
    
  result = sum(grades)/len(grades)
  return result

def add_student(student):   #добавлення студента
  students.append(student)
  


def change_grade(student_surname, new_grade):  #функція зміни оцінки
  for student in students:
    if student_surname == student.surname:
      student.grade = new_grade
      print("оцінку змінено\n")
      break
  else:
    print("Такого студента немає\n")



students = []
read_students()


while True:
  print("1 = пошук студента за Фамілею")
  print("2 = порахувати середню оцінку всіх студентів")
  print("3 = добавити нового студента")
  print("4 = зміна оцінки студента")
  print("5 = зупинка програми та сохранення\n")
  
  question = input("Що ви хочете зробити?:")
  if question == "1":
    student_surname = input("Ведіть прізвище учня:")
    search_student(student_surname)
  elif question == "2":
    print(average_grade(students))
  elif question == "3":
    surname = input("введіть прізвище студента:")
    name = input("введіть імя студента:")
    grade = int(input("введіть середню оцінку студента:"))
    student = Student(surname, name, grade)
    add_student(student)
  elif question == "4":
    student_surname = input("Ведіть прізвище учня якому треба змінити оцінку:")
    new_grade = int(input("Ведіть нову оцінку учня:"))
    change_grade(student_surname, new_grade)
  elif question == "5":
    with open(file_path, "w", encoding="utf-8") as file:
      for student in students:
        file.write(f"{student.surname} {student.name} {student.grade}\n")
    break
  else:
    print("Введено неправильний запит\n")