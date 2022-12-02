SYMBOL_VALUES = {
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3 # Scissors
}

TRANSLATE_SYMBOL = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

SCORE_WIN = 6
SCORE_DRAW = 3

def part_1(input_text):
    total_score = 0

    for line in input_text:
        sym_1, sym_2 = line.split(" ")

        if TRANSLATE_SYMBOL[sym_1] == sym_2: # Draw
            total_score += SCORE_DRAW + SYMBOL_VALUES[sym_2]

        elif sym_1 == "A" and sym_2 == "Y":
            total_score += SCORE_WIN + SYMBOL_VALUES[sym_2]

        elif sym_1 == "B" and sym_2 == "Z":
            total_score += SCORE_WIN + SYMBOL_VALUES[sym_2]

        elif sym_1 == "C" and sym_2 == "X":
            total_score += SCORE_WIN + SYMBOL_VALUES[sym_2]

        else: # Loss
            total_score += SYMBOL_VALUES[sym_2]

    print(total_score)

def part_2(input_text):
    total_score = 0

    for line in input_text:
        sym_1, sym_2 = line.split(" ")

        if sym_2 == "Y": # Draw
            total_score += SCORE_DRAW + SYMBOL_VALUES[TRANSLATE_SYMBOL[sym_1]]

        elif sym_2 == "X": # Loss
            if sym_1 == "A":
                total_score += SYMBOL_VALUES["Z"]
            elif sym_1 == "B":
                total_score += SYMBOL_VALUES["X"]
            else:
                total_score += SYMBOL_VALUES["Y"]

        elif sym_2 == "Z": # Win
            if sym_1 == "A":
                total_score += SCORE_WIN + SYMBOL_VALUES["Y"]
            elif sym_1 == "B":
                total_score += SCORE_WIN + SYMBOL_VALUES["Z"]
            else:
                total_score += SCORE_WIN + SYMBOL_VALUES["X"]

    print(total_score)
