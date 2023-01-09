# Import the necessary libraries
import time
import jira

# Define a list to store the tasks
tasks = []

# Define a function to add a task to the list
def add_task(task):
    tasks.append(task)

# Define a function to remove a task from the list
def complete_task(task_number):
    del tasks[task_number]

# Define a function to list all tasks
def list_tasks():
    for i, task in enumerate(tasks):
        # Print the task number and task description
        print(f"{i+1}: {task}")

# Define a function to pull tasks from Jira
def pull_tasks_from_jira():
    # Connect to Jira using your account credentials
    jira_client = jira.JIRA(basic_auth=("your_username", "your_password"), options={"server": "your_server_url"})
    
    # Search for open tasks assigned to you
    jql = "assignee = currentUser() AND status = 'Open'"
    open_tasks = jira_client.search_issues(jql)
    
    # Add the tasks to the list
    for task in open_tasks:
        tasks.append(task.fields.summary)

# Define a function to start a Pomodoro timer for a task
def pomodoro(task_number):
    # Set the timer for 25 minutes
    minutes = 25
    seconds = 0
    total_seconds = minutes * 60 + seconds
    
    # Print the task description
    print(f"Starting Pomodoro for task {task_number}: {tasks[task_number]}")
    
    # Start the timer
    while total_seconds:
        # Calculate the minutes and seconds remaining
        minutes, seconds = divmod(total_seconds, 60)
        # Format the time string as MM:SS
        time_string = f"{minutes:02d}:{seconds:02d}"
        # Print the time string and progress bar
        print(f"{time_string} [{'#' * (total_seconds // 60)}]", end="\r")
        # Sleep for 1 second
        time.sleep(1)
        # Decrement the total number of seconds
        total_seconds -= 1
    # Print a message when the timer finishes
    print("Time's up!")

# Define the main function to handle input and call other functions
def main():
    while True:
        # Get the action from the user
        action = input("What do you want to do? (add/complete/list/pomodoro/jira) ")
        if action == "add":
            # Get the task from the user and add it to the list
            task = input("Enter task: ")
            add_task(task)
        elif action == "complete":
            # Get the task number from the user and remove it from the list
            task_number = int(input("Enter task number: ")) - 1
            complete_task(task_number)
        elif action == "list":
            # List all tasks
            list_tasks()
        elif action == "pomodoro":
            # List all tasks
            print("Here are the current tasks:")
            list_tasks()
            # Get the task number from the user and start the Pomodoro timer
            task_number = int(input("Enter task number: ")) - 1
            pomodoro(task_number)
        elif action == "jira":
            # Pull tasks from Jira and add them to the list
            pull_tasks_from_jira()
        else:
            # Print an error message for invalid input
            print("Invalid input")

# Call the main function
main()

