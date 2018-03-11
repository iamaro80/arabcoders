class Parent():
    def __init__(self, last_name, eye_color):
        print 'Parent Constructor is Called'
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print 'Last Name: ', self.last_name
        print 'Eye Color: ', self.eye_color


class Child(Parent):
    def __init__(self,last_name, eye_color, number_of_toys):
        print 'Child Constructor is Called'
        Parent.__init__(self,last_name, eye_color)
        self.number_of_toys = number_of_toys
    def show_info(self):
        print 'Number of Toys:', self.number_of_toys


# ibrahim  = Parent('Maro','Brown')
elyas = Child('Ibrahim','Black',10)
elyas.show_info()
# print ibrahim.eye_color
# print elyas.number_of_toys
