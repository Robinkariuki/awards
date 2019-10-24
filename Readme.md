### By Robin kariuki

### Description
This is an application that allows users to upload their personal projects which they have been working on. These projects can then be rated by the other users. The other users can also sign up and post their own personal projects too.

### BDD Specifications Table
|        User Requirements                 |           Input                           |           Output                         |
|------------------------------------------|-------------------------------------------|------------------------------------------|
| Sign Up/Login                            | To create a new account, click on the sign| If login is successful, the user is      |
|                                          | up link and fill in the form details. To  | redirected to the home page              |
|                                          | login, fill in the details                |                                          |
| Add a new project                        | Click on the submit new project tab on the| You will be navigated to a page which    |
|                                          | navbar and submit the project details     | has a form to submit the project         |
| Review a project                         | Click on the Review button                | You will be navigated to a page where you|
|                                          |                                           | can post your review                     |
| Create a profile                         | Click on the profile tab then Edit Profile| A new profile for the user will be       |
|                                          | button                                    | created                                  |
| Search for a project                     | Enter the project's name into the search  | You will be redirected to a page with all||                                          | bar in the navbar                         | results matching your search. You can    |
|                                          |                                           | then click on the project you want       |
| Log out                                  | Click on the Account button and select    | You will be logged out                   ||                                          | log out                                   |                                          |


### Setup/Installation Requirements
- Ensure you have Python3.6 installed.
- Clone the Awards directory.
- Create your own virtual environment and activate it using these respective commands `python3.6 -m venv --without-pip virtual` and  `source virtual/bin/activate`
- Install all the necessary dependencies necessary for running the application using this command `pip install -r requirements.txt`
- Open the terminal and run this command `psql` You can then create a database by running this command
`CREATE DATABASE awards`
- Run migrations using these respective commmands `python3.6 manage.py makemigrations projects` then `python3.6 manage.py migrate`
- Run the app using this command `python3.6 manage.py runserver` on the terminal.You can then open the app on your browser.


### Technologies Used
<ul>
<li>Python 3.6</li>
<li>Django</li>
<li>Bootstrap</li>
<li>HTML</li>
</ul>

### Support and Contact Details
For more information, questions, or feedback, get in touch with me on my email:
robinkariuki123@gmail.com

## Licence
 
 [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
 
 
 Copyright (c) 2019 RobinKariuki