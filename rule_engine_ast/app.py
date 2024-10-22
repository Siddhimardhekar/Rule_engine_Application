from flask import Flask, request, jsonify
from rule_parser import create_rule, combine_rules, evaluate_rule
from database import init_db

app = Flask(__name__)

# Initialize the database (if needed)
init_db()

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.get_json()
    rule_string = data.get('rule_string')
    ast_node = create_rule(rule_string)
    return jsonify(ast_node)

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.get_json()
    rules = data.get('rules')
    combined_ast = combine_rules(rules)
    return jsonify({"combined_ast": combined_ast})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.get_json()
    rule_id = data.get('rule_id')
    user_data = data.get('data')
    result = evaluate_rule(rule_id, user_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)