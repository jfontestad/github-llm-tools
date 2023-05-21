
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

limit = 5  # Specify the number of commits to fetch
encoded_branch = parse.quote(branch)
API_URL = f"https://api.github.com/repos/{org}/{repo}/commits?sha={encoded_branch}&per_page={limit}"
print(API_URL)


def get_recent_commits(api_url, username, password):
    """Fetch the recent commits from the GitHub API."""
    response = requests.get(api_url, auth=(username, password))
    response.raise_for_status()  # Raise an exception if the request failed
    return response.json()


def get_commit_diff(commit_url, username, password):
    """Fetch the diff of a commit from the GitHub API."""
    response = requests.get(commit_url, auth=(username, password))
    response.raise_for_status()  # Raise an exception if the request failed
    return response.json()["files"]


def generate_commit_summary(commit_data):
    """Generate a descriptive summary for a commit using the OpenAI API."""
    message = commit_data["commit"]["message"]
    author = commit_data["commit"]["author"]["name"]
    date = commit_data["commit"]["author"]["date"]
    diff = get_commit_diff(commit_data["url"], username, password)

    # Define the conversation messages
    messages = [
        {"role": "system", "content": "You are a Senior Python Developer that reviews PRs and posts brief .md ."},
        {"role": "user",
         "content": f"On {date}, {author} made a commit with the following message: {message}. The diff for this commit is: {diff}. Can you summarize this commit?"}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        return response.choices[0].message['content']
    except openai.InvalidRequestError as e:
        print(f"Failed to generate summary for commit {commit_data['sha']}: {e}")
        return None


def main():
    # Fetch the recent commits
    commits = get_recent_commits(API_URL, username, password)

    # Open the markdown file in append mode
    safe_branch = branch.replace('/', '_')
    with open(f'commit_summaries_{org}_{repo}_{safe_branch}.md', 'a') as f:
        # Generate and write a summary for each commit
        for commit in commits:
            summary = generate_commit_summary(commit)
            if summary is not None:  # Only write summaries that were successfully generated
                f.write(summary)
                f.write("\n---\n")


if __name__ == "__main__":
    main()
