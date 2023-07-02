# Global Search Application

The Global Search Application is a Django-based web application that enables users to perform global searches across various data, including cities, countries, and languages. The application's core functionality includes a search bar with autosuggestions and a dashboard to display search results.

## Requirements

Before setting up and running the Global Search Application, make sure you have the following requirements installed on your system:

1. **Python 3.8+**: Install Python by running the following commands in your terminal:
   ```bash
   sudo apt update
   sudo apt-get install python3 python3-pip
   python --version
   ```

2. **Virtualenv**: Create a virtual environment to isolate the application's dependencies. Install Virtualenv using the following command:
   ```bash
   sudo pip3 install virtualenv
   ```
   Then, create a virtual environment and activate it:
   ```bash
   virtualenv --python=python3.8 .venv
   source .venv/bin/activate
   ```
   To deactivate the virtual environment, simply run `deactivate`.

3. **Poetry**: Poetry is a dependency management tool that we'll use to install and manage the project dependencies. Install Poetry by running the following commands:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   poetry --version
   ```

4. **MySQL 15+**: The application requires a MySQL database to store and retrieve data. Install MySQL by following the appropriate instructions for your operating system.

## Installation Instructions

Follow these steps to install and set up the Global Search Application:

1. **Python Dependencies**: Install the Python dependencies for the application by navigating to the project's root directory and running the following command:
   ```bash
   poetry install
   ```

2. **MySQL Setup**: Create a new database and user for the application to use. Launch the MySQL shell by running the following command and entering your MySQL root password when prompted:
   ```bash
   mysql -u root -p
   ```
   Once inside the MySQL shell, execute the following commands to create the necessary database and user:
   ```sql
   CREATE DATABASE world;
   CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';
   ```
   Replace `'your_username'` and `'your_password'` with your desired values.

3. **Environment Configuration**: Copy the `.env.example` file to `.env.development` and add the necessary database configuration, such as `DB_NAME`, in the `.env.development` file.

4. **Database Migration**: Run the following commands in the given order to perform database migration and populate the database with initial data. Please ensure you execute them in the specified order to avoid errors during the application run:
   ```bash
   python manage.py dbshell < global_search/data/dump/world.sql
   python manage.py migrate global_search 0001
   python manage.py migrate global_search 0002 --fake
   python manage.py migrate
   ```

5. **Run the Application**: Start the server and run the Global Search Application using the following command:
   ```bash
   python manage.py runserver
   ```

## Using the Global Search Application

To use the Global Search Application:

1. Open any web browser.

2. Visit the sign-up page by navigating to http://localhost:8000/signup/.

On the sign-up page, users can create an account to access the Global Search Application. Once signed up and logged in, users can use the search bar on the dashboard to perform global searches. The application provides autocomplete suggestions as users type in the search bar, making the search process more
