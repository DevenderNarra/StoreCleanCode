class Store:
    def __init__(self):
        self.items = []

    def add_item(self,items):
          self.items.append(items)

    def filter(self, query):
        if query.operation == "IN":
            return [
                item for item in self.items if getattr(item, query.field, None) in query.value
            ]
        elif query.operation == "EQ":
            return [
                item for item in self.items if getattr(item, query.field, None) == query.value
            ]
        elif query.operation == "GT":
            return [
                item for item in self.items if getattr(item, query.field, None) > query.value
            ]
        elif query.operation == "GTE":
            return [
                item for item in self.items if getattr(item, query.field, None) >= query.value
            ]
        elif query.operation == "LT":
            return [
                item for item in self.items if getattr(item, query.field, None) < query.value
            ]
        elif query.operation == "LTE":
            return [
                item for item in self.items if getattr(item, query.field, None) <= query.value
            ]
        elif query.operation == "starts_with":
            return [
                item for item in self.items if str(getattr(item, query.field, None)).startswith(query.value)
            ]
        elif query.operation == "ends_with":
            return [
                item for item in self.items if str(getattr(item, query.field, None)).endswith(query.value)
            ]
        elif query.operation == "contains":
            return [
                item for item in self.items if query.value in str(getattr(item, query.field,""))
            ]
        else:
            raise ValueError(f"Invalid operation: {query.operation}")
    def exclude(self,query):
        if query.operation == "GT":
            return [
                item for item in self.items if getattr(item, query.field, None) >  (query.value)
            ]
        if query.operation == "IN":
            return [
                item for item in self.items if getattr(item, query.field, None) in query.value
            ]
        elif query.operation == "EQ":
            return [
                item for item in self.items if getattr(item, query.field, None) == query.value
            ]
        elif query.operation == "CONTAINS":
            return [
                item for item in self.items if query.value in str(getattr(item, query.field,""))
            ]
        else:
            raise ValueError(f"Invalid operation: {query.operation}")

    def count(self):
        return len(self.items)

    def __str__(self):
        return "\n".join(str(item) for item in self.items)