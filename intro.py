# emp1 = {
#     "name":"Ahmed",
#     "id" : 1,
#     "company": "iti",
#     "dept" : "opensource",
#     "address" : "Cairo"
# }
#
# emp2 = {
#     "name": "Mohamed",
#     "id": 2,
#     "company": "iti",
#     "dept": "Telecom"
# }
#
#
# class Course:
#     iso_certifed = True  # class variable
#     def __init__(self, coursename):
#         self.coursename =coursename  # instance variable
#
# python = Course("python")
# print(Course.iso_certifed)
# print(python.iso_certifed)
# python.iso_certifed = False  # this is now not the class variable we created before for the class course
# print(f"this is for Python {python.iso_certifed}")
# Postgres = Course("postgres")
# print(f"this is for postgres {Postgres.iso_certifed}")
#
# Course.iso_certifed = "Courses"
#
# print(python.iso_certifed)
# print(Postgres.iso_certifed)
# print("debugging")
########################

class Car:
    carcount = 0
    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.carcount +=1

    @classmethod
    def carFactory(cls):
        return cls("Fait",128,1985)

    @classmethod
    def addCar(cls,c1, c2):
        brand = c1.brand + c2.brand
        model = c1.model + c2.model
        return cls(brand, model,2023)

c = Car("Kia", "Picanto", 2018)
mm= Car.carFactory()
print(mm)
c2 = Car("Kia", "Soul", 2018)
res=Car.addCar(c, c2)
print(f"new car is {res.brand}, {res.model}, {res.year}")