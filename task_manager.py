from task import Task
import json
import os.path

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


    def save_to_file(self,filename):
        data=[]
        for task in self._tasks:
            data.append({"title": task.title, "completed":task.completed})

        with open (filename,"w", encoding="utf-8") as file:
            json.dump(data,file,ensure_ascii=False, indent=2)

    def load_from_file(self, filename):
        self._tasks=[]
        try:
            with open(filename, encoding="utf-8") as file:
                data=json.load(file)
            for item in data:
                task=Task(item.get("title"))
                if item.get("completed"):
                    task.mark_done()
                self._tasks.append(task)

        except FileNotFoundError:
            self._tasks=[]
        
 