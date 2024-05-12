from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    @staticmethod
    def validate_phone_number(number):
        return len(number) == 10 and number.isdigit()

    def __init__(self, value):
        super().__init__(value)
        if not self.validate_phone_number(value):
            raise ValueError("Invalid phone number format")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, old_phone_number, new_phone_number):
        if old_phone_number not in [phone.value for phone in self.phones]:
            raise ValueError("Old phone number not found")

        if not Phone.validate_phone_number(new_phone_number):
            raise ValueError("Invalid new phone number format")

        self.remove_phone(old_phone_number)
        self.add_phone(new_phone_number)

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        raise ValueError("Phone number not found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(phone.value for phone in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        raise ValueError("Contact not found")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Contact not found")



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
john.edit_phone("0504589632", "0678569845")
print(john)

found_phone = john.find_phone("0678569845")
print(f"{john.name}: {found_phone}")

book.delete("Jana")
