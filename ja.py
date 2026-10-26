# class Animal: 
#     def eat(self):                                                               #sin
#         print("Eating")

# class Dog(Animal):               
#     def bark(self):   
#         print("Barking")
# d = Dog()
# d.eat()
# d.bark()




 
# # class Camera:                                                          #muliple 
# #     def photo(self):
# #         print("Taking photo")

# # class Phone:
# #     def call(self):
# #         print("Calling")

# # class SmartPhone(Camera, Phone):
# #     pass

# # s = SmartPhone()
# # s.photo()
# # s.call()




# # class Person:                                                       #multile
# #     def speak(self):
# #         print("Speaking")

# # class Student(Person):
# #     def study(self): 
# #         print("Studying")

# # class CollegeStudent(Student):
# #     pass

# # c = CollegeStudent()
# # c.speak()
# # c.study()




# # class Animal:                                                              #hier
# #     def eat(self):
# #         print("Eating")


# # class Dog(Animal):
# #     pass


# # class Cat(Animal):
# #     pass


# # d = Dog()
# # c = Cat()

# # d.eat()
# # c.eat()







# # class Person:                                              #hybr
# #     def work(self):
# #         print("Working")

# # class Student(Person):
# #     def study(self): 
# #         print("Studying")

# # class Employee(Person):
# #     def earn(self): 
# #         print("Earning")

# # class Intern(Student, Employee):
# #     pass

# # i = Intern()
# # i.work()
# # i.study()
# # i.earn()







# from abc import ABC, abstractmethod
# class car(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class BMW(car):
#     def start(self):
#             print("car started")

# c = BMW()
# c.start()









# class bank:
#      def __init__(self):
#          self.balance=1000


# account=bank()
# account.balance =-5000
# print(account.balance)


# class bank:
#     def __init__(self):
#       self.__balance=1000
#       def set_balance(self,amount):
#          if amount>=0:
#             self.__balance=amount



#     def get_balance(self):
#         return self.__balance


# account = bank()
# account.set_balance(-5000)
# print(account.get_balance())






class bank:
   def __init__(self):
      self._balance=1000



   @property
   def balance(self):
       return self.__balance
   @balance.setter
   def balance(self,amount):
      if amount >=0:
         self.__balance=amount
      else:
         print("invalid balance. balance cannot be negtive")
account=bank()
print("initial balance:",account.balance)

account.balance=5000
print("updated balance:",account.balance)

account.balnce=-2000

print("final balance:",account.balance)






