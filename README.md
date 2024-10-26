Prerequisites
Python (version 3.8 or higher)
Virtual Environment for Python
Visual Studio Code (VSCode) - optional, recommended for Python and Flask development
Setup Instructions
1. Clone the Repository
To get started, clone this repository: 

bash
Copy code
git clone <repository-url>
cd <repository-name>
2. Set Up a Virtual Environment
Inside the backend folder, create a virtual environment:

bash
Copy code
cd backend
python -m venv venv
3. Activate the Virtual Environment
Windows:

bash
Copy code
.\venv\Scripts\activate
MacOS/Linux:

bash
Copy code
source venv/bin/activate
4. Install Required Packages
Install the dependencies listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
5. Select Python Interpreter in VSCode (Optional)
To ensure VSCode uses the virtual environment’s Python interpreter:

Open VSCode and navigate to the backend folder.
Go to View > Command Palette and type Python: Select Interpreter.
Choose venv\Scripts\python.exe from the list.
6. Set Up the SQLite Database
The application uses SQLite for storing rules. The database will be automatically initialized when running main.py.

7. Run the Backend Server
To start the backend server:

bash
Copy code
python main.py
The Flask server will run on http://127.0.0.1:5000 by default. You should see a message indicating that the server is running in debug mode.

8. Access the Frontend
Open the index.html file in a web browser to use the frontend interface. This HTML file provides a UI to create, combine, evaluate, and modify rules through the backend server’s API.

Usage
Create Rule: Enter a rule string (e.g., age > 25) in the frontend and click Create Rule.
Combine Rules: Provide the IDs of rules to combine, separated by commas (e.g., 1,2,3), and click Combine Rules.
Evaluate Rule: Provide the rule ID and data in JSON format (e.g., { "age": 30, "income": 50000 }) and click Evaluate Rule.
Modify Rule: Enter a rule ID and a new rule string to modify an existing rule.
Testing
Unit tests are provided in test.py. To run the tests:

Make sure the virtual environment is activated.
Run the tests using the following command:
bash
Copy code
python -m unittest test.py
Project Configuration
Configuration Options
Database: The database is configured to use SQLite with rules.db as the filename. This can be modified in main.py if needed.
Logging: Logging is set to DEBUG level to capture detailed logs. This can be adjusted by modifying logging.basicConfig(level=logging.DEBUG) in main.py.
API Endpoints
POST /create_rule: Creates a new rule.
POST /combine_rules: Combines multiple rules using AND logic.
POST /evaluate_rule: Evaluates a rule with provided data.
POST /modify_rule: Modifies an existing rule.
Troubleshooting
If the virtual environment fails to activate, ensure you are in the correct directory and that Python is installed.
If the frontend fails to communicate with the backend, verify that the backend server is running at http://127.0.0.1:5000.