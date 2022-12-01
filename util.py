import os
import requests

def read_input(day):
    path = f"inputs/day{day}.txt"

    if not os.path.exists(path):
        # Download input from adventofcode
        url = f"https://adventofcode.com/2022/day/{day}/input"

        # Get session ID and attach it as a cookie to the request
        with open("secret.txt", "r", encoding="utf-8") as fp:
            session_id = fp.readline().strip()

        input_text = requests.get(url, cookies={"session": session_id}).text

        # Write input text to file
        with open(path, "w", encoding="utf-8") as fp:
            fp.write(input_text)

        input_text = [line.strip() for line in input_text.split("\n")]

    else:
        # Load already downloaded input text from file
        with open(path, "r", encoding="utf-8") as fp:
            input_text = [line.strip() for line in fp.readlines()]

    return input_text
