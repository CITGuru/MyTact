# MyTact

A simple cli for managing contacts

# Installation

Clone this github repo

```bash
$ git clone https://github.com/citguru/mytact
$ cd mytact
```
Create a virtualenv

```bash
$ mkvirtualenv mytactenv
$ workon mytactenv
```

Install Python Libraries

```bash
$ pip install -r requirements.txt
```

# Usage

```bash
$ python mytact.py --help
```

## Add

```bash
$ python mytact.py add
```

With arguments

```bash
$ python mytact.py add <firstname> <lastname> <email> <phone>
```

E.g

```bash
$ python mytact.py add Oyetoke Toby oyetoketoby80@gmail.com 08182315466
```

## Update

```bash
$ python mytact.py update
```

or

```bash
$ python mytact.py update --id <ID>
```

E.g 
```bash
$ python mytact.py update --id 8686
```

With options

```bash
$ python mytact.py update --id <ID> --firstname <firstname> --lastname <lastname>
```

E.g

```bash
$ python mytact.py update --id 8686 --firstname Oyetoke --lastname Toby
```

## List

```bash
$ python mytact.py list
```
or

```bash
$ python mytact.py list <len:int>
```
E.g
```bash
$ python mytact.py list 2
```

## Find

```bash
$ python mytact.py find
```

or

```bash
$ python mytact.py find <query>
```

E.g 
```bash
$ python mytact.py find Toby
```

With options

```bash
$ python mytact.py find --firstname <firstname> 
```

E.g

```bash
$ python mytact.py find --firstname Oyetoke
```

## Delete

```bash
$ python mytact.py delete
```

With options

```bash
$ python mytact.py delete --id <ID> 
```

E.g

```bash
$ python mytact.py delete --id 86800
```