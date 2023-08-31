# LearnWay

Django backend application for helping users retain information long-term by prompting them to review said information periodically. The intervals implemented in this application are based on the information on this site 'https://www.edapp.com/blog/how-spaced-repetition-works/'.

## Installation

1. Install an IDE (I have Visual Studio Code from 'https://code.visualstudio.com/').
2. Install Python (from 'https://www.python.org/downloads/').
3. Install Postgresql (from 'https://www.postgresql.org/download/').
4. Set up a virtual environment and install Django within it (according to the instructions on 'https://docs.djangoproject.com/en/4.2/howto/windows/').
5. Set the python interpreter to the 'python.exe' file within the Scripts folder.
6. In the terminal, run:
   ```cmd
    pip install djangorestframework-simplejwt
   ```
7. Fork this repository inside the virtual environment.
8. Sep up the database connection (according to the instructions on 'https://medium.com/@rudipy/how-to-connecting-postgresql-with-a-django-application-f479dc949a11').

   i. Make sure to hide your password in an '.env' file (according to the instructions on: 'https://pypi.org/project/python-dotenv/').
9. Set up DRF (according to the instructions on 'https://www.django-rest-framework.org/#installation').
10. Run the following inside the terminal:*
   ```cmd
    ..\Scripts\activate.bat
   ```
   ```python
    py manage.py runserver
   ```
*You have to do this step everytime you open the project.

Backup the database at regular intervals inside a folder (+ place the folder in .gitignore) from the root directory with:
   ```cmd
      pg_dump -U learnway -F t <username> > db-backups/<database name>-<backup number>.tar
   ```

## Support

These instructions are specific to Windows, for Unix OS you can try to find similar instructions elsewhere online or open an issue and I'll try to help.

## Roadmap

The aim of this project is to learn how to use Django and thereafter secure a job as a python backend developer. Short-term goal is to produce a minimally viable product complete with testing, before I move on to implementing additional features. Ordinarily I would take a TDD approach, but for the purposes of learning Django I will get the basics down before I start testing.

For prospective employers, if you would like to set me a task to complete or a feature to add as part of the application process feel free to do so.

## Contributing

For any changes, please open an issue first to discuss what you would like to add or change.

## License

[MIT](https://choosealicense.com/licenses/mit/)