from collections import UserDict
from datetime import datetime
import pickle
replies = ["hello", ["good bye", "close", "exit", ' ']]
answers = ['How can I help you?', 'Good bye!']


class AddressBook(UserDict): # логика поиска по записям
    MAX_VALUE = 3
    file_name = 'data.bin'

    def add_record(self, record): # добавляет Record в self.data
        # print('add_record(self, record)= ', self.data, record.name.value )
        self.data[record.name.value] = record

    def save(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self.data, file)

    def load(self, file_name):
        with open(file_name, 'rb') as file:
            self.data = pickle.load(file)
        return self.data
    
    def seach(self, seach_element):
        self.seach_element = seach_element
        # print(self.data)
        count = 0
        for i in ab:
            if self.seach_element in i or self.seach_element in ab.data[i].phones[0].value:
                print("name: ", i, end=" ")
                print_phones(ab[i])
                print("birthday: ", ab[i].birthday.value)
                count += 1
        if count == 0:
            print("No element")         

    def iterator():
        def __next__(self):
            if self.current_value < self.MAX_VALUE:
                self.current_value += 1
                return self.current_value
            raise StopIteration
class CustomIterator:
    def __iter__(self):
        return AddressBook()

class Field: # будет родительским для всех полей, в нем потом реализуем логику общую для всех полей
    def __init__(self, value):
        self.value = value  # обязательное поле с именем
        # print("Field_name = ", self.value)

class Name(Field):
    pass


class Phone(Field):

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, input):
        if input.isdigit():
            self._value = input
        else:
            raise ValueError("Wrong phone.")


class Birthday(Field):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, input):
        if (datetime.strptime(input, "%Y-%m-%d")):
            self._value = input
        else:
            raise ValueError("Wrong date.")



class Record: # отвечает за логику добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name
     def __init__(self, name: Name, phone:Phone=None, birthday:Birthday=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday

     def days_to_birthday(self):
        self.now = datetime.now()
        user_birthday = self.birthday.value.split('-')
        year_input = int((datetime.now()).year)
        month_input = int(user_birthday[1])
        day_input = int(user_birthday[2])
        control_date = datetime(year=year_input, month=month_input, day=day_input)
        if control_date < self.now:
            control_date = datetime(year=(year_input + 1), month=month_input, day=day_input)
        self.control_date = control_date
        return (control_date - datetime.now()).days
     

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except:
            return "Give me name and phone please"
    return inner

def print_phones(rec):
    for x in rec.phones:
        print("phone: ", x.value)

def print_all():
    for x in ab:
        print("name: ", x, end=" ")
        print_phones(ab[x])
        print("birthday: ", ab[x].birthday.value)

def print_remainder(rec):
    for x in ab:
        print("name: ", x, end=" ")
        print("remainder: ", ab[x].birthday.value)

# hello-good_bye-others
# @input_error
def reply(answer):
    if answer == replies[0]: # -> hello
        return answers[0]
    elif answer in replies[1]: # -> exit...
        return answers[1]
    else:
        # init
        name = None
        phone = None
        birthday = None

        comand = answer.split()
        input_comand = comand[0]
        name = Name(comand[1])
        if len(comand) >= 3:
            phone = Phone(comand[2])
        if len(comand) >= 4:
            birthday = Birthday(comand[3])

        if input_comand == 'add' or input_comand == 'change':
            rec = Record(name, phone, birthday)
            ab.add_record(rec)
        elif input_comand == 'phone':
            print_phones(ab.data[name.value])
        elif answer.startswith('show all'):
            print_all()
        elif answer.startswith('remainder'):
            print(ab.data[name.value].days_to_birthday())
        elif answer.startswith('save adressbook'):
            ab.save('data_ab.bin')
        elif answer.startswith('load adressbook'):
            ab.load('data_ab.bin')
        elif input_comand == 'seach':
            ab.seach(comand[1])
        return 'Ok'

ab = AddressBook() 

def main():
    botloop = True
    while botloop:
        print('user:', end=' ')
        rep = input().lower()
        print(reply(rep))
        if rep in replies[1]:
            botloop = False
       

if __name__ == '__main__':
    name = Name('bill')
    phone = Phone('1234567890')
    birthday = Birthday('1995-02-27')
    rec = Record(name, phone, birthday)
    ab = AddressBook()
    ab.add_record(rec)

    name = Name('qqq')
    phone = Phone('0987654321')
    birthday = Birthday('1995-03-03')
    rec = Record(name, phone, birthday)
    ab.add_record(rec)

    name = Name('www')
    phone = Phone('02222222222')
    birthday = Birthday('1996-02-02')
    rec = Record(name, phone, birthday)
    ab.add_record(rec)

    name = Name('eee')
    phone = Phone('03333333333')
    birthday = Birthday('1996-03-03')
    rec = Record(name, phone, birthday)
    ab.add_record(rec)

    name = Name('rrr')
    phone = Phone('0444444444')
    birthday = Birthday('1996-04-04')
    rec = Record(name, phone, birthday)
    ab.add_record(rec)

    assert isinstance(ab['bill'], Record)
    assert isinstance(ab['bill'].name, Name)
    assert isinstance(ab['bill'].phones, list)
    assert isinstance(ab['bill'].phones[0], Phone)
    assert ab['bill'].phones[0].value == '1234567890'
    print('All Ok)')
    main()
    