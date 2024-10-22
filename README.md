# Rule_engine_Application
This is a simple rule engine application that allows you to create, combine, and evaluate rules.

Features
Create Rules: Define rules using a simple JSON format.
Combine Rules: Combine multiple rules using logical operators (AND, OR, NOT).
Evaluate Rules: Evaluate rules against a given data set.
How to use
Create a rule: Enter a rule in the "Create Rule" section.
Combine rules: Enter your rules for combining in the "Combine Rules" section.
Evaluate a rule: Enter the rule ID and data set in the "Evaluate Rule" section.
Example
Create Rule:

json

Verify

Open In Editor
Edit
Copy code
{ "rule_string": "age > 30 AND department = 'Sales'" }
Combine Rules:

json

Verify

Open In Editor
Edit
Copy code
{
  "salary > 50000",
  "age > 30"
}
Evaluate Rule:

json

Verify

Open In Editor
Edit
Copy code
{
  "rule_id": 1,
  "data": {
    "age": 35,
    "department": "Sales",
    "salary": 60000
  }
}
Dependencies
JavaScript
Node.js
Installation
Clone this repository.
Install the dependencies: npm install
Usage
Run the application: node index.js
Open your browser and visit http://localhost:3000.
Development
Make your changes to the code.
Run the application: node index.js
Open your browser and visit http://localhost:3000.
Contribution
Contributions are welcome! Please feel free to submit pull requests or open issues.
