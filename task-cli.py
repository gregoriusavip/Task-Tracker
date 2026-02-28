import argparse
import sys
import os
import json
from Tasks import Tasks

FILEPATH = "tasks.json"

def pretty_print(tasks_list):
    # tasks_list is a list of object formatted just like how it is in tasks.json
    for task in tasks_list:
        print(f"ID: {task["id"]}. Description: {task["description"]}. Status: {task["status"]}. Created_at: {task["created_at"]}. Updated_at: {task["updated_at"]}")

def load_data():
    if not os.path.exists(FILEPATH):
        with open(FILEPATH, "x"): pass
        return []
    else:
        with open(FILEPATH, "r") as f:
            data = json.load(f)
        return data
    
def save_data(data):
    with open(FILEPATH, "w") as f:
        json.dump(data, f, indent=4)


def add_task(args, tasks):
    if tasks.add_task(args.description):
        print (f"Task added successfully (ID: {tasks.latest_id})")
    else:
        print ("Failed to add a task")

def delete_task(args, tasks):
    if tasks.delete_task(args.id):
        print (f"Deleted task (ID: {args.id})")
    else:
        print ("Failed to delete task")

def update_task(args, tasks):
    if tasks.update_description(args.id, args.description):
        print (f"Updated task (ID: {args.id})")
    else:
        print ("Failed to update task")

def in_progress(args, tasks):
    if tasks.update_status(args.id, 2):
        print (f"Task {args.id} is now in progress")
    else:
        print ("Failed to mark task")

def done(args, tasks):
    if tasks.update_status(args.id, 3):
        print (f"Task {args.id} is now completed")
    else:
        print ("Failed to mark task")

def list_all(args, tasks):
    pretty_print(tasks.tasks_list)

def list_done(args, tasks):
    pretty_print(tasks.filter_task(3))

def list_in_progress(args, tasks):
    pretty_print(tasks.filter_task(2))

def list_todo(args, tasks):
    pretty_print(tasks.filter_task(1))

def main():
    # create the top-level parser
    parser = argparse.ArgumentParser(description="Maintains a list of tasks")
    subparsers = parser.add_subparsers(description="Commands to use on the list")

    # create the parser for the "add" command
    add_description = "Adds a task with a description to the list. An ID will be assigned automatically to this task."
    parser_add = subparsers.add_parser('add', description=add_description, help=add_description)
    parser_add.add_argument('description')
    parser_add.set_defaults(func=add_task)

    # create the parser for the "update" command
    update_description = "Updates a task selected from the ID."
    parser_update = subparsers.add_parser('update', description=update_description, help=update_description)
    parser_update.add_argument('id', type=int)
    parser_update.add_argument('description')
    parser_update.set_defaults(func=update_task)    

    # create the parser for the "delete" command
    delete_description = "Deletes a task from the list selected from the ID."
    parser_delete = subparsers.add_parser('delete', description=delete_description, help=delete_description)
    parser_delete.add_argument('id', type=int)
    parser_delete.set_defaults(func=delete_task)

    # create the parser for the "mark in progress" command
    in_progress_description = "Marks a task as in progress from the list selected from the ID."
    parser_in_progress = subparsers.add_parser('mark-in-progress', description=in_progress_description, help=in_progress_description)
    parser_in_progress.add_argument('id', type=int)
    parser_in_progress.set_defaults(func=in_progress)

    # create the parser for the "mark done" command
    done_description = "Marks a task as completed from the list selected from the ID."
    parser_done = subparsers.add_parser('mark-done', description=done_description, help=done_description)
    parser_done.add_argument('id', type=int)
    parser_done.set_defaults(func=done)

    # create the parser for the "list" command
    list_description = "Prints all the tasks or optionally by its status"
    parser_list = subparsers.add_parser('list', description=list_description, help=list_description)
    parser_list.set_defaults(func=list_all)
    list_subparser = parser_list.add_subparsers(description="Optional filter by tasks' status")

    # lists done optional arguments
    list_done_description = "Prints out all done tasks"
    list_parser_done = list_subparser.add_parser('done', description=list_done_description, help=list_done_description)
    list_parser_done.set_defaults(func=list_done)

    # lists todo optional arguments
    list_todo_description = "Prints out all todo tasks"
    list_parser_todo = list_subparser.add_parser('todo', description=list_todo_description, help=list_todo_description)
    list_parser_todo.set_defaults(func=list_todo)

    # lists in-progress optional arguments
    list_progress_description = "Prints out in-progress tasks"
    list_parser_progress = list_subparser.add_parser('in-progress', description=list_progress_description, help=list_progress_description)
    list_parser_progress.set_defaults(func=list_in_progress)

    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    tasks = Tasks(load_data())
    args.func(args, tasks)
    save_data(tasks.tasks_list)


if __name__ == "__main__":
    main()