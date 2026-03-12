import os
import sys
import requests
from dotenv import load_dotenv

def main():

    load_dotenv()
    
    # Read the secret from the environment variable
    TREASURE_KEY = os.environ.get("TREASURE_KEY")
    REPO_URL = "https://raw.githubusercontent.com/iyad-obeid/secret-message/main/treasure.txt"

    if TREASURE_KEY is None:
        print("TREASURE_KEY NOT FOUND!")
        sys.exit(1)

    headers = {
        "Authorization": f"token {TREASURE_KEY}",
        "Accept": "application/vnd.github.v3.raw",
    }

    try:
        response = requests.get(REPO_URL, headers=headers)
        response.raise_for_status()  
        treasure_content = response.text
        print(treasure_content)

    except Exception as e:
        print(f"Incorrect Token or HTTP Error: {e}")

if __name__ == "__main__":
    main()