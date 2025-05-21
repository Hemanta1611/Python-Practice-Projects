# To-Do List Management Application

A simple command-line To-Do List Management Application built with Python that allows users to manage their tasks efficiently.

## Features

- View all tasks with their completion status
- Add new tasks with title and description
- Delete existing tasks
- Mark tasks as completed
- Persistent storage using JSON file
- User-friendly command-line interface

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone the repository or download the project files
2. Navigate to the project directory
3. Run the application using Python:
   ```bash
   python main.py
   ```

## Usage

The application provides a menu-driven interface with the following options:

1. **View Tasks**: Displays all tasks with their completion status
2. **Add Task**: Add a new task by providing a title and description
3. **Delete Task**: Remove a task by selecting its index number
4. **Mark Task as Completed**: Mark a task as completed by selecting its index number
5. **Save and Exit**: Save all changes and exit the application

## Data Storage

The application stores all tasks in a JSON file (`todo_list.json`) in the project directory. The data structure is as follows:

```json
{
    "tasks": [
        {
            "title": "Task Title",
            "description": "Task Description",
            "completed": false
        }
    ]
}
```

## Error Handling

The application includes basic error handling for:
- File operations (reading/writing tasks)
- Invalid user inputs
- Task index validation

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.