class Shelter:
    def __init__(self, id, name, location, capacity, status):
        self.id = id
        self.name = name
        self.location = location
        self.capacity = capacity
        self.status = status

    def is_available(self):
        return self.status == 'available'

    def update_status(self, new_status):
        self.status = new_status

    def __repr__(self):
        return f"Shelter(id={self.id}, name={self.name}, location={self.location}, capacity={self.capacity}, status={self.status})"