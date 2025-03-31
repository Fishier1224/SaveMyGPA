import pandas as pd

def calculate_gpa_scenarios(current_gpa, current_units, desired_gpa, max_future_units, college_A, college_A_minus):
    # Calculate current total grade points
    current_grade_points = current_gpa * current_units

    combinations = []
    
    for a_units in range(1, max_future_units):  # Exclude 0
        a_minus_units = max_future_units - a_units
        if a_minus_units == 0:
            continue  # Exclude 0

        total_grade_points = current_grade_points + college_A * a_units + college_A_minus * a_minus_units
        total_units = current_units + max_future_units
        new_gpa = total_grade_points / total_units

        if new_gpa >= desired_gpa:
            combinations.append((a_units, a_minus_units, round(new_gpa, 4)))

    df = pd.DataFrame(combinations, columns=["A Units", "A− Units", "Projected GPA"])
    return df
