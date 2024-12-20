# devLMS
Project Assignment for DevNext
### First Clone this project from github\
## How to Setup this.
# DevLMS - Django Project

## Setup Instructions

Follow these steps to set up and run the **DevLMS** Django project locally.

### 1. Clone the Repository

Clone the repository to your local machine using Git. Open **PowerShell** or your terminal and navigate to the directory where you want to store the project. Then, run:


### 2. Open PowerShell or Terminal in the Current Directory

If you're using **PowerShell** on Windows:

- Open **PowerShell** in the directory where the repository is cloned. 
- Navigate to the folder where you cloned the project (or right-click the folder and select "Open PowerShell window here").

For **macOS** or **Linux**, open your terminal and navigate to the project directory where the repository was cloned.

### 3. Set Up a Virtual Environment (Optional but Recommended)

It is highly recommended to create and use a virtual environment to isolate the project dependencies.

- **On macOS/Linux**:


  python3 -m venv venv
  source venv/bin/activate


- **On Windows**:

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

> This will create a `venv` folder where all the dependencies will be installed.

### 4. Install Project Dependencies

With the virtual environment activated, install all necessary dependencies from the `requirements.txt` file using `pip`:


pip install -r requirements.txt


This command installs all the packages specified in `requirements.txt`.




### 6. Apply Database Migrations

Run the following command to set up the database schema (it creates tables and prepares the database for the project):


python manage.py migrate


### 9. Run the Development Server

Now you are ready to run the Django development server:


python manage.py runserver


By default, the server will run at `http://127.0.0.1:8000/`. Open this URL in your browser to see the project running locally.





### Note - Background Async Task using Celery
run celery worker with 

celery -A devlms worker --pool=solo
#use above command with separte powershell with same location as project  to run async task. 

and first give the user write permission on the reports folder because of celery unless you got permission error

for backend browker we used sqlite with sqlalchemy

# For API Documention -DRF YASg and Swagger
Steps:
Run the [project using ]
Python manage.py runserver
then open the browser and put this url there:
http://localhost:8000/swagger/


# I have added 2 unit Test as well for twoo appi Endpoint
/authors/ - list or author 
/books/ - list of all books

you can find this code at

devlms/book/tests.py
devlms/author/tests.py

#And for run the unit test you needd  ot use this

python manage.py test