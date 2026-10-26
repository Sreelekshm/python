# class car:
#     def __init__(self,brand,colour):
#         self.brand=brand
#         self.colour=colour


#     def drive(self):
#         print(f"i love {self.colour} {self.brand} car so much")



# car1=car("audi" ,"black")
# car2=car("ciaz","red")



# print(car1.brand)
# car2.drive ()
# print(car2.colour)
# car1.drive()

    

# class student:
#     def __init__(self,name):
#         self.name =name
# s=student("anu")
# print(s.name)



# class student:
#     def __init__(self):
#         print("student created")
# s= student()


# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s = student("anu",21)
# print(s.name) 
# print(s.age)  




class parent:
    def __init__(self):
        print("parent construct")
class child(parent):
    def __init__(self):
                super().__init__()
                print("child constructor")
c  = child()
    

