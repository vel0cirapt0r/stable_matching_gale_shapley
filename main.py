def stable_matching(hospital_pref, student_pref):
    hospital_to_student = {hospital: None for hospital in hospital_pref}
    student_to_hospital = {}

    while any(hospital_to_student[h] is None for h in hospital_pref):
        h = next(h for h in hospital_pref if hospital_to_student[h] is None)
        s = hospital_pref[h].pop(0)

        if s not in student_to_hospital:
            # s is unmatched, so match h with s
            hospital_to_student[h] = s
            student_to_hospital[s] = h
        else:
            # s is currently matched with h'
            h_prime = student_to_hospital[s]
            if student_pref[s].index(h) < student_pref[s].index(h_prime):
                # s prefers h over h', so match h with s
                hospital_to_student[h] = s
                hospital_to_student[h_prime] = None  # h' becomes unmatched
                student_to_hospital[s] = h

    return hospital_to_student


# Example usage:
hospital_preferences = {
    'H1': ['S1', 'S2', 'S3'],
    'H2': ['S1', 'S3', 'S2'],
    'H3': ['S3', 'S2', 'S1']
}

student_preferences = {
    'S1': ['H2', 'H1', 'H3'],
    'S2': ['H1', 'H3', 'H2'],
    'S3': ['H1', 'H2', 'H3']
}

stable_matching_result = stable_matching(hospital_preferences, student_preferences)

print("Stable Matching:")
for hospital, student in stable_matching_result.items():
    print(f"{hospital} is matched with {student}")
