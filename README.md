# Task Tracker CLI

A simple Command Line Interface (CLI) application to manage your tasks, track their status, and keep organized. This project is a solution to the [Task Tracker](https://roadmap.sh/projects/task-tracker) challenge from roadmap.sh.

## Features

- **Add Tasks:** Create new tasks with a description.
- **Update Tasks:** Modify the description of existing tasks.
- **Delete Tasks:** Remove tasks from your list.
- **Track Status:** Mark tasks as `todo`, `in-progress`, or `done`.
- **List Tasks:** View all tasks or filter them by status.
- **Persistent Storage:** Tasks are automatically saved to a `tasks.json` file.

## Project Structure

- `task-cli.py`: The main entry point for the CLI application.
- `Tasks.py`: Contains the `Tasks` class for managing the collection of tasks.
- `task.py`: Defines the `Task` class representing a single task object.
- `tasks.json`: (Generated) The JSON file where tasks are stored.

## Requirements

- Python 3.12 or newer

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd task-tracker
   ```

2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage

Run the script using `python task-cli.py` followed by a command.

### Commands

#### 1. Add a new task

```bash
python task-cli.py add "Buy groceries"
```

#### 2. Update a task

```bash
python task-cli.py update <id> "Buy groceries and cook dinner"
```

#### 3. Delete a task

```bash
python task-cli.py delete <id>
```

#### 4. Mark a task as in progress

```bash
python task-cli.py mark-in-progress <id>
```

#### 5. Mark a task as done

```bash
python task-cli.py mark-done <id>
```

#### 6. List all tasks

```bash
python task-cli.py list
```

#### 7. List tasks by status

```bash
python task-cli.py list todo
python task-cli.py list in-progress
python task-cli.py list done
```

## Data Schema

Each task in `tasks.json` has the following structure:

```json
{
  "id": 1,
  "description": "Task description",
  "status": "todo",
  "created_at": "MM/DD/YYYY, HH:MM:SS:ffffff",
  "updated_at": "MM/DD/YYYY, HH:MM:SS:ffffff"
}
```
