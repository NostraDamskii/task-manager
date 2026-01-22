class Task():
    def __init__(self, title):
        self.title=title
        self._completed=False

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if value=="":
            raise ValueError ("Задача не может быть пустой")
        if not isinstance(value,str):
            raise TypeError ("Задача должна быть строкой!")
        self._title=value
    
    @property
    def completed(self):
        return self._completed
    
    
    def mark_done(self):
        self._completed=True
    
    def __str__(self):
        if self._completed:
            status="✓"
        else:
            status=" "
        return f"[{status}]  {self.title}"
    
    
task = Task("Buy milk")
print(task)
task.mark_done()
print(task.completed)
print(task)
    
    

        