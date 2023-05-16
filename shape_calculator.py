class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return 'Rectangle(width={}, height={})'.format(self.width, self.height)
  
  def get_area(self):
    return int(self.width) * int(self.height)

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    end_picture = ''
    if self.width > 50 or self.height >50:
      return "Too big for picture."
    else:
      for x in range(self.height):
        width = int(self.width)
        end_picture += '*'*width + '\n'
      return end_picture

  def get_amount_inside(self, new_shape):
    number_of_widths = 0
    number_of_height = 0
    old_width = self.width
    old_height = self.height
    while old_height >= new_shape.height:
          number_of_height += 1
          old_height -= new_shape.height
    while old_width >= new_shape.width:
      number_of_widths += 1
      old_width -= new_shape.width
    return number_of_widths * number_of_height


class Square(Rectangle):
  def __init__(self, length):
    self.width = length
    self.height = length
  def set_side(self, new_length):
    self.width = new_length
    self.height = new_length
  def __repr__(self):
    return 'Square(side={})'.format(self.width)
