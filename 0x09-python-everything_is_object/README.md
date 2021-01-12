# 0x09. Python - Everything is object
---
### Description
###### This project was created for learning purposes, answering some questions about objects in python
---
### Tasks
##### 0. Who am I?
What function would you use to print the type of an object?
Write the name of the function in the file, without ```()```.
##### 1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without ```()```.
##### 2. Right count
In the following code, do ```a``` and ```b``` point to the same object? Answer with ```Yes``` or ```No```.
```python
>>> a = 89
>>> b = 100
```
##### 3. Right count =
In the following code, do ```a``` and ```b``` point to the same object? Answer with ```Yes``` or ```No```.
```python
>>> a = 89
>>> b = 89
```
##### 4. Right count =
In the following code, do ```a``` and ```b``` point to the same object? Answer with ```Yes``` or ```No```.
```python
>>> a = 89
>>> b = a
```
##### 5. Right count =+
In the following code, do ```a``` and ```b``` point to the same object? Answer with ```Yes``` or ```No```.
```python
>>> a = 89
>>> b = a + 1
```
##### 6. Is equal 
What do these 3 lines print?
```python
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```
##### 7. Is the same 
What do these 3 lines print?
```python
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```
##### 8. Is really equal 
What do these 3 lines print?
```python
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```
##### 9. Is really the same 
What do these 3 lines print?
```python
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```
##### 10. And with a list, is it equal 
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
##### 11. And with a list, is it the same 
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
##### 12. And with a list, is it really equal
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
##### 13. And with a list, is it really the same
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
##### 14. List append
What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
````
##### 15. List add
What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 [4]
print(l2)
````
##### 16. Integer incrementation
What does this script print?
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
##### 17. List incrementation 
What does this script print?
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
##### 18. List assignation
What does this script print?
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
##### 19. Copy a list object
Write a function def copy_list(l): that returns a copy of a list.
##### 20. Tuple or not?
```python
a = ()
```
Is a a tuple? Answer with ```Yes``` or ```No```.
##### 21. Tuple or not?
```python
a = (1, 2)
```
Is a a tuple? Answer with ```Yes``` or ```No```.
##### 22. Tuple or not?
```python
a = (1)
```
Is a a tuple? Answer with ```Yes``` or ```No```
##### 23. Tuple or not?
```python
a = (1, )
```
Is a a tuple? Answer with ```Yes``` or ```No```
##### 24. Who I am?
What does this script print?
```python
a = (1)
b = (1)
a is b
```
##### 25. Tuple or not
What does this script print?
```python
a = (1, 2)
b = (1, 2)
a is b
```
##### 26. Empty is not empty 
```python
a = ()
b = ()
a is b
```
##### 27. Still the same? 
```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
Will the last line of this script print 139926795932424? Answer with ```Yes``` or ```No```.
##### 28. Same or not? 
```python
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
Will the last line of this script print 139926795932424? Answer with ```Yes``` or ```No```.
##### 29. Python3: Mutable, Immutable... everything is object! 
Write a blog post about everything you just learned / this project is covering. 
##### 35. Clear strings
```shell
termi@ubuntu:/python3$ cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
termi@ubuntu:/python3$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

- How many string objects are created by the execution of the first line of the script? (```106-line1.txt```)
- How many string objects are created by the execution of the second line of the script (```106-line2.txt```)
- After the execution of line 3, is the string object pointed by ```a``` deleted? Answer with ```yes``` or ```No``` (```106-line3.txt```)
- After the execution of line 4, is the string object pointed by b deleted? Answer with ```Yes``` or ```No``` (```106-line4.txt```)
- How many string objects are created by the execution of the last line of the script (```106-line5.txt```)


---
## Author
[Adrian Vides] | [Twitter] | [GitHub]



[GitHub]: <https://github.com/AdrianVides56>
[Twitter]: <https://twitter.com/termi56661>
[Adrian Vides]: <https://www.linkedin.com/in/adrian-felipe-vides-jimenez-a201401b7> 
