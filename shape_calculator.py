# Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        text = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        return text

    # To print rectangle area
    def get_area(self):
        area = self.width * self.height
        return area

    # To print rectangle perimeter
    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    # To print rectangle diagonal
    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2) ** .5)
        return diagonal
    
    # To print rectangle picture
    def get_picture(self):
        picture = ""
        star = "*"
        if self.height <= 50:
            if  self.width <= 50:
                for i in range(self.height):
                    line = star * self.width
                    picture += line + "\n"
            else:
                picture = "Too big for picture."
        else:
            picture= "Too big for picture."
        return picture
    
    # To print shape amount_inside
    def get_amount_inside(self, shape):
        shape_height = shape.height
        shape_width = shape.width
        height_times = self.height//shape_height
        width_times = self.width//shape_width
        amount = height_times * width_times
        return amount

    # To set rectangle height
    def set_height(self, height):
        self.height = height
        return self.height

    # To set rectangle width
    def set_width(self, width):
        self.width = width
        return self.width 

class Square(Rectangle):
    def __init__(self, side=9):
        self.side = side
        self.height = self.set_height(side)
        self.width = self.set_width(side)
    
    def set_side(self, side):
        self.height = side
        self.width = side
        return self.width
    
    # To print rectangle area
    def get_area(self):
        area = Rectangle(self.height, self.width).get_area()    
        return area
    
    # To print rectangle perimeter
    def get_perimeter(self):
        perimeter = Rectangle(self.height, self.width).get_perimeter()    
        return perimeter
        
    # To print rectangle diagonal
    def get_daigonal(self):
        diagonal = Rectangle(self.height, self.width).get_diagonal()    
        return diagonal

    # To set rectangle height
    def set_height(self, height):
        self.height = height
        return self.height

    # To set rectangle width
    def set_width(self, width):
        self.width = width
        return self.width 

    # To print shape amount_inside
    def get_amount_inside(self, shape):
        amount = Rectangle(self.height, self.width).get_amount_inside(shape)
        return amount

    def get_picture(self):
        picture = Rectangle(self.height, self.width).get_picture()
        return picture
 