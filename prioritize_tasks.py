def prioritize_tasks(tasks):
    # Example prioritization logic: tasks containing "Study" come first
    prioritized_tasks = sorted(tasks, key=lambda x: "Study" not in x["task"])
    return prioritized_tasks

# Example usage for testing purposes
if __name__ == "__main__":
    tasks = [
        {"task": "Study AI", "time": "No specific time", "date": "No specific date"},
        {"task": "Exercise", "time": "No specific time", "date": "No specific date"}
    ]
    prioritized_tasks = prioritize_tasks(tasks)
    print(prioritized_tasks)
