import json
import datetime

def load_workouts():
    try:
        with open("workouts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_workouts(all_workouts):
    with open("workouts.json", "w") as f:
        json.dump(all_workouts, f, indent=4)

def get_valid_response(prompt):
    while True:
        response = input(prompt).lower()
        if response in ["yes", "no", "y", "n"]:
            break
        else:
            print("Please enter a valid response (yes/no).")
    return response

def get_valid_input(prompt):
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print("Please enter a valid number.")
    return number

def track_exercise():
    exercise = input("Enter the name of the exercise you want to track: ")
    number_of_sets = get_valid_input("Enter the number of sets: ")
    workout = {
        "exercise": exercise,
        "sets": []
    }

    for set_number in range(number_of_sets):
        print(f"Set {set_number + 1}:")
        reps = get_valid_input("Enter the number of reps: ")
        weight = get_valid_input("Enter the weight used (in kg): ")

        workout["sets"].append({
            "set": set_number + 1,
            "reps": reps,
            "weight_kg": weight
        })

    return workout

def print_session(session):
    print(f"Date: {session['date']}")
    for workout in session["exercises"]:
        print(f"Exercise: {workout['exercise']}")
        for set_data in workout["sets"]:
            print(
                f"Set {set_data['set']}: "
                f"{set_data['reps']} reps at {set_data['weight_kg']} kg"
            )

def log_session(all_workouts):
    session_date = str(datetime.datetime.now().strftime("%x"))
    session = {
        "date": session_date,
        "exercises": []
    }

    keep_going = True
    while keep_going:
        workout = track_exercise()
        session["exercises"].append(workout)
        more = get_valid_response("Would you like to track another exercise? (yes/no): ")
        keep_going = more in ["yes", "y"]

    print("\nWorkout summary:")
    print_session(session)

    all_workouts.append(session)
    save_workouts(all_workouts)

def view_history(all_workouts):
    if not all_workouts:
        print("No workouts logged yet.")
        return

    for i, session in enumerate(all_workouts, start=1):
        print(f"\n--- Session {i} ---")
        print_session(session)

def main():
    all_workouts = load_workouts()
    print("Welcome to the Gym Tracker!")

    while True:
        print("\n1. Log a workout")
        print("2. View history")
        print("3. Quit")
        choice = input("> ")

        if choice == "1":
            log_session(all_workouts)
        elif choice == "2":
            view_history(all_workouts)
        elif choice == "3":
            print("Okay, have a great day!")
            break
        else:
            print("Not a valid option, try again.")

if __name__ == "__main__":
    main()
