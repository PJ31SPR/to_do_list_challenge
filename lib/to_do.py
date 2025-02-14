class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        if not isinstance(task, str):
            raise TypeError('task must be type string')
        elif task.strip() == '':
            raise ValueError('task cannot be empty')
        else:
            self.task = task
            self.complete = False

    def get_task(self):
        return self.task
    
    def get_complete(self):
        return self.complete
        
    def mark_complete(self):
        self.complete = True
            
