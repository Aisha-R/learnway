# LearnWay

Django backend application for helping users retain information long-term by prompting them to review said information periodically. The intervals implemented in this application are based on the information on this site 'https://www.edapp.com/blog/how-spaced-repetition-works/'.

## Installation

1. Install an IDE (I have Visual Studio Code from 'https://code.visualstudio.com/').
2. Install Python (from 'https://www.python.org/downloads/').
3. Install Postgresql (from 'https://www.postgresql.org/download/').
4. Set up a virtual environment and activate it:

   i. Navigate to the folder you want to create your project within.

   ii. Run the following in the terminal:
      ```python
       python -m venv <project-name>
      ```
      ```cmd
       <project-name>\Scripts\activate.bat
      ```
5. Run the following in the terminal within the virtual environment:
   ```python
    python -m pip install Django
   ```
   ```cmd
    pip install django psycopg2
    pip install python-dotenv
    pip install djangorestframework
    pip install markdown
    pip install django-filter
    pip install djangorestframework-simplejwt
   ```
6. Set the python interpreter to the 'python.exe' file within the Scripts folder.
7. Fork this repository inside the virtual environment.
8. Set up the database:

   i. Create PostgreSQL user and database (with user as owner/all privileges granted).

   ii. Within the virtual environment, run the following:
      ```python
       python manage.py makemigrations
       python manage.py migrate
       python manage.py createsuperuser
       python manage.py runserver
      ```

   iii. Access 'http://127.0.0.1:8000/admin/' and login using the credentials you just created.

*Everytime you open the project you have to activate the virtual environment inside the terminal before you can start the server:
   ```cmd
    ..\Scripts\activate.bat
   ```
   ```python
    python manage.py runserver
   ```

Backup the database at regular intervals from the root directory with:
   ```cmd
    pg_dump -U learnway -F t <username> > db-backups/<database name>-<backup number>.tar
   ```

## Support

These instructions are specific to Windows, for Unix OS you can try to find similar instructions elsewhere online or open an issue and I'll try to help.

## Contributing

For any changes, please open an issue first to discuss what you would like to add or change.

## License

[MIT](https://choosealicense.com/licenses/mit/)