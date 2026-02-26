import argparse
import sys

# create the top-level parser
parser = argparse.ArgumentParser(description="Maintains a list of tasks")
subparsers = parser.add_subparsers(description="Commands to use on the list")

# create the parser for the "add" command
add_description = "Adds a task with a description to the list. An ID will be assigned automatically to this task."
parser_add = subparsers.add_parser('add', description=add_description, help=add_description)
parser_add.add_argument('description')

# create the parser for the "update" command
update_description = "Updates a task selected from the ID."
parser_update = subparsers.add_parser('update', description=update_description, help=update_description)
parser_update.add_argument('id', type=int)
parser_update.add_argument('description')

# create the parser for the "delete" command
delete_description = "Deletes a task from the list selected from the ID."
parser_delete = subparsers.add_parser('delete', description=delete_description, help=delete_description)
parser_delete.add_argument('id', type=int)

# create the parser for the "mark in progress" command
in_progress_description = "Marks a task as in progress from the list selected from the ID."
parser_in_progress = subparsers.add_parser('mark-in-progress', description=in_progress_description, help=in_progress_description)
parser_in_progress.add_argument('id', type=int)

# create the parser for the "mark done" command
done_description = "Marks a task as completed from the list selected from the ID."
parser_done = subparsers.add_parser('mark-done', description=done_description, help=done_description)
parser_done.add_argument('id', type=int)

# create the parser for the "list" command
list_description = "Prints all the tasks or optionally by its status"
parser_list = subparsers.add_parser('list', description=list_description, help=list_description)
list_subparser = parser_list.add_subparsers(description="Optional filter by tasks' status")

# lists done optional arguments
list_done_description = "Prints out all done tasks"
list_parser_done = list_subparser.add_parser('done', description=list_done_description, help=list_done_description)

# lists todo optional arguments
list_todo_description = "Prints out all todo tasks"
list_parser_todo = list_subparser.add_parser('todo', description=list_todo_description, help=list_todo_description)

# lists in-progress optional arguments
list_progress_description = "Prints out in-progress tasks"
list_parser_progress = list_subparser.add_parser('in-progress', description=list_progress_description, help=list_progress_description)

parser.parse_args(args=None if sys.argv[1:] else ['--help'])
