class Point_1:
  """
  A class to represent a point in 2D space"""

  self.__x: float = 0.0
  self.__y: float = 0.0
  __point_count: int = 0

  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y
    Point1.__point_count += 1

  def __del__(self):
    print("Point has been deleted")
    Point1.__point_count -= 1

  @property
  def x(self):
    return self.__x
  
  @x.setter
  def x(self, value):
    if value <= 100 and value >= -100:
      self.__x = value
    else:
      self.__x = 0.0

  @property
  def y(self):
    return self.__y

  @y.setter
  def y(self, value):
    if value <= 100 and value >= -100:
      self.__y = value
    else:
      self.__y = 0.0

  def shift(self, x_shift: float, y_shift: float):
    self.x += x_shift
    self.y += y_shift

  @staticmethod
  def get_point_count():
    return Point1.__point_count


point1 = Point_1(1.0, 2.0)
point1.shift(1.0, 2.0)
point1.x = 5.0
print(point1.x)
point2 = Point_1(3.0, 4.0)
point3 = Point_1(2.0, 5.0)