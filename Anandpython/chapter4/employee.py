class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary  
emp1 = Employee("sara",2000)
emp1.displayEmployee()
print "Total Employees %d" % Employee.empCount
emp1.age = 7 #### add an age attribute
