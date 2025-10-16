import ast

def analyze_code(code):
    issues = []
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and len(node.body) > 30:
                issues.append({
                    "line": node.lineno,
                    "type": "complexity_warning",
                    "message": f"Function '{node.name}' exceeds 30 lines."
                })
    except SyntaxError as e:
        issues.append({"line": e.lineno, "type": "syntax_error", "message": str(e)})
    return issues
