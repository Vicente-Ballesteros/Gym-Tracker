print("Welcome to the Gym Tracker!")

response = input("Would you like to track your exercise? (yes/no): ")
def track_exercise():
        exercise = input("Enter the name of the exercise you want to track: ")
        sets = int(input("Enter the number of sets: "))
        for i in range(sets):
            print(f"Set {i + 1}:")
            reps = int(input("Enter the number of reps: "))
            weight = int(input("Enter the weight used (in kg): "))
            print(f"Exercise: {exercise}, Set: {i + 1}, Reps: {reps}, Weight: {weight} kg")
if response == "yes":
        track_exercise()
else:
    print("Okay, have a great day!") 
    exit()