# Python Password Analyzer

## PROJECT DESCRIPTION
I completed my project using the fundamentals of Python. This is my first project coded in Python to show the beginning skills that I acquired from my Python Fundamentals course with Nucamp. The Python Password Analyzer begins with the requesting a user to register their name. Once their name is registered, the Analyzer requests that the user creates a password. The user will go through a loop before creating a successful password. The loop does force the user to create a passwor that not only includes lower and upper-cased alphabet, but also numbers and special characters. 

I chose this project because I have a heavy interest in the cybersecurity side software engineering, and I wanted this project to emulate a secure way for users to create passwords that can not be infiltrated or obtained from cyber attacks. This project is the beginning of an extensive journey to learn how Python can mitigate potential cyber threats.

## FEATURES
- Input function requests for user to create a username and password
- For loops to loop through the data to check if password includes requirements
- If statements to check if password matches the requirements and provides a print statement indicating what is missing
- Data structures using tuples to hold alphabet, numbers, and special characters
- While loop to loop through the entire password process until a password is successfully created
- String module to shorten adding the alphabet (upper and lower case) and numbers data 

## INSTALLATION INSTRUCTIONS
I installed the following in the project:
- Download Python 3.11.2 
- Install VS Code Python Extension Intellisense (if using VS Code)
- python -m pip install --upgrade pip
- pip install pylint
- pip install pep8
- pip install --upgrade autopep8

- Update VS Code Settings
- Use Ctrl/Cmd+ to open settings
- Click file icon
- in settings.json add the following below into the curly braces at the bottom:
"editor.formatOnSave": true,
"python.linting.enabled": true,
"python.linting.pylintEnabled": true,
"python.linting.pylintArgs": ["--errors-only"]

## USAGE INSTRUCTIONS
- To run this code, you will need to open the VS Code terminal by typing Ctrl + `. Once the terminal is opened, type python + the corresponding name of the file where the code exists. In this project, the file name is app.py.

- Therefore, the user will need to type python + app.py + ENTER.

