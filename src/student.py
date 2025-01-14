class Student:
    def __init__(self, first_name, last_name, address, index_number, pesel, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.index_number = index_number
        self.pesel = pesel
        self.gender = gender

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "index_number": self.index_number,
            "pesel": self.pesel,
            "gender": self.gender,
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data["first_name"],
            data["last_name"],
            data["address"],
            data["index_number"],
            data["pesel"],
            data["gender"],
        )
