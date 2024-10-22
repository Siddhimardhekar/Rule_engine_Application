// script.js

async function createRule() {
    const ruleString = document.getElementById('ruleString').value;
    const response = await fetch('/create_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rule_string: ruleString })
    });
    const data = await response.json();
    alert(JSON.stringify(data));
}

async function combineRules() {
    const rules = document.getElementById('rules').value.split('\n');
    const response = await fetch('/combine_rules', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rules })
    });
    const data = await response.json();
    displayCombinedAST(data);
}

function displayCombinedAST(data) {
    const resultDiv = document.getElementById('result');
    if (data.combined_ast) {
        resultDiv.innerHTML = `<h3>Combined AST:</h3><pre>${JSON.stringify(data.combined_ast, null, 2)}</pre>`;
    } else {
        resultDiv.innerHTML = `<h3>Error:</h3><pre>${JSON.stringify(data)}</pre>`;
    }
}

async function evaluateRule() {
    const ruleId = document.getElementById('ruleId').value;
    const data = JSON.parse(document.getElementById('data').value);
    const response = await fetch('/evaluate_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rule_id: ruleId, data })
    });
    const result = await response.json();
    alert(JSON.stringify(result));
}