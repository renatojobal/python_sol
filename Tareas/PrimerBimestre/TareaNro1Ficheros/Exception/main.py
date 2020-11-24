
class RadiusInputError(ValueError): 
  """ 
  Exception class
  """
  pass
  
class Circle:
  """
  Circle classs with attribute radius
  """
  
  def __init__(self, radius):
    """
    If radius is not a number raise RadiusInputError
    """
    try:
      self.radius = float(radius)
    except Exception:
      raise RadiusInputError(radius, "is not a number")
      
      
  def __str__(self):
    return ("Circle with raius: %.2f \n" % (self.radius))


# Tests
      
circle = Circle(8)
print(circle)

circle2 = Circle("hello")
print(circle2)

      

  
  
