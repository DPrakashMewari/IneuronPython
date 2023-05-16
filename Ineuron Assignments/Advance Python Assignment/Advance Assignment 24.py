# Q1. Is it permissible to use several import statements to import the same module? 
# What would the goal be? Can you think of a situation where it would be beneficial ?

# Ans: Yes, it is permissible to use several import statements to 
# import the same module. It is used in case when we have to import multiple functions from same module.

# ----------------------

# Q2. What are some of a module's characteristics? (Name at least one.)
# Ans: The following are some of a module's characteristics:

# __name__ : It returns the name of the module
# __doc__ : It denotes the documentation string line written in a module code.
# __file__ : It holds the name and path of the module file from which it is loaded
# __dict__ : It return a dictionary object of module attributes, functions and other definitions and their respective values



# Q3. Circular importing, such as when two modules import each other, can lead to dependencies and bugs that aren't visible. How can you go about creating a program that avoids mutual importing?

# Circular imports can indeed lead to dependencies and bugs that are difficult to identify and resolve. 
# To avoid mutual importing and its associated problems, you can follow a few strategies:

# Reorganize your code structure: Circular imports often occur when there is a design flaw in the code organization. \
# Consider restructuring your code to separate concerns and dependencies more clearly. 
# Identify and extract common functionality into separate modules or packages, reducing the likelihood of 
# circular dependencies.

# Use function-level imports: Instead of importing modules at the top-level, you can import them within the functions or methods where they are needed. 
# This approach allows you to defer the import until it is required, avoiding circular import issues. 
# However, it can result in repeated imports and a slight performance overhead, so use it judiciously.

# Dependency inversion: Apply the dependency inversion principle, which states that high-level modules 
# should not depend on low-level modules directly. 
# Instead, both should depend on abstractions. By introducing an abstract interface or base class,
#  you can break the direct circular dependency between two modules, 
# allowing them to depend on the abstraction instead.

# Q4. Why is __all__ in Python ?
# Ans: It provides list of all modules present in a library.


# Q5. In what situation is it useful to refer to the __name__ attribute or the string __main_ _ ?

# The __name__ attribute and the string __main__ are useful in the context of Python scripts and 
# modules when you want to conditionally execute certain code based on how the script is being invoked.

# The __name__ attribute is a special attribute in Python that is automatically 
# set for every module and script. It holds the name of the module or script. 
# When a script is directly executed, its __name__ attribute is set to '__main__'. On the other hand, when a script is 
# imported as a module, its __name__ attribute is set to the actual module name.