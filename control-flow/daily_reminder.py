task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
time_sensitive_message = ""
if time_bound == "yes":
    time_sensitive_message = " that requires immediate attention today!"
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
time_sensitive_message = ""
if time_bound == "yes":
    time_sensitive_message = " that requires immediate attention today!"

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task{time_sensitive_message}")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task{time_sensitive_message}")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a low priority task{time_sensitive_message}")
    case _:
        print("Invalid priority level entered. Please choose high, medium, or low.")
