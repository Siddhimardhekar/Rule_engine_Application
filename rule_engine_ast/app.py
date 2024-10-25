from flask import Flask, request, jsonify
from rule_parser import create_rule, combine_rules, evaluate_rule
from database import init_db
from models.node import Node  # Import the Node class
from ast_node import Node
import traceback  # Make sure this line is present at the top of your app.py


app = Flask(__name__)  # Use __name__ instead of name

# Initialize the database (if needed)
init_db()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.get_json()
    rule_string = data.get('rule_string')

    if not rule_string:
        return jsonify({"error": "Missing rule_string"}), 400

    ast_node = create_rule(rule_string)

    # Ensure ast_node is a Node and convert it to dict
    if isinstance(ast_node, Node):
        return jsonify(ast_node.to_dict())  # Convert to dict if it's a Node
    else:
        return jsonify({"error": "Failed to create AST from rule string"}), 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    try:
        data = request.get_json()
        rules = data.get('rules')

        if not rules or not isinstance(rules, list):
            return jsonify({"error": "Missing or invalid rules"}), 400

        combined_ast = combine_rules(rules)

        if combined_ast is None:
            return jsonify({"error": "No valid nodes were created from the rules."}), 400

        # Use the to_dict method to convert to a serializable format
        combined_ast_dict = combined_ast.to_dict() if isinstance(combined_ast, Node) else combined_ast

        return jsonify({"combined_ast": combined_ast_dict})

    except Exception as e:
        # Log the full traceback for debugging
        traceback.print_exc()
        return jsonify({"error": "An unexpected error occurred."}), 500
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.get_json()
    rule_id = data.get('rule_id')
    user_data = data.get('data')

    if not rule_id or user_data is None:
        return jsonify({"error": "Missing rule_id or data"}), 400

    result = evaluate_rule(rule_id, user_data)

    # Ensure the result is JSON serializable
    if isinstance(result, dict) or isinstance(result, list):
        return jsonify(result)
    else:
        return jsonify({"error": "Evaluation result is not serializable"}), 500

if __name__ == '__main__':
    app.run(debug=True)
