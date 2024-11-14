#10-4 PROGRAMMING EXERCISE
#WRITE A CLASS NAMED EMPLOYEE THAT HOLDS THE FOLLOWING DATA:
#ATTRIBUTES: NAME, ID NUMBER, DEPARTMENT, AND JOB TITLE
#THEN WRITE A PROGRAM THAT CREATES THREE EMPLOYEE OBJECTS
#THAT HOLD THE FOLLOWING:
#NAME: SUSAN MEYERS, ID NUMBER: 47899, DEPARTMENT: ACCOUNTING, JOB TITLE: VICE PRESIDENT
#NAME: MARK JONES, ID NUMBER: 39119, DEPARTMENT: IT, JOB TITLE: PROGRAMMER
#NAME: JOY ROGERS, ID NUMBER: 81774, DEPARTMENT: MANUFACTURING, JOB TITLE: ENGINEER

#CREATE CLASS NAME EMPLOYEE
class Employee:
      def __init__(self, name, id, department, job_title):
            self.__name = name
            self.__id = id #number
            self.__department = department
            self.__job_title = job_title

      #SET (MUTATOR METHOD)
      def set_name(self, name):
            self.__name = name
      def set_id(self,id):
            self.__id = id
      def set_department(self,department):
            self.__department = department
      def set_job_title(self, job_title):
            self.__job_title = job_title
      #GET (ACCESSOR METHOD)
      def get_name(self):
            return self.__name
      def get_id(self):
            return self.__id
      def get_department(self):
            return self.__department
      def get_job_title(self):
            return self.__job_title
      #STRING METHOD TO DISPLAY EMPLOYEE INFO
      def __str__(self):
            return f"NAME: {self.__name}\n"\
                  f"ID NUMBER: {self.__id}\n"\
                  f"DEPARTMENT: {self.__department}\n"\
                  f"JOB TITLE: {self.__job_title}\n"
def main():
    # CREATE EMPLOYEE OBJECTS
    employee_one = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee_two = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee_three = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    # DISPLAY EMPLOYEE INFO
    print("Employee #1:")
    print(employee_one)
    print("Employee #2:")
    print(employee_two)
    print("Employee #3:")
    print(employee_three)

# RUN
main()
                  
