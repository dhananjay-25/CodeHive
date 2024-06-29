import openai
import re

def openai_completion(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def extract_time_and_date(task):
    time_pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d\b'  # Matches HH:MM format
    date_pattern = r'\b(?:\d{1,2}(?:st|nd|rd|th)? (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}(?:st|nd|rd|th)?)\b'
    
    time_match = re.search(time_pattern, task)
    date_match = re.search(date_pattern, task)
    
    time = time_match.group() if time_match else "No specific time"
    date = date_match.group() if date_match else "No specific date"
    
    return time, date

def generate_tasks(user_input, api_key):
    prompt = f"Generate a detailed list of tasks based on the following user input: \"{user_input}\""
    tasks_text = openai_completion(prompt, api_key)

    tasks = tasks_text.split('\n')
    tasks = [task.strip() for task in tasks if task.strip()]

    detailed_tasks = []
    for task in tasks:
        time, date = extract_time_and_date(task)
        detailed_task = {
            "task": task,
            "time": time,
            "date": date
        }
        detailed_tasks.append(detailed_task)
    
    return detailed_tasks

# Example usage for testing purposes
if __name__ == "__main__":
    user_input = "Plan my week with study sessions for AI and exercise routines."
    api_key = "YOUR_OPENAI_API_KEY"  # Replace with your OpenAI API key
    tasks = generate_tasks(user_input, api_key)
    print(tasks)
