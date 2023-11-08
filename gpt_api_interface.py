import openai
import os

# Ensure your OPENAI_API_KEY is set as an environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

def call_gpt(prompt, model='gpt-3.5-turbo', temperature=0.5, max_tokens=100):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    while True:
        prompt = input("Enter your prompt (or 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        response = call_gpt(prompt)
        print(f"GPT-3.5-turbo Response: {response}\n")

if __name__ == "__main__":
    main()
