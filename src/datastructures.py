from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name" : self.last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name" : self.last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name" : self.last_name,
            "age": 5,
            "lucky_numbers": [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if 'id' in member:
                member["last_name"] = self.last_name
                self._members.append(member)
                return member
        else:
                member['id'] = self._generateId()
                self._members.append(member)
                return member
    
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                index = self._members.index(member)
                self._members.pop(index)
                return self._members

    def get_all_members(self):
        return self._members
