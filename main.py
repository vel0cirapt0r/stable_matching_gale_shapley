def gale_shapley(hospital_pref, student_pref):
    """
    Gale-Shapley algorithm implementation to find a stable matching between hospitals and students.

    Complexity:
    - Time: O(n^2) where n is the number of hospitals or students (since each hospital might propose to each student).
    - Space: O(n) for storing mappings and preference lists.

    Args:
    - hospital_pref (dict): Dictionary mapping hospitals to their preference lists of students.
    - student_pref (dict): Dictionary mapping students to their preference lists of hospitals.

    Returns:
    - hospital_to_student (dict): Dictionary mapping hospitals to their matched students.
    """
    hospital_to_student = {hospital: None for hospital in hospital_pref}
    student_to_hospital = {}

    local_hospital_pref = {h: prefs[:] for h, prefs in hospital_pref.items()}

    free_hospitals = list(hospital_pref.keys())

    while free_hospitals:
        h = free_hospitals[0]
        if local_hospital_pref[h]:
            s = local_hospital_pref[h].pop(0)
            if s not in student_to_hospital:
                hospital_to_student[h] = s
                student_to_hospital[s] = h
                free_hospitals.pop(0)
            else:
                h_prime = student_to_hospital[s]
                if student_pref[s].index(h) < student_pref[s].index(h_prime):
                    hospital_to_student[h] = s
                    hospital_to_student[h_prime] = None
                    student_to_hospital[s] = h
                    free_hospitals.pop(0)
                    free_hospitals.append(h_prime)
        else:
            free_hospitals.pop(0)

    return hospital_to_student


def is_stable_matching(hospital_to_student, student_pref, hospital_pref):
    """
    Check if a given matching between hospitals and students is stable.

    Complexity:
    - Time: O(n^2) where n is the number of hospitals or students (for checking each pair of preferences).
    - Space: O(n) for storing mappings and preference lists.

    Args:
    - hospital_to_student (dict): Dictionary mapping hospitals to their matched students.
    - student_pref (dict): Dictionary mapping students to their preference lists of hospitals.
    - hospital_pref (dict): Dictionary mapping hospitals to their preference lists of students.

    Returns:
    - bool: True if the matching is stable, False otherwise.
    """
    # Create reverse mapping of hospital_to_student for quick lookup
    student_to_hospital = {s: h for h, s in hospital_to_student.items() if s is not None}

    for h in hospital_pref:
        for s in hospital_pref[h]:
            current_match = hospital_to_student[h]

            if current_match is None:
                break

            if current_match in student_pref[s] and student_pref[s].index(h) < student_pref[s].index(current_match):
                return False

    return True


def find_all_stable_matchings(hospital_pref, student_pref):
    """
    Find all stable matchings between hospitals and students using Gale-Shapley algorithm.

    Complexity:
    - Time: O(n^3) where n is the number of hospitals or students (due to nested loops and checking stability).
    - Space: O(n^2) for storing mappings and preference lists.

    Args:
    - hospital_pref (dict): Dictionary mapping hospitals to their preference lists of students.
    - student_pref (dict): Dictionary mapping students to their preference lists of hospitals.

    Returns:
    - list of dict: List of all stable matchings found, where each matching is a dictionary mapping hospitals to students.
    """
    initial_matching = gale_shapley(hospital_pref, student_pref)
    stable_matchings = [initial_matching]

    hospitals = list(hospital_pref.keys())

    for i in range(len(hospitals)):
        for j in range(i + 1, len(hospitals)):
            h1, h2 = hospitals[i], hospitals[j]
            s1, s2 = initial_matching[h1], initial_matching[h2]

            if s1 and s2 and student_pref[s1].index(h2) < student_pref[s1].index(h1) and student_pref[s2].index(h1) < student_pref[s2].index(h2):
                new_matching = initial_matching.copy()
                new_matching[h1], new_matching[h2] = s2, s1

                if is_stable_matching(new_matching, student_pref, hospital_pref):
                    stable_matchings.append(new_matching)

    return stable_matchings


# Example usage with 4 hospitals and 4 students
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

# Print all stable matchings found
print("All Stable Matchings:")
for idx, matching in enumerate(all_stable_matchings):
    print(f"Matching {idx + 1}:")
    for hospital, student in matching.items():
        print(f"{hospital} is matched with {student}")
    print()
