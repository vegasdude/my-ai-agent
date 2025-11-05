import openai
import os

# Use your GitHub Actions secret
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": "Hello from GitHub Actions!"}]
    )
    print(response.choices[0].message["content"])

if __name__ == "__main__":
    main()