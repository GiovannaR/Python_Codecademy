"""
*Author: Giovanna Avila Riqueti
*Version 1 02/26/2018
"""

class Triangle(object):
  
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    resp = False
    sum = 0
    sum = self.angle1 + self.angle2 + self.angle3
    if sum == 180:
      resp = True
    return resp
  
##########################################################################  
  
class Equilateral(Triangle):
  angle = 60
    
  def __init__(self):
    self.angle1 = self.angle2 = self.angle3 = self.angle
      
      
      
my_triangle = Triangle(90,60,30)
print my_triangle.number_of_sides
print my_triangle.check_angles()