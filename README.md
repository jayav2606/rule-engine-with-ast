# Rule Engine with AST

A Flask-based rule engine that parses, evaluates, and modifies conditional rules using Abstract Syntax Trees (AST). This project allows users to create, combine, evaluate, and modify rules that can be used to make dynamic data-driven decisions. The engine uses SQLAlchemy for rule storage in an SQLite database, and Flask-CORS is enabled for cross-origin resource sharing.

---

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)


---

## Features
- **Create Rules:** Define rules with conditions using logical operators like `AND`, `OR`.
- **Combine Rules:** Combine multiple rules into a single rule with logical connectors.
- **Evaluate Rules:** Evaluate rules against incoming data to get boolean results.
- **Modify Rules:** Update existing rules to adjust to changing requirements.
- **Store Rules:** Store rules and their AST representations in an SQLite database.

## Tech Stack
- **Backend:** Flask
- **Database:** SQLAlchemy with SQLite
- **Other Libraries:** Flask-CORS, Logging, JSON

---

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/rule-engine-ast.git
   cd rule-engine-ast

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. **Install dependencies**
   ```bash
    pip install -r requirements.txt

4. **Run the application**
   ```bash
    python main.py

## Usage
### Running the Server
1. **Start the Flask server by running:**
   ```bash
    python main.py
### The server will be available at http://127.0.0.1:5000.

##API Endpoints
1. **Create Rule**
   - Endpoint: POST /create_rule
   - Description: Create a new rule and store its AST representation.
   - Payload Example:
   ```json
       {
          "rule_string": "(age > 25 AND income > 50000)"
       }
2. **Combine Rules**
   - Endpoint: POST /combine_rules
   - Description: Combine existing rules using AND or OR operators.
   - Payload Example:
   ```json
       {
          "rule_ids": [1, 2]
       }
   
3. **Evaluate Rule**
   - Endpoint: POST /evaluate_rule
   - Description: Evaluate a rule with the provided data.
   - Payload Example:
   ```json
       {
          "rule_id": 1,
          "data": {"age": 30, "income": 60000}
       }

4. **Modify Rule**
   - Endpoint: POST /modify_rule
   - Description: Modify an existing rule by updating its condition.
   - Payload Example:
   ```json
       {
          "rule_id": 1,
           "new_rule_string": "age > 30"
       }
## Testing
### Unit tests are included to verify the rule creation, combination, evaluation, and modification functionalities.
1. **Run the tests**
   ```bash
    python -m unittest test.py
2. **Test Coverage**
   - test_create_rule: Validates rule creation with different conditions.
   - test_combine_rules: Verifies correct functionality of rule combination.
   - test_evaluate_rule: Checks the evaluation results for different datasets.
   - test_modify_rule: Ensures that rule modification works as expected.
   - test_error_handling: Tests error handling for non-existent rules.
  


























