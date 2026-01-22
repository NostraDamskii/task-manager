from task import Task

class TaskManager():
    def __init__(self):
        self._tasks=[]
    
    def add_task(self,title):
        new_task=Task(title)
        self._tasks.append(new_task)

    def list_tasks(self):
        string_list=[]
        for task in self._tasks:
            string_list.append(str(task))
        return string_list
    

