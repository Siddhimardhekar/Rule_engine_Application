from ast_node import Node

def create_rule(rule_string):
    print(f"Creating rule from string: {rule_string}")  # Debugging output
    if "=" in rule_string:
        left, right = rule_string.split("=")
        left = left.strip()  # Remove whitespace
        right = right.strip().strip("'")  # Remove quotes
        return Node(type="comparison", left=left, right=right)
    else:
        print(f"Failed to parse rule: {rule_string}")  # Debugging output
        return None  # Return None if parsing fails


def combine_rules(rules):
    if not rules or not isinstance(rules, list) or len(rules) == 0:
        return None  # Handle empty or invalid input

    nodes = []
    for rule in rules:
        ast_node = create_rule(rule)  # Create a Node from the rule string
        if isinstance(ast_node, Node):
            nodes.append(ast_node)
        else:
            print(f"Failed to create Node from rule: {rule}")  # Debugging output
            return None  # Return None if any rule fails to create a Node

    # Combine nodes into a single Node using an AND operator
    if len(nodes) == 1:
        return nodes[0]  # Return the single node if only one exists
    elif len(nodes) > 1:
        combined_node = Node(type="operator", left=nodes[0], right=nodes[1])
        for node in nodes[2:]:  # Combine remaining nodes
            combined_node = Node(type="operator", left=combined_node, right=node)
        return combined_node

    return None 
def evaluate_rule(rule_id, user_data):
    # Logic to evaluate the rule against user_data
    # For demonstration, let's return a dummy result
    return {"result": True}  # Dummy result
