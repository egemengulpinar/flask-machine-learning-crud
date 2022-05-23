# Flask People Manager
A Python-Flask application that performs CRUD actions by allowing a user to add, edit and delete information from a table.<br />

# Installation
After cloning from github, in your terminal, run virtualenv for separate installations of packages for this project:
`virtualenv env`
`source env/bin/activate`
`pip3 install -r requirements.txt`

Run the seeds file to load the database with:
`python3 seeds.py`

Start the server with `python3 server.py`

Begin adding, editing and deleting users!

# References
## Jinja
https://jinja.palletsprojects.com/en/3.0.x/

## Flask
https://pythonise.com/series/learning-flask/flask-http-methods
https://flask.palletsprojects.com/en/2.0.x/testing/

## SQLAlchemy
https://overiq.com/sqlalchemy-101/crud-using-sqlalchemy-orm/

## Python
https://docs.python.org/3/

# Contributing
Bug reports and pull requests are welcome on Github at https://github.com/qfuggett/people-manager-flask.git. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the Contributor Covenant code of conduct.

# License
Copyright 2022 QueenTesa Fuggett

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
