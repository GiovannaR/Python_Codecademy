"""
*Author: Giovanna Avila Riqueti
*Version 1 02/26/2018
"""

class Employee(object):
  
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

###############################################################################


class PartTimeEmployee(Employee):
  
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)
  
  
milton = PartTimeEmployee("Milton")

print milton.full_time_wage(10)