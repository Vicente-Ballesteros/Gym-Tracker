import json
import datetime
x = datetime.datetime.now()

date = str(x.strftime("%x"))
print(date)

print("Welcome to the Gym Tracker!")

response = input("Would you like to track your exercise? (yes/no): ").lower()
answer = ["yes", "y"]

try:
    with open("workouts.json", "r") as f:
        all_workouts = json.load(f)
except FileNotFoundError:
    all_workouts = []

def track_exercise():
        exercise = input("Enter the name of the exercise you want to track: ")
        number_of_sets = int(input("Enter the number of sets: "))
        workout = {
                "exercise": exercise,
                "sets": []
        }

        for set_number in range(number_of_sets):
                print(f"Set {set_number + 1}:")
                reps = int(input("Enter the number of reps: "))
                weight = int(input("Enter the weight used (in kg): "))
                workout["sets"].append({
                        "set": set_number + 1,
                        "reps": reps,
                        "weight_kg": weight
                })

        return workout


if response in answer:
        session = {
        "date": date,
        "exercises": []
        }

        keep_going = True
        while keep_going:
                workout = track_exercise()
                session["exercises"].append(workout)
                more = input("Would you like to track another exercise? (yes/no): ").lower()
                keep_going = more in answer

        print("\nWorkout summary:")
        for workout in session["exercises"]:
                print(f"Exercise: {workout['exercise']}")
                for set_data in workout["sets"]:
                        print(
                                f"Set {set_data['set']}: "
                                f"{set_data['reps']} reps at {set_data['weight_kg']} kg"
                        )

        all_workouts.append(session)
        with open("workouts.json", "w") as f:
                json.dump(all_workouts, f, indent=4)
else:
        print("Okay, have a great day!")