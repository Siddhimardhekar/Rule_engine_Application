async function createRule() {
    const ruleString = document.getElementById('createRuleInput').value;
    try {
        const response = await fetch('/create_rule', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ rule_string: ruleString })
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        displayCreateRuleResult(data);
    } catch (error) {
        displayCreateRuleResult({ error: error.message });
    }
}

async function combineRules() {
    const rules = document.getElementById('combineRulesInput').value.trim();
    try {
        const response = await fetch('/combine_rules', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ rules: JSON.parse(rules) })
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        displayCombineRulesResult(data);
    } catch (error) {
        displayCombineRulesResult({ error: error.message });
    }
}

async function evaluateRule() {
    const ruleId = document.getElementById('ruleId').value;
    const data = document.getElementById('evaluateRuleInput').value.trim();
    try {
        const response = await fetch('/evaluate_rule', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ rule_id: ruleId, data: JSON.parse(data) })
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const result = await response.json();
        displayEvaluateRuleResult(result);
    } catch (error) {
        displayEvaluateRuleResult({ error: error.message });
    }
}
