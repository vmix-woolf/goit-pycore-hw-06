from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, value):
        self.filed = value


    def validation_phone(phone)-> bool:
        return True if len(phone) == 10 and phone.isdigit() else False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
        if Phone.validation_phone(phone):
            self.phones.append(phone)
        else:
            raise ExactDigitException('Phone should consist of exactly 10 digits!')


    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)


    def edit_phone(self, old_phone, new_phone):
        try:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
        except ValueError:
            print(f"No a such phone")
            exit()

    
    def find_phone(self, phone):
        index = self.phones.index(phone)
        return self.phones[index]

    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


class AddressBook(UserDict):
    current_id = 1

    def add_record(self, record):
        self.data[AddressBook.current_id] = record
        AddressBook.current_id += 1

    
    def find(self, name):
        for _, record in self.data.items():
            if record.name.value == name:
                return record

    
    def delete(self, name):
        {key: record for key, record in self.data.items() if record.name.value != name}
        

class ExactDigitException(Exception):
    pass


#  check functionality
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення телефону у записі John
john.remove_phone("5555555555")

# Видалення запису Jane
book.delete("Jane")
