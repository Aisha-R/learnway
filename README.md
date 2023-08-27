# LearnWay

Python/Django backend for helping users retain information long-term by prompting them to review said information periodically. The intervals implemented in this application are based on the information on this site 'https://www.edapp.com/blog/how-spaced-repetition-works/'.

## Installation

1. Install an IDE (I have Visual Studio Code from 'https://code.visualstudio.com/').
2. Install Python (from 'https://www.python.org/downloads/').
3. Install Postgresql (from 'https://www.postgresql.org/download/').
4. Set up a virtual environment and install Django within it (according to the instructions on 'https://docs.djangoproject.com/en/4.2/howto/windows/').
5. Set the python interpreter to the 'python.exe' file within the Scripts folder.
6. Fork this repository inside the virtual environment.
7. Sep up the database connection (according to the instructions on 'https://medium.com/@rudipy/how-to-connecting-postgresql-with-a-django-application-f479dc949a11').

        i. Make sure to hide your password in an '.env' file (according to the instructions on: 'https://pypi.org/project/python-dotenv/').
9. Run the following inside the terminal:*
   ```cmd
    ..\Scripts\activate.bat
   ```
   ```python
    py manage.py runserver
   ```
*You have to do this step everytime you open the project.

## Support

These instructions are specific to Windows, for Unix OS you can try to find similar instructions elsewhere online or open an issue and I'll try to help.

## Contributing

For any changes, please open an issue first to discuss what you would like to add or change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
