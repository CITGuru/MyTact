import sys
import click
from mytact.utils import askContactsInfo, log, selectContact, pretty_format, askField, create_data
import uuid
from pprint import pprint
from mytact.db import load, insert

create_data()

data = load()

@click.group()
@click.version_option("1.0.0")
def main():
    """A Simple Contacts App CLI"""
    pass

@main.command()
@click.argument('firstname', required=False)
@click.argument('lastname', required=False)
@click.argument('email', required=False)
@click.argument('phone', required=False)
# @click.option("--birthday")
def add(**kwargs):
    """Add a Contact"""
    contacts = data[0]["contacts"]
    contact = askContactsInfo(kwargs)
    contact["id"] = str(uuid.uuid4())
    contacts.append(contact)
    data[0]["contacts"] = contacts
    insert(data)
    log("Contact saved..", color="green")
    
@main.command()
@click.option("--id", help='Contact ID')
def delete(**kwargs):
    """Delete a Contact"""
    contacts = data[0]["contacts"]
    if len(contacts) == 0:
        log("Empty Contact list..", color="green")
        return
    pos = 0
    if kwargs.get("id"):
        for contact in contacts:
            if contact["id"] == kwargs["id"]:
                _contact = contact
            pos+=1
    else:
        _data = selectContact(contacts)
        kwargs["id"] = _data["contact"].split("[")[-1].split("]")[0]
        for contact in contacts:
            if contact["id"] == kwargs["id"]:
                _contact = contact
                break
            pos+=1
            
    data[0]["contacts"].pop(pos)
    insert(data)
    log("Contact deleted..", color="green")

@main.command()
@click.option("--id", help='Contact ID')
@click.option("--firstname", help='Contact firstname')
@click.option("--lastname", help='Contact lastname')
@click.option("--email", help='Contact email')
@click.option("--phone", help='Contact phone')
def update(**kwargs):
    """Update a Contact"""
    contacts = load()[0]["contacts"]
    if len(contacts) == 0:
        log("Empty Contact list..", color="green")
        return
    pos = 0
    if kwargs.get("id"):
        for contact in contacts:
            if contact["id"] == kwargs["id"]:
                _contact = contact
                break
            else:
                log("Contact not found!", color="red")
                sys.exit()
            pos+=1
    else:
        _data = selectContact(contacts)
        kwargs["id"] = _data["contact"].split("[")[-1].split("]")[0]
        for contact in contacts:
            if contact["id"] == kwargs["id"]:
                _contact = contact
                break
            pos+=1
    
    id = kwargs.pop("id")

    if any(value is not None for value in kwargs.values()):
        _kwargs = {key:value for key, value in kwargs.items() if value is not None}
        contact = askField(_kwargs)
        for key, value in _kwargs.items():
            _contact[key] = value
        contact = _contact
    else:
        contact = askContactsInfo(_contact)
    
    kwargs["id"] = id
    contact["id"] = kwargs["id"]
    data[0]["contacts"][pos] = contact
    insert(data)
    log("Contact updated..", color="green")

@main.command()
@click.argument("len", type=click.INT, required=False)
def list(**kwargs):
    """List Contacts"""
    contacts = load()[0]["contacts"]
    if kwargs.get("len"):
        contacts = contacts[:kwargs["len"]]
    pretty_contact = pretty_format(contacts)
    for contact in pretty_contact:
        log(contact, color="blue")
    log("{} contacts".format(len(pretty_contact)))

@main.command()
@click.argument("query", required=False)
@click.option("--id", help='Contact ID')
@click.option("--firstname", help='Contact firstname')
@click.option("--lastname", help='Contact lastname')
@click.option("--email", help='Contact email')
@click.option("--phone", help='Contact phone')
def find(**kwargs):
    """Find Contact"""
    data = load()[0]["contacts"]
    contacts = []
    for contact in data:
        for opt in kwargs:
            if opt == "query":
                if kwargs[opt].lower() in (x.lower() for x in contact.values()):
                    contacts.append(contact)
            else:
                if kwargs[opt] == contact[opt]:
                    contacts.append(contact)
    
    pretty_contact = pretty_format(contacts)
    for contact in pretty_contact:
        log(contact, color="blue")
    
    log("{} contact(s)".format(len(pretty_contact)))

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        log("MyTact", color="blue", figlet="True", font="georgia11")
    main()