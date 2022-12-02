import os
import requests

def read_input(day, test=False):
    folder = "inputs"

    if not os.path.exists(folder):
        os.mkdir(folder)

    if test:
        # Use test input
        path = f"{folder}/day{day}_test.txt"

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as fp:
                input_text = [line.strip() for line in fp.readlines()]

        else:
            raise Exception(f"No test data exists (yet) for day {day}. Exiting...")

    else:
        # Use real input
        with open(f"{folder}/day{day}.txt", "r", encoding="utf-8") as fp:
            input_text = [line.strip() for line in fp.readlines()]

    return input_text

def download_input(day):
    # Download input from adventofcode
    url = f"https://adventofcode.com/2022/day/{day}/input"

    # Get session ID and attach it as a cookie to the request
    with open("secret.txt", "r", encoding="utf-8") as fp:
        session_id = fp.readline().strip()

    input_text = requests.get(url, cookies={"session": session_id}).text

    # Write input text to file
    with open(f"inputs/day{day}.txt", "w", encoding="utf-8") as fp:
        fp.write(input_text)
