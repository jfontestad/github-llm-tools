import openai
import requests
from urllib import parse
import os
import dotenv
import json

dotenv.load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
username = os.environ.get("GITHUB_USER")
password = os.environ.get("GITHUB_PASSWORD")
org = 'Significant-Gravitas'
repo = 'Auto-GPT'
branch = 'master'
branch = branch.replace('/', '_')

def load_commit_summaries(filename):
    with open(filename, "r") as file:
        return file.read()

def generate_summary(content):
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    messages = [
        {"role": "system", "content": "Your goal is to write a detailed blog post of the most recent changes to the Github Repository."},
        {"role": "user", "content": f"Your goal is to make a summary blog post about the following commit changes: {content}. Organize the blogpost structure in sections like Features, CI/CD, Testing, and so on. Remember to make an intro and conclusion for the readers including the time and contributors."}
    ]


    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=3000
        )
        return response.choices[0].message['content']
    except openai.InvalidRequestError as e:
        print(f"Failed to generate summary: {e}")
        return None

def main():
    commit_summaries = load_commit_summaries(f"commit_summaries_{org}_{repo}_{branch}.md")
    summary = generate_summary(commit_summaries)
    with open(f'commit_newsletter_{org}_{repo}_{branch}.md', 'w') as f:
        f.write(summary)
        
if __name__ == "__main__":
    main()
