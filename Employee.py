#  task 02 : soppose ur working in a xyz company and they demands a software the takes the details of an emp 
# such as
# empId
# empname
# empSalz
# empDept
# and also print the required details ...
class Employee:
    def __init__(self, empId, empName, empSal, empDept):
        self.empId = empId
        self.empName = empName
        self.empSal = empSal
        self.empDept = empDept

    def displaydetails(self):
        print("Employee ID:",self.empId)
        print("Employee Name:",self.empName)
        print("Employee Salary:",self.empSal)
        print("Employee Department:",self.empDept)

def getemployeedetails():
    empId = input("Enter Employee ID: ")
    empName = input("Enter Employee Name: ")
    empSal = float(input("Enter Employee Salary: "))
    empDept = input("Enter Employee Department: ")

    return Employee(empId, empName, empSal, empDept)

emp = getemployeedetails()
print("Employee Details:")
emp.displaydetails()


