# 0x15. JavaScript - Web jQuery
---

## Description :newspaper:
This project was created with learning purposes at Holberton School; on `JQuery 3.x` `Chrome 57.0`; and is about Web JQuery.

---

jQuery is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers. With a combination of versatility and extensibility,

---

## Resources :blue_book: :orange_book: :green_book:
Read or watch:
- [JQuery](https://jquery-tutorial.net/introduction/what-is-jquery/)
- [JQuery CheatSheet](https://oscarotero.com/jquery/)
- [JQuery Ajax](https://learn.jquery.com/ajax/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)

Import JQuery
```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

---

## Tasks :white_check_mark:
All below tasks have next conditions (Except if anything else is said):
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API

#### 0. No JQuery
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
- You must use `document.querySelector` to select the HTML tag
- You can’t use the JQuery API

<details>
<summary>Please test with this HTML file in your browser:</summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
```
</details>

#### 1. With JQuery
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
<details>
<summary>
Please test with this HTML file in your browser: </summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
```
</details>

#### 2. Click and turn red
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:
<details>
<summary>Please test with this HTML file in your browser: </summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
```
</details>

#### 3. Add `.red` class
Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`
<details>
<summary>Please test with this HTML file in your browser: </summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
```
</details>

#### 4. Toggle classes
Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:
- The `<header>` element must always have one class: `red` or `green`, never both in the same time and never empty.
- If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.

<details>
<summary>Please test with this HTML file in your browser: </summary

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
```
</details>

#### 5. List of elements
Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:
- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`

<details>
<summary>Please test with this HTML file in your browser: </summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
```
</details>

#### 6. Change the text
Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`
<details>
<summary>Please test with this HTML file in your browser: </summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
```
</details>

#### 7. Star wars character
Write a JavaScript script that fetches the character `name` from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
- The name must be displayed in the HTML tag `DIV#character`

<details>
<summary>Please test with this HTML file in your browser: </summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
```
</details>

The name must be displayed in the HTML tag DIV#character

#### 8. Star Wars movies
Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
- All movie titles must be list in the HTML tag `UL#list_movies`

<details>
<summary>Please test with this HTML file in your browser: </summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
```
</details>

#### 9. Say Hello!
Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`.
- The translation of “hello” must be displayed in the HTML tag `DIV#hello`
- Your script must work when it is imported from the `<head>` tag

<details>
<summary>Please test with this HTML file in your browser: </summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
</details>

---

## Author :bust_in_silhouette:
- [Adrian Vides] | [Twitter] | [GitHub]

---

[GitHub]: <https://github.com/AdrianVides56>
[Twitter]: <https://twitter.com/termi56661>
[Adrian Vides]: <https://www.linkedin.com/in/adrianvides56/>     
