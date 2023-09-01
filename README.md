# LearnWay

Django backend application for helping users retain information long-term by prompting them to review said information periodically. The intervals implemented in this application are based on the information on this site 'https://www.edapp.com/blog/how-spaced-repetition-works/'.

## Installation

1. Install an IDE (I have Visual Studio Code from 'https://code.visualstudio.com/').
2. Install Python (from 'https://www.python.org/downloads/').
3. Install Postgresql (from 'https://www.postgresql.org/download/').
4. Set up a virtual environment and activate it:
   i. Navigate to the folder you want to create your project within.
   ii. Run the following in the terminal:
      ```cmd
       py -m venv <project-name>
       <project-name>\Scripts\activate.bat
      ```
5. Run the following in the terminal within the virtual environment:
   ```cmd
    py -m pip install Django
    pip install django psycopg2
    pip install python-dotenv
    pip install djangorestframework
    pip install markdown
    pip install django-filter
    pip install djangorestframework-simplejwt
   ```
5. Set the python interpreter to the 'python.exe' file within the Scripts folder.
7. Fork this repository inside the virtual environment.
8. Set up the database connection (according to the instructions on 'https://medium.com/@rudipy/how-to-connecting-postgresql-with-a-django-application-f479dc949a11').

*Everytime you open the project you have to activate the virtual environment inside the terminal before you can start the server:
   ```cmd
    ..\Scripts\activate.bat
   ```
   ```python
    py manage.py runserver
   ```

Backup the database at regular intervals from the root directory with:
   ```cmd
      pg_dump -U learnway -F t <username> > db-backups/<database name>-<backup number>.tar
   ```

## Support

These instructions are specific to Windows, for Unix OS you can try to find similar instructions elsewhere online or open an issue and I'll try to help.

## Roadmap

The aim of this project is to learn how to use Django and thereafter secure a job as a Python Backend Developer. The short-term goal is to produce a minimally viable product complete with testing, before I move on to implementing additional features. Ordinarily I would take a TDD approach, but for the purposes of learning Django I will get the basics down before I start testing.

For prospective employers, if you would like to set me a task to complete or a feature to add as part of the application process feel free to do so.

## Contributing

For any changes, please open an issue first to discuss what you would like to add or change.

## License

[MIT](https://choosealicense.com/licenses/mit/)