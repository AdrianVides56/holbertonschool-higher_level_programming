# 0x0A-python-inheritance
---
### Description
###### This project was created for learning purposes, about the Inheritance in Python
---
### Resources
###### Read or watch:
- [Inheritance]
- [Inheritance in Python]
---
### Tasks
##### 0. Lookup
Write a function that returns the list of available attributes and methods of an object:
- Prototype: ```def lookup(obj):```
##### 1. My list 
Write a class ```MyList``` that inherits from ```list```:
- Public instance method: ```def print_sorted(self):``` that prints the list, but sorted (ascending sort)
- Assume that all elements of the list will be of type ```int```
##### 2. Exact same object
Write a function that returns ```True``` if the object is exactly an instance of the specified class ; otherwise ```False```.
- Prototype: ```def is_same_class(obj, a_class):```
##### 3. Same class or inherit from
Write a function that returns ```True``` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise ```False```.
- Prototype: ```def is_kind_of_class(obj, a_class):```
##### 4. Only sub class of 
Write a function that returns ```True``` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise ```False```.
- Prototype: ```def inherits_from(obj, a_class):```
##### 5. Geometry module
Write an empty class ```BaseGeometry```.
##### 6. Improve Geometry 
Write a class ```BaseGeometry``` (based on ```5-base_geometry.py```).
- Public instance method: ```def area(self):``` that raises an ```Exception``` with the message ```area() is not implemented```
##### 7. Integer validator 
Write a class ```BaseGeometry``` (based on ```6-base_geometry.py)```.
- Public instance method: ```def integer_validator(self, name, value):``` that validates value:
    - you can assume ```name``` is always a string
    - if ```value``` is not an integer: raise a ```TypeError``` exception, with the message ```<name> must be an integer```
    - if ```value``` is less or equal to 0: raise a ```ValueError``` exception with the message ```<name> must be greater than 0```
##### 8. Rectangle
Write a class ```Rectangle``` that inherits from BaseGeometry (```7-base_geometry.py```).
- Instantiation with ```width``` and ```height```: ```def __init__(self, width, height):```
##### 9. Full rectangle
Write a class ```Rectangle``` that inherits from ```BaseGeometry``` (```7-base_geometry.py```). (task based on ```8-rectangle.py```)
- the ```area()``` method must be implemented
- ```print()``` should print, and ```str()``` should return, the following rectangle description: ```[Rectangle] <width>/<height>```
##### 10. Square #1 
Write a class ```Square``` that inherits from ```Rectangle``` (```9-rectangle.py)```:
##### 11. Square #2 
Write a class ```Square``` that inherits from ```Rectangle``` (```9-rectangle.py```). (task based on ```10-square.py```).

---
## Author
[Adrian Vides] | [Twitter] | [GitHub]

[Inheritance]: <https://docs.python.org/3.4/tutorial/classes.html#inheritance>
[Inheritance in Python]: <https://hub.packtpub.com/inheritance-python/>
[GitHub]: <https://github.com/AdrianVides56>
[Twitter]: <https://twitter.com/termi56661>
[Adrian Vides]: <https://www.linkedin.com/in/adrian-felipe-vides-jimenez-a201401b7> 
