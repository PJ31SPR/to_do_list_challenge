class TodoList:
    def __init__(self):
        self.task_list = []
        

    def get_todos(self):
        return self.task_list
        

    def add(self, todo):
        if todo in self.task_list:
            raise ValueError('todo already exists in list')
        else:
            self.task_list.append(todo)

    def incomplete(self):
        return [todo for todo in self.task_list if not todo.complete]

    def complete(self):
        return [todo for todo in self.task_list if todo.complete]

    def give_up(self):
        for todo in self.task_list:
            todo.complete = True


