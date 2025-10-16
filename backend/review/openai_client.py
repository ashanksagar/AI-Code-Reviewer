from openai import OpenAI

client = OpenAI()

def gpt_review(code: str) -> str:
    
    prompt = f"Review the following code and provide clear, concise feedback:\n\n{code}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content

def gpt_chat(message: str) -> str:
    """
    Sends a single message to GPT-4o-mini and returns the model's reply.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"