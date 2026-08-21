print("Welcome to the Gym Tracker!")

response = input("Would you like to track your exercise? (yes/no): ")


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


if response == "yes":
        workout = track_exercise()
        print("\nWorkout summary:")
        print(f"Exercise: {workout['exercise']}")
        for set_data in workout["sets"]:
                print(
                        f"Set {set_data['set']}: "
                        f"{set_data['reps']} reps at {set_data['weight_kg']} kg"
                )
else:
        print("Okay, have a great day!")