# 0x00. Python - Hello, World
---

## Description :newspaper:
This project was created with learning purposes at Holberton School; on `Ubuntu 14.04` `python 3.4.x`; and is an introduction to Python.

---

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

---

### Resources :blue_book: :orange_book: :green_book:
Read or watch:
- [The Python Tutorial](https://docs.python.org/3.4/tutorial/index.html)
- [String Formatting](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
- [Learn To Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [PEP8 Style](https://www.python.org/dev/peps/pep-0008/)

---

### Tasks :white_check_mark:

#### 0. Run Python file
Write a Shell script that runs a Python script.
- The Python file name will be saved in the environment variable `$PYFILE`

  `cat main.py`
  ```python
  #!/usr/bin/python3
  print("Holberton School")
  ```
  ```shell
  your@shell:~/py/0x00$ export PYFILE=main.py
  your@shell:~/py/0x00$ ./0-run
  Holberton School
  ```

#### 1. Run inline
Write a Shell script that runs Python code.
- The Python code will be saved in the environment variable `$PYCODE`
  ```shell
  your@shell:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
  your@shell:~/py/0x00$ ./1-run_inline 
  Holberton School: 98
  ```

#### 2. Hello, print
Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
  ```shell
  your@shell:~/py/0x00$ ./2-print.py 
  "Programming is like building a multilingual puzzle
  ```

#### 3. Print integer
Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.
  ```shell
  your@shell:~/py/0x00$ ./3-print_number.py
  98 Battery street
  ```

#### 4. Print float
Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable number with a precision of 2 digits.
- he output of the program should be:
-   - `Float:`, followed by the float with only 2 digits
  ```shell
  your@shell:~/py/0x00$ ./4-print_float.py
  Float: 3.14
  ```

#### 5. Print string
Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
- The output of the program should be:
  - 3 times the value of `str`
  - followed by a new line
  - followed by the 9 first characters of `str`
  ```shell
  your@shell:~/py/0x00$ ./5-print_string.py 
  Holberton SchoolHolberton SchoolHolberton School
  Holberton
  ```

#### 6. Play with strings
Complete [this source](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) code to print Welcome to Holberton School!
- You are not allowed to use any loops or conditional statements.
- You have to use the variables `str1` and `str2` in your new line of code
- Your program should be exactly 5 lines long
```shell
your@shell:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
```

#### 7. Copy - Cut - Paste
Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)
- Your program should be exactly 8 lines long
- `word_first_3` should contain the first 3 letters of the variable `word`
- `word_last_2` should contain the last 2 letters of the variable `word`
- `middle_word` should contain the value of the variable `word` without the first and last letters
```shell
your@shell:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```

#### 8. Create a new sentence
Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print object-oriented programming with Python, followed by a new line.
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals
  ```shell
  your@shell:~/py/0x00$ ./8-concat_edges.py
  object-oriented programming with Python
  ```

#### 9. Easter Egg
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
- Your script should be maximum 98 characters long 

#### 10. Linked list cycle
Write a function in C that checks if a singly linked list has a cycle in it.
- Prototype: `int check_cycle(listint_t *list);`
- Return: `0` if there is no cycle, `1` if there is a cycle

---

## Author :bust_in_silhouette:
- [Adrian Vides] | [Twitter] | [GitHub]



---

[GitHub]: <https://github.com/AdrianVides56>
[Twitter]: <https://twitter.com/termi56661>
[Adrian Vides]: <https://www.linkedin.com/in/adrian-felipe-vides-jimenez-a201401b7>     

