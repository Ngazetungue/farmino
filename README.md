
# The system has the ability to
* Ability to login as an admin and login as a new user member
* Ability to register new users
* Ability to allow the Farmer can register their livestock into the system
* Ability to log out
* Ability to calculate the cost of each livestock
* Ability to do some logic operation
* Implementation of pagination for all the list views across the application.
* Ability to calculate the Bill of the farmer 
* Ability to calculate farmer discount if they register more than five livestocks
#Prerequisites
* Use requirements.txt file to install all required packages
* Any Editor (Preferably VS Code or Sublime Text)
* Any web browser with latest version
# Languages and Technologies used
* HTML5/CSS3
* Bootstrap (An HTML, CSS, and JS library)
* Django, Python
* Sqlite
# Steps to run the project in your machine
* python -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py runserver

# GETTING INTO THE PROJECT:
* Livestock registration systems in Python and Django This system has a ‘Login’ page from where the administrator can login into their accounts . Fig 1.1 shows the ‘Login’ page of our project.
 <img width="446" alt="Screenshot 2022-10-14 at 2 32 50 PM" src="https://user-images.githubusercontent.com/10814039/195865131-889631e5-57f3-4bee-9f1d-a1e33ac58c00.png">

* This system has a ‘Signup’ page from which the user can register into the system 
. Fig 1.2 shows the ‘Signup’ page of our project.
 <img width="446" alt="Screenshot 2022-10-14 at 2 34 29 PM" src="https://user-images.githubusercontent.com/10814039/195865334-dcbc0b3b-9c77-4062-a55c-a26760cb2cab.png">
 
* This system has a "Register" page from which farmers can register their livestock.  Fig 1.3 shows the "Register livestock’ page of our project.<img width="446" alt="Screenshot 2022-10-14 at 2 33 13 PM" src="https://user-images.githubusercontent.com/10814039/195865557-73779162-5b33-4ee3-a59e-377f775c4511.png">



 
#The ‘Home’ page consists of 2 modules:
1. Farmer list
2. Billing
* Farmer module
This module contains the list of the farmers that register their livestock and also the number of their livestock.
* Billing module
This module contains all the necessary information about the farmer, and this is why the business logic is happening. The discount is given to the farmers once they register more than five livestock; otherwise, they won’t get a discount.

