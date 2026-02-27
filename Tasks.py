import os
import json
from datetime import datetime
from task import Task

FILEPATH = "tasks.json"


# A collection of tasks
class Tasks:
    def __init__(self, data):
        self.tasks_list = data
        self.latest_id = (
            0 if not self.tasks_list else max(task.get("id") for task in self.tasks_list)
        )

    def _load_data(self):
        if not os.path.exists(FILEPATH):
            return []
        else:
            with open(FILEPATH, "r") as f:
                data = json.load(f)
            return data

    def _find_task_index(self, id):
        for index, task in enumerate(self.tasks_list):
            if task.get("id") == id:
                return index
        return None

    def add_task(self, description):
        self.latest_id += 1
        now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
        self.tasks_list.append(Task(self.latest_id, description, "todo", now, now).to_dict())
        return True

    def delete_task(self, id):
        index = self._find_task_index(id)
        if index >= 0:
            self.tasks_list.pop(index)
            return True
        return False

    def update_description(self, id, description):
        index = self._find_task_index(id)
        if index >= 0:
            self.tasks_list[index].update(
                {
                    "description": description,
                    "updated_at": datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f"),
                }
            )
            return True
        return False

    def update_status(self, id, status):
        statuses = {1: "todo", 2: "in-progress", 3: "done"}
        index = self._find_task_index(id)
        if index >= 0:
            self.tasks_list[index].update(
                {
                    "status": statuses.get(status),
                    "updated_at": datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f"),
                }
            )
            return True
        return False
