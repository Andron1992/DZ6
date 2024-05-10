class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if str(p) == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p
        return None

    def __str__(self):
        phones_str = ', '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}"

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("Baric")
    john_record.add_phone("0504589632")
    john_record.add_phone("0678569845")

    book.add_record(john_record)

    jane_record = Record("Jana")
    jane_record.add_phone("0959635698")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("Baric")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)

    if john:
        found_phone = john.find_phone("0678569845")
        if found_phone:
            print(f"{john.name}: {found_phone}")

    book.delete("Jana")
