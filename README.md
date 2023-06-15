# Energy Consumption API
API for collecting and managing energy consumption data from different appliances 

[View Frontend Repo](https://github.com/Andrea-Galindo/energy-calculator/blob/main/README.md)

## Technologies Used
- Flask
- SQLAlchemy
- Postgres

## Installation

1. Fork the repository
2. Clone the forked repository to your local machine: `git clone https://github.com/your-username/energy-consumption-api.git`
3. Navigate to the project directory: `cd energy-consumption-api`
4. Run `python3 -m venv venv` to setup virtual environment
5. Run `source venv/bin/activate` to activate virtual environment
6. Run `pip install -r requirements.txt` to install requirements
7. Create two databases on your local machine:
- A development database named `energy_consumption_development`
- A test database named `energy_consumption_test`
8. Create a file named `.env` on the root directory and add two environment variables that will hold your database URLs: 
  `SQLALCHEMY_DATABASE_URI` to hold the path to your development database
  `SQLALCHEMY_TEST_DATABASE_URI` to hold the path to your development database
  
Your `.env` may look like this:

```
SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/energy_consumption_development
SQLALCHEMY_TEST_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/energy_consumption_test
```
9. Initialize migrations: 
- `$ flask db init` 
- `$ flask db migrate` 
- `$ flask db upgrade`

## API Endpoints
1. Start your flask server: `$ flask run` or `$ FLASK_ENV=development flask run`
1. Make a POST request to /appliances to add a new appliance to the database
1. Make a GET request to /appliances/{appliance_id} to get the info of an appliance
1. Make a PUT request to /appliances/{appliance_id} to edit an apliance
1. Make a DELETE request to /appliances/{appliance_id} to delete an appliance
