# deepwork2 - The application

After I read the book Deep Work, by Cal Newport, I started tracking my coding study/work hours in a simple text file. As the file got bigger, I wanted to see things like total hours for a month, or cumulative totals, without having to to the math every time, so I created a Flask app to track and view my deep work time.

![deepwork2 screenshot](deepwork2-screenshot.png?raw=true)

### Technologies used

* Flask (Python web micro-framework)
* SQLite (lightweight SQL database engine)
* SQLAlchemy (database ORM) - flask-sqlalchemy
* Alembic (database migration) - flask-migrate
* Bootstrap (CSS styles) - flask-bootstrap

### How to install deepwork2

1. Clone the repo on your local machine: `git clone https://github.com/thomasjohncole/deepwork2.git`
2. Make a Python virtual environment:`python3 -m venv venv`
3. Activate virtual environment: `. venv/bin/activate`
4. Install requirements.txt: `pip install -r requirements.txt`
5. Create the database, from the python REPL:
```
>>> from work import db
>>> db.create_all()
>>> exit()
```
7. Add some data, from the sqlite prompt (`sqlite3 deepwork.db`): `INSERT INTO dailyhours VALUES ('2022-06-01', '4', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit');
`
8. Exit sqlite and start the server: `flask run`
9. Point your browser to localhost:5005

### Tasks

- [x] Fix header in edit and delete forms
- [x] Make header modular and use include across templates
- [x] Refactor based on best practices for file separation
- [x] Add date picker on form templates
- [x] Add WTForms for validation and security purposes
- [x] Error processing for Add day page, can use WTForms here
- [x] Make month links autogenerate based on what is in the db
- [ ] Add user login module - flask-login
- [ ] Deploy a demo of this app: Heroku, AWS, Linode, etc.
- [ ] Add some visualizations, graphs, charts, etc.
- [ ] Add an about page


