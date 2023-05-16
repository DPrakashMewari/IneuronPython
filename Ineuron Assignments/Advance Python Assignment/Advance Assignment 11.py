# Q1. What is the concept of a metaclass?
# Ans: Metaclass in Python is a class of a class that defines how a class behaves. 
# A class is itself a instance of Metaclass, and any Instance of Class in Python is 
# an Instance of type metaclass. E.g. Type of of int, str, float, list, tuple and many more is of metaclass type.


# Q2. What is the best way to declare a class's metaclass?
# Ans: A way to declare a class’ metaclass is by using metaclass keyword in class definition.

# class meta(type):
#     pass
# class class_meta(metaclass=meta):
#     pass
# print(type(meta))
# print(type(class_meta))


# Q3. How do class decorators overlap with metaclasses for handling instances?
# Class decorators are functions that modify the behavior of a class by wrapping it with another class. 
# They are applied using the "@" syntax immediately before the class definition. 
# Decorators can add or modify attributes and methods of the class, 
# but they don't directly interact with the instance creation process or control the behavior of instances.

# On the other hand, metaclasses are classes themselves and 
# can be used to define the behavior of classes. 
# They are responsible for creating and initializing instances of a class. 
# By defining a metaclass, you can customize how classes are created, 
# which allows you to control the behavior of instances that are created 
# from those classes.




# Q4. How do class decorators overlap with metaclasses for handling instances?
# Class decorators are functions that modify the behavior of a class by wrapping it with another class. 
# They are applied using the "@" syntax immediately before the class definition. 
# Decorators can add or modify attributes and methods of the class, 
# but they don't directly interact with the instance creation process or control the behavior of instances.

# On the other hand, metaclasses are classes themselves and 
# can be used to define the behavior of classes. 
# They are responsible for creating and initializing instances of a class. 
# By defining a metaclass, you can customize how classes are created, 
# which allows you to control the behavior of instances that are created 
# from those classes.