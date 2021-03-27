# 0x0F. Python - Object-relational mapping
---

## Description :newspaper:
This project was created with learning purposes at Holberton School; on `Ubuntu 14.04` `MySQL. 5.7` `MySQLdb 1.3.x` `SQLAlchemy 1.2.x`; and is about Object-Relational Mapping

---

ORM (Object-Relational Mapping) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.

---

### Resources :blue_book: :orange_book: :green_book:
Read or watch:
- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
- [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)

---

### Tasks :white_check_mark:

All tasks will follow this instructions, unless another ones are specified
- Your script should take 3 arguments: `mysql username`, `mysql password` and _`extra argument`_ (no argument validation needed)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

#### 0. Get all states
Write a script that lists all `states` from the database `hbtn_0e_0_usa`:
- Your script should take 3 arguments: `mysql username`, ``mysql password`` and ``database name`` (no argument validation needed)
```shell
your@shell:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL,
	    PRIMARY KEY (id)
	    );
	    INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

your@shell:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
your@shell:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

#### 1. Filter states
Write a script that lists all states with a name starting with `N` from the database `hbtn_0e_0_usa`:
- - Your script should take 3 arguments: `mysql username`, ``mysql password`` and ``database name`` (no argument validation needed)
```shell
your@shell:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL,
	    PRIMARY KEY (id)
	    );
	    INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

your@shell:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
your@shell:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
```

#### 2. Filter states by user input
Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where name matches the argument.
- Your script should take 4 arguments: ``mysql username``, ``mysql password``, ``database name`` and ``state name searched`` (no argument validation needed)
```shell
your@shell:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

your@shell:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
your@shell:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

#### 3. SQL Injection...
Wait, do you remember the previous task? Did you test ``"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"`` as an input?
What? Empty?
Yes, it’s an [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) to delete all records of a table…
Once again, write a script that takes in arguments and displays all values in the ``states`` table of ``hbtn_0e_0_usa`` where ``name`` matches the argument. But this time, write one that is safe from MySQL injections!
- Your script should take 4 arguments: ``mysql username``, ``mysql password``, ``database name`` and ``state name searched`` (no argument validation needed)
```shell
your@shell:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

your@shell:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
your@shell:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

#### 4. Cities by states
Write a script that lists all ``cities`` from the database ``hbtn_0e_4_usa``
- Your script should take 3 arguments: `mysql username`, ``mysql password`` and ``database name``
```
your@shell:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

your@shell:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
your@shell:~/0x0F$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
```

#### 5. All cities by state
Write a script that takes in the name of a state as an argument and lists all ``cities`` of that state, using the database ``hbtn_0e_4_usa``
```shell
your@shell:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

your@shell:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

your@shell:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
your@shell:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
your@shell:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii
```

#### 6. First state model
Write a python file that contains the class definition of a ``State`` and an instance ``Base = declarative_base()``:

- `State` class:
    - inherits from ``Base`` Tips
    - links to the MySQL table `states`
    - class attribute ``id`` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    - class attribute ``name`` that represents a column of a string with maximum 128 characters and can’t be null
```shell
your@shell:~/0x0F$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

your@shell:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
your@shell:~/0x0F$ cat 6-model_state.py
#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

your@shell:~/0x0F$ ./6-model_state.py root root hbtn_0e_6_usa
your@shell:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

#### 7. All states via SQLAlchemy
Write a script that lists all ``State`` objects from the database ``hbtn_0e_6_usa``
- Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``
- You must import ``State`` and ``Base`` from ``model_state`` - ``from model_state import Base, State``
```shell
your@shell:~/0x0F$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

your@shell:~/0x0F$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
your@shell:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
```

#### 8. First state
Write a script that prints the first ``State`` object from the database ``hbtn_0e_6_usa``
- Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``
- You must import ``State`` and ``Base`` from ``model_state`` - ``from model_state import Base, State``
- If the table `states` is empty, print `Nothing` followed by a new line
```shell
your@shell:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
```

#### 9. Contains `a`
Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
- Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``
- You must import ``State`` and ``Base`` from ``model_state`` - ``from model_state import Base, State``
```sell
your@shell:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
```

#### 10. Get a state
Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`
- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name to search` (SQL injection free)
- You must import `State` and `Base` from `model_stat`e - f`rom model_state import Base, State`
- If no state has the name you searched for, display `Not found`
```shell
your@shell:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
your@shell:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
```

#### 11. Add a new state
Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Print the new `states.id` after creation
```shell
your@shell:~/0x0F$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
your@shell:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
```

#### 12. Update a state
Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Change the name of the `State` where `id = 2` to `New Mexico`
```shell
your@shell:~/0x0F$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
your@shell:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
```

#### 13. Delete states
Write a script that deletes all `State` objects with a name containing the letter a from the database `hbtn_0e_6_usa`
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
```shell
your@shell:~/0x0F$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
your@shell:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
2: New Mexico
4: New York
```

#### 14. Cities in state
Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.

- `City` class:
    - inherits from `Base` (imported from `model_state`)
    - links to the MySQL table `cities`
    - class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    - class attribute `name` that represents a column of a string of 128 characters and can’t be null
    - class attribute `state_id` that represents a column of an integer, can’t be null and is a foreign key to `states.id`

Next, write a script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`:
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Results must be display as they are in the example below (`<state name>: (<city id>) <city name>`)
```shell
your@shell:~/0x0F$ cat 14-model_city_fetch_by_state.sql
-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

your@shell:~/0x0F$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password: 
your@shell:~/0x0F$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
```


---

## Author :bust_in_silhouette:
- [Adrian Vides] | [Twitter] | [GitHub]



---

[GitHub]: <https://github.com/AdrianVides56>
[Twitter]: <https://twitter.com/termi56661>
[Adrian Vides]: <https://www.linkedin.com/in/adrian-felipe-vides-jimenez-a201401b7>     
