class Shapes:
    def __init__(self,area,perimeter):
        self.area = area
        self.perimeter = perimeter
    
    def get_area(self):
        return self.area
    
    def get_perimeter(self):
        return self.perimeter
    
class Triangle(Shapes):
    def __init__(self,area,perimeter,category):
        super().__init__(area,perimeter)
        self.category = category
    
    def get_perimeter(self):
        return self.perimeter
    
    def classify(self):
        return self.category
    
class Quadrilateral(Shapes):
    def __init__(self,area,perimeter,type_of):
        super().__init__(area,perimeter)
        self.type_of = type_of

    def get_perimeter(self):
        return self.perimeter
    
    def getType(self):
        return self.type_of

class Child1(Quadrilateral):
    def __init__(self,area,perimeter,type_of,s1,s2,s3,s4):
        super().__init__(area,perimeter,type_of)
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def getType_of(self):
        return self.type_of
    
    def get_sides(self):
        return f"{self.s1},{self.s2},{self.s3},{self.s4}"
    
class Child2(Triangle):
    def __init__(self,area,perimeter,category,a1,a2,a3):
        super().__init__(area,perimeter,category)
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def classify(self):
        return self.category
    
    def get_angles(self):
        return f"{self.a1},{self.a2},{self.a3}"
    
print("Quadrilateral")
q = Child1(600,100,'Rhombus',30,20,30,20)
print(q.get_area())
print(q.get_perimeter())
print(q.get_sides())
print(q.getType_of())
print("Triangle:")
t = Child2(500,150,'Equilateral',50,50,80)
print(t.get_area())
print(t.get_perimeter())
print(t.classify())
print(t.get_angles())