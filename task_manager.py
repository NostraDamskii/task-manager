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
    
    def remove_task(self,index):
        if index <0 or index>=len(self._tasks):
            raise IndexError("Wrong index for remove")
        #self._tasks.remove(self._tasks[index])
        self._tasks.pop(index)

    def mark_task_done(self,index):
        if index <0 or index>=len(self._tasks):
            raise IndexError("Wrong index for mark")
        self._tasks[index].mark_done()


