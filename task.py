# A singular task
class Task:
    def __init__(self, id, description, status, created_at, updated_at):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return  {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'created_at' : self.created_at,
            'updated_at': self.updated_at
        }