from datetime import datetime, date
import re
from AddressBook import *
from exeptions import *


class Field:
    def __init__(self, value: str) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return self.value


class Name(Field):
    def __init__(self, first_name, last_name=None) -> None:
        if last_name:
            self.value = f"{first_name} {last_name}"
        else:
            self.value = first_name
    

class Phone(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value:str):
        if self.is_correct_phone(value):
            self.__value = value
        else:
            raise PhoneError(value)
        
    def is_correct_phone(self, value) -> bool:
        pattern = re.compile(r"\+\d{11,13}")
        result = re.fullmatch(pattern, value)
        
        return True if result else False


class Birthday(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value:str):
        if re.fullmatch(r"\d{1,2}-\d{1,2}-\d{4}", value):
            self.__value = datetime.strptime(value, "%d-%m-%Y")
        elif re.fullmatch(r"\d{1,2}\.\d{1,2}\.\d{4}", value):
            self.__value = datetime.strptime(value, "%d.%m.%Y")
        elif re.fullmatch(r"\d{1,2}/\d{1,2}/\d{4}", value):
            self.__value = datetime.strptime(value, "%d/%m/%Y")
        else:
            raise BirthdayError(value)
        
    def is_empty_date(self) -> bool:
        return self.__value == datetime(1, 1, 1)
    
    def __str__(self):
        return self.__value.strftime("%d-%m-%Y") if not self.is_empty_date() else ""


class Email(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value:str):
        if self.is_correct_email(value):
            self.__value = value.lower()
        else:
            raise EmailError(value)
        
    def is_correct_email(self, value) -> bool:
        pattern = re.compile(r"([a-zA-Z]{1}[a-zA-Z0-9_.]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,})")
        result = re.fullmatch(pattern, value)
        
        return True if result else False
    

class Adress(Field):
    pass


class Tag(Field):
    def __init__(self, value) -> None:
        return


class Note(Field):
    def __init__(self, title: str) -> None:
        self.title = title    


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None, email: Email = None, adress: Adress = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday
        self.email = email
        self.adress = adress


    def change_birthday(self, new_birthday:Birthday):
        self.birthday = new_birthday
        # try:
        #     self.birthday = datetime.strptime(new_birthday, "%d.%m.%Y").date()
        #     return f"Birthday set for {self.name}"
        # except ValueError:
        #     return f"Invalid birthday format. Please use dd.mm.yyyy format."


    def change_email(self, new_email:Email):
        self.email = new_email

    
    def change_adress(self, new_adress:Adress):
        self.adress = new_adress

    
    def add_phone(self, phone):
        if str(phone) not in [str(p) for p in self.phones]:
            self.phones.append(phone)
            return f"Succesfully added phone '{phone}' to name '{self.name}'"
        else:
            return f"Phone '{phone}' is already in record '{self}'"


    def change_phone(self, old_phone, new_phone):
        pass


    def change_name(self, new_name):
        pass


    def days_to_birthday(self):
        pass

    
    def __str__(self) -> str:
        result = ""
        if self.name:
            result = result + str(self.name)
        if len(self.phones):
            result = result + ", " + ",".join([str(p) for p in self.phones])
        if self.birthday:
            result = result + ", " + str(self.birthday)
        if self.email:
            result = result + ", " + str(self.email)
        if self.adress:
            result = result + ", " + str(self.adress)

        return result
