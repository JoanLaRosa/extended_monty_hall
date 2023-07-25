import random

WINNING_CHOICES = 1  # W
DOORS_OPENED = 1  # D
NUMBER_OF_CHOICES = 3  # N
NUMBER_OF_RUNS = 100_000  # for the simualtion


def scenario():
    loosing_choices = NUMBER_OF_CHOICES - WINNING_CHOICES
    assert -1 < WINNING_CHOICES <= NUMBER_OF_CHOICES
    assert -1 < DOORS_OPENED < loosing_choices

    choices = [1] * WINNING_CHOICES + [0] * (loosing_choices)

    # Scenario A: The plyer does not switch their choice
    selection = random.randint(0, NUMBER_OF_CHOICES - 1)
    result_A = choices[selection]

    # Scenario B: The player switches their choice [ 1,1,1,1,0,0,0,0,0]
    choices.pop(selection)  # remove the original choice
    choices = choices[: len(choices) - DOORS_OPENED]  # remove the loosing choices
    result_B = choices[random.randint(0, len(choices) - 1)]

    return result_A, result_B


def gather_statistics():
    result_A = 0
    result_B = 0
    for _ in range(NUMBER_OF_RUNS):
        A, B = scenario()
        result_A += A
        result_B += B

    print(
        f"Scenario A: {100 * result_A / NUMBER_OF_RUNS}% wins out of {NUMBER_OF_RUNS} runs"
    )
    print(
        f"Scenario B: {100 * result_B / NUMBER_OF_RUNS}% wins out of {NUMBER_OF_RUNS} runs"
    )


def calculate_expected():
    scenario_A = WINNING_CHOICES / NUMBER_OF_CHOICES
    scenario_B = (WINNING_CHOICES * (NUMBER_OF_CHOICES - 1)) / (
        NUMBER_OF_CHOICES * (NUMBER_OF_CHOICES - DOORS_OPENED - 1)
    )
    print(f"Scenario A: {100 * scenario_A}%")
    print(f"Scenario B: {100 * scenario_B}%")


if __name__ == "__main__":
    print("Expected from calculation:")
    calculate_expected()

    print("Gathered from simulation:")
    gather_statistics()
