from analyzer.ast_parser import analyze_code as ast_analyze
from .openai_client import gpt_review

def analyze_code(code: str) -> dict:
    ast_issues = ast_analyze(code)
    
    gpt_feedback = gpt_review(code)
    
    return {
        "ast_issues": ast_issues,
        "gpt_feedback": gpt_feedback
    }
