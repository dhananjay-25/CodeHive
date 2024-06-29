import yaml
import task_handlers.generate_tasks as generate_tasks
import task_handlers.prioritize_tasks as prioritize_tasks
import task_handlers.execute_tasks as execute_tasks
import task_handlers.real_time_feedback as real_time_feedback

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    # Load the configuration file
    config = load_config('config.yaml')
    
    # Get the OpenAI API key from the config
    api_key = config['model']['api_key']
    
    while True:
        # Get user input
        user_input = input("Enter your plan for the week: ")
        
        # Generate tasks based on user input
        tasks = generate_tasks.generate_tasks(user_input, api_key)
        
        # Prioritize tasks
        prioritized_tasks = prioritize_tasks.prioritize_tasks(tasks)
        
        # Execute tasks
        execution_results = execute_tasks.execute_tasks(prioritized_tasks)
        
        # Display the generated and executed tasks
        print("\nGenerated and Executed Tasks:")
        for result in execution_results:
            print(result)
        
        # Get feedback from the user
        feedback = input("Provide any feedback on the tasks (e.g., missed tasks): ")
        
        # Update tasks based on feedback
        updated_tasks = real_time_feedback.real_time_feedback(prioritized_tasks, feedback)
        
        # Display updated tasks
        print("\nUpdated Tasks:")
        for task in updated_tasks:
            print(f"Task: {task['task']}")
            print(f"  Time: {task['time']}")
            print(f"  Date: {task['date']}\n")
        
        # Ask the user if they want to generate more tasks
        continue_input = input("Do you want to generate more tasks? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            break

if __name__ == "__main__":
    main()
