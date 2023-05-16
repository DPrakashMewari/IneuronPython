# Q1. What is the difference between __getattr__ and __getattribute__?

    # 1.
    # __getattr__: This method is called only when the requested attribute is not found through normal attribute lookup. 
    # It is invoked when an attribute that doesn't exist is accessed. This method takes the attribute name as a parameter 
    # and can return a value or raise an AttributeError if the attribute is not found.

    # 2.
    # __getattribute__: This method is called for every attribute access on an object, regardless of whether the attribute exists or not. 

    # Difference
    # __getattr__ is called when an attribute is not found through normal attribute lookup, while __getattribute__ is called for every attribute access, regardless of whether the attribute exists or not.

# ---------------------

# Q2. What is the difference between properties and descriptors?

    # Properties and descriptors are both mechanisms in Python that allow you to define custom behavior for attribute access

    # Properties:

    # Properties are a simpler and more straightforward way to define computed or dynamic attributes in Python.
    # Properties are defined using the @property decorator and can be accessed like regular attributes.
    # Properties allow you to define getter, setter, and deleter methods, which are automatically called when the property is accessed, assigned a value, or deleted.


    # Descriptors:

    # Descriptors provide a more low-level and flexible mechanism for defining custom attribute access.
    # Descriptors are defined as classes with special methods such as __get__, __set__, and __delete__.
    # Descriptors can be used to define custom behavior for attribute access on a class or an instance level.

    # Difference
    # properties provide a simpler way to define computed or dynamic attributes with predefined getter, setter, and deleter methods, 
    # while descriptors offer more flexibility and control over attribute access and can be shared across multiple attributes and classes

# ---------------------

# Q3. What are the key differences in functionality between __getattr__ and __getattribute__, as well as
    # properties and descriptors?

    # The key differences in functionality between __getattr__ and __getattribute__, as well as properties and descriptors, 
    # can be summarized as follows:

    # __getattr__ vs. __getattribute__:

    # __getattr__ is only called when the requested attribute is not found through normal attribute lookup, \
    #     while __getattribute__ is called for every attribute access, regardless of whether the attribute exists or not.


    # Properties vs. Descriptors:

    # Properties are a high-level way to define computed or dynamic attributes using the @property decorator. 
    # They allow you to define custom behavior for attribute access, assignment, and deletion through getter, 
    # setter, and deleter methods.

    # Descriptors are a lower-level mechanism for defining custom attribute access. 
    # They are implemented as classes with __get__, __set__, and __delete__ methods, 
    # allowing more flexibility and control over attribute access.