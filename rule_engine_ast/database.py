import sqlite3

def init_db():
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    # Create tables as needed
    c.execute('''CREATE TABLE IF NOT EXISTS rules
                 (id INTEGER PRIMARY KEY, rule_string TEXT)''')
    conn.commit()
    conn.close()

def add_rule(rule_string):
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute("INSERT INTO rules (rule_string) VALUES (?)", (rule_string,))
    conn.commit()
    conn.close()

def get_rule(rule_id):
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute("SELECT rule_string FROM rules WHERE id=?", (rule_id,))
    rule = c.fetchone()
    conn.close()
    return rule[0] if rule else None