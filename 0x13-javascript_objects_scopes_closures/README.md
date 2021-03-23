# 0x13. JavaScript - Objects, Scopes and Closures
---

## Description :newspaper:
This project was created with learning purposes at Holberton School; on `Ubuntu 14.04` `Node 10`; and is about Objects, Scopes and Closures in JavaScript.

---

### Resources :blue_book: :orange_book: :green_book:
Read or watch:
- [Inheritance in JS](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance)
- [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS)
- [this/self](https://alistapart.com/article/getoutbindingsituations/)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

---

### Tasks :white_check_mark:

#### 0. Rectangle #0
Write an empty class `Rectangle` that defines a rectangle:

#### 1. Rectangle #1
Write a class `Rectangle` that defines a rectangle:
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute width `with` the value of `w`
- Initialize the instance attribute `height` with the value of `h`

#### 2. Rectangle #2
Write a class `Rectangle` that defines a rectangle:
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object

#### 3. Rectangle #3
Write a class `Rectangle` that defines a rectangle:
Create an instance method called `print()` that prints the rectangle using the character `X`

#### 4. Rectangle #4
Write a class Rectangle that defines a rectangle:
- Create an instance method called `print()` that prints the rectangle using the character `X`
- Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
- Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2

#### 5. Square #0
Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:
- You must use the `class` notation for defining your class and `extends`
- The constructor must take 1 argument: `size`
- The constructor of Rectangle` must be called (by using `super()`)

#### 6. Square #1
Write a class `Square` that defines a square and inherits from Square of `5-square.js`:
- You must use the `class` notation for defining your class and extends
- Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
- If `c` is `undefined`, use the character `X`

#### 7. Occurrences
Write a function that returns the number of occurrences in a list:
- Prototype: `exports.nbOccurences = function (list, searchElement)`

#### 8. Esrever
Write a function that returns the reversed version of a list:
- Prototype: `exports.esrever = function (list)`

#### 9. Log me
Write a function that prints the number of arguments already printed and the new argument value. (see example below)
- Prototype: `exports.logMe = function (item)`
- Output format: `<number arguments already printed>: <current argument value>`
```sh
your@shell:~/0x13$ ./9-main.js
0: Hello
1: Holberton
2: School
```

#### 10. Number conversion
Write a function that converts a number from base 10 to another base passed as argument:
- Prototype: `exports.converter = function (base)`

---

## Author :bust_in_silhouette:
- [Adrian Vides] | [Twitter] | [GitHub]



---

[GitHub]: <https://github.com/AdrianVides56>
[Twitter]: <https://twitter.com/termi56661>
[Adrian Vides]: <https://www.linkedin.com/in/adrian-felipe-vides-jimenez-a201401b7>     
