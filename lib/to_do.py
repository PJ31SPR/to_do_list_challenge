class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        if task == '':
            raise Exception('task cannot be empty')
        elif not isinstance(task, str):
            raise Exception('task must be type string')
        else:
            self.task = task
            self.complete = False

    def get_task(self):
        return self.task
    
    def get_complete(self):
        return self.complete
        
    def mark_complete(self):
        self.complete = True
            
