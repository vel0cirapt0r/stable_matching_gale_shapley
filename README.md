# Stable Matching with Gale-Shapley Algorithm

This Python script implements the Gale-Shapley algorithm to find stable matchings between hospitals and students based on their preferences. It allows for the generation of multiple stable matchings and provides a way to validate each matching for stability.

## Contents

- [Introduction](#introduction)
- [Functions](#functions)
  - [Gale-Shapley Algorithm](#gale-shapley-algorithm)
  - [is_stable_matching Function](#is_stable_matching-function)
  - [find_all_stable_matchings Function](#find_all_stable_matchings-function)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Introduction

The Gale-Shapley algorithm is a well-known algorithm for solving the stable marriage problem and has applications in matching scenarios where preferences of two sides need to be satisfied without conflicts. In this implementation, hospitals propose to students based on their preference lists, and stable matchings are found iteratively.

## Functions

### Gale-Shapley Algorithm

The `gale_shapley(hospital_pref, student_pref)` function implements the Gale-Shapley algorithm:

```python
def gale_shapley(hospital_pref, student_pref):
    """
    Implements the Gale-Shapley algorithm to find a stable matching between hospitals and students.

    Args:
    - hospital_pref (dict): Dictionary where keys are hospital identifiers and values are lists of student identifiers
      representing the hospital's preference order.
    - student_pref (dict): Dictionary where keys are student identifiers and values are lists of hospital identifiers
      representing the student's preference order.

    Returns:
    - hospital_to_student (dict): Dictionary where keys are hospital identifiers and values are student identifiers
      representing the stable matching found.
    """
    # Implementation details...
```

### `is_stable_matching` Function

The `is_stable_matching(hospital_to_student, student_pref, hospital_pref)` function checks if a given matching is stable:

```python
def is_stable_matching(hospital_to_student, student_pref, hospital_pref):
    """
    Checks if a given matching between hospitals and students is stable.

    Args:
    - hospital_to_student (dict): Dictionary where keys are hospital identifiers and values are student identifiers
      representing the matching to be checked.
    - student_pref (dict): Dictionary where keys are student identifiers and values are lists of hospital identifiers
      representing the student's preference order.
    - hospital_pref (dict): Dictionary where keys are hospital identifiers and values are lists of student identifiers
      representing the hospital's preference order.

    Returns:
    - bool: True if the matching is stable, False otherwise.
    """
    # Implementation details...
```

### `find_all_stable_matchings` Function

The `find_all_stable_matchings(hospital_pref, student_pref)` function generates all possible stable matchings:

```python
def find_all_stable_matchings(hospital_pref, student_pref):
    """
    Finds all possible stable matchings between hospitals and students.

    Args:
    - hospital_pref (dict): Dictionary where keys are hospital identifiers and values are lists of student identifiers
      representing the hospital's preference order.
    - student_pref (dict): Dictionary where keys are student identifiers and values are lists of hospital identifiers
      representing the student's preference order.

    Returns:
    - list: A list of dictionaries, each dictionary representing a stable matching found.
    """
    # Implementation details...
```

## Usage

To use the script, ensure you have Python installed on your machine (version 3.x recommended). Follow these steps:

1. Clone the repository or download the `main.py` file.
2. Modify the `hospital_preferences` and `student_preferences` dictionaries in `main.py` to reflect your matching scenario.
3. Run the script using Python:

   ```bash
   python main.py
   ```

4. The script will output all stable matchings found based on the preferences provided.

## Example

Here's an example configuration of hospital and student preferences:

```python
hospital_preferences = {
    'H1': ['S1', 'S2', 'S3', 'S4'],
    'H2': ['S2', 'S1', 'S3', 'S4'],
    'H3': ['S3', 'S2', 'S1', 'S4'],
    'H4': ['S4', 'S2', 'S3', 'S1']
}

student_preferences = {
    'S1': ['H2', 'H1', 'H3', 'H4'],
    'S2': ['H1', 'H2', 'H3', 'H4'],
    'S3': ['H3', 'H2', 'H1', 'H4'],
    'S4': ['H4', 'H2', 'H3', 'H1']
}

all_stable_matchings = find_all_stable_matchings(hospital_preferences, student_preferences)

# Output all stable matchings found
for idx, matching in enumerate(all_stable_matchings):
    print(f"Matching {idx + 1}:")
    for hospital, student in matching.items():
        print(f"{hospital} is matched with {student}")
    print()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
