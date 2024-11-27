class Query:
    def __init__(self,field,operation,value):
        self.field = field
        self.operation = operation
        self.value = value
    def __str__(self):
        return f"{self.field} {self.operation} {self.value}"