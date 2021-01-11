# Python - More Classes and Objects
---
### Description
###### This project was created for learning purposes, about more classes and objects in python
---
### Tasks
##### 0. Simple rectangle
Write an empty class Rectangle that defines a rectangle
##### 1. Real definition of a rectangle 
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
- Private instance attribute: ```width```
- Private instance attribute: ```heigth```
##### 2.Area and Perimeter
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
- Public instance method: ```def area(self):``` that returns the rectangle area
- Public instance method: ```def perimeter(self):``` that returns the rectangle perimeter
##### 3.String representation
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
- ```print()``` and ```str()``` should print the rectangle with the character #
##### 4.Eval is magic
Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
- ```repr()``` should return a string representation of the rectangle to be able to recreate a new instance by using ```eval()```
##### 5.Detect instance deletion 
Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
- Print the message ```Bye rectangle...``` (```...``` being 3 dots not ellipsis) when an instance of Rectangle is deleted
##### 6.How many instances
Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
- Public class attribute ```number_of_instances:```
    - Initialized to ```0```
    - Incremented during each new instance instantiation
    - Decremented during each instance deletion
##### 7.Change representation
Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)
- Public class attribute ```print_symbol:```
    - Initialized to ```#```
    - Used as symbol for string representation
    - Can be any type
##### 8.Compare rectangles
Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)
- Static method def ```bigger_or_equal(rect_1, rect_2):``` that returns the biggest rectangle based on the area
    - Returns ```rect_1``` if both have the same area value
##### 9.A square is a rectangle
Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
- Class method def ```square(cls, size=0):``` that returns a new Rectangle instance with ```width == height == size```
---
## Author
[Adrian Vides] | [Twitter] | [GitHub]



[GitHub]: <https://github.com/AdrianVides56>
[Twitter]: <https://twitter.com/termi56661>
[Adrian Vides]: <https://www.linkedin.com/in/adrian-felipe-vides-jimenez-a201401b7> 
