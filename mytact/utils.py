# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import six
import os
import sys
from pyfiglet import Figlet, figlet_format
import re
import json


from PyInquirer import style_from_dict, Token, prompt, print_json, Separator
from PyInquirer import Validator, ValidationError
from pprint import pprint

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


style = style_from_dict({
    Token.QuestionMark: '#673ab7 bold',
    Token.Answer: '#f44336 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})


def log(object, color="white", figlet=False, pretty=False, font='slant'):
    if not pretty:
        if colored:
            if not figlet:
                six.print_(colored(object, color))
            else:
                six.print_(colored(figlet_format(
                    object, font=font), color))
        else:
            six.print_(object)
    else:
        pprint(object)

class EmptyValidator(Validator):
    def validate(self, value):
        if len(value.text):
            return True
        else:
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position=len(value.text))

class EmailValidator(Validator):
    pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"

    def validate(self, email):
        if len(email.text):
            if re.match(self.pattern, email.text):
                return True
            else:
                raise ValidationError(
                    message="Invalid email",
                    cursor_position=len(email.text))
        else:
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position=len(email.text))

class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = re.match('^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid phone number',
                cursor_position=len(document.text))  # Move cursor to end
        else:
            return True

def askContactsInfo(kwargs):
    questions = [
        {
            'type': 'input',
            'name': 'firstname',
            'message': 'Enter firstname:',
            'default': "" if kwargs.get("firstname") is None else kwargs["firstname"],
            'validate': EmptyValidator,
        },
        {
            'type': 'input',
            'name': 'lastname',
            'message': 'Enter lastname:',
            'default': "" if kwargs.get("lastname") is None else kwargs["lastname"],
            'validate': EmptyValidator,
        },
        {
            # 'qmark': u'📞 ',
            'type': 'input',
            'name': 'phone',
            'message': 'Enter phone:',
            'default': "" if kwargs.get("phone") is None else kwargs["phone"],
            'validate': PhoneNumberValidator,
        },
        {
            # 'qmark': u'📧 ',
            'type': 'input',
            'name': 'email',
            'message': 'Enter email:',
            'default': "" if kwargs.get("email") is None else kwargs["email"],
            'validate': EmailValidator,
        }
    ]
    answers = prompt(questions, style=style)
    return answers

def askField(data):
    questions = []
    for key, value in data.items():
        question = {
           'type': 'input',
            'name': key,
            'message': 'Enter {}:'.format(key),
            'default': value,
            'validate': EmailValidator if key=="email" else PhoneNumberValidator if key == "phone" else EmptyValidator, 
        }
        questions.append(question)
    
    answers = prompt(questions, style=style)
    return answers

def pretty_format(data):
    contacts = []
    for contact in data:
        _contact = "{} {} ({}) <{}> [{}]".format(
            contact["firstname"], 
            contact["lastname"], 
            contact["email"],
            contact["phone"],
            contact["id"]
        )
        contacts.append(_contact)

    return contacts


def selectContact(data):
    questions = [
        {
            'qmark': u'📝 ',
            'type': 'list',
            'name': 'contact',
            'message': 'Select Contact',
            'choices': pretty_format(data),
            'filter': lambda val: val.lower()
        }
    ]
    answers = prompt(questions, style=style)
    return answers

def getConfigDir():
    if sys.platform == "win32":
        app_config_dir = os.getenv("LOCALAPPDATA")
    else:
        app_config_dir = os.getenv("HOME")
        if os.getenv("XDG_CONFIG_HOME"):
            app_config_dir = os.getenv("XDG_CONFIG_HOME")
            
    
    configDir = os.path.join(app_config_dir, ".config")
    return configDir

def create_data():
    path = os.path.join(getConfigDir(), "data.json")
    schema = [{"contacts": []}, {"todos": []}]
    if not os.path.exists(path) or len(open(path, 'r').read().strip()) == 0:
        with open(path, "w") as _data:
            json.dump(schema,_data)