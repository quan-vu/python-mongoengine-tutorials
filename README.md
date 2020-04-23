# MongoDB with Python & MongoEngine

A collection of example for working with MongoDB in Python.

In this tutorial, we use mongoenine **A Python Object-Document-Mapper for working with MongoDB**.

## Prerequisites

- Python 3
- Python Virtualenv
- MongoDB

## Quickstart

Start Mongo database use Docker

```shell
cd mongodb
docker-compose up -d
```

Test simple app

```
cd 01-simple
python app.py
```

## Multiple Mongo database in Docker

You can add multiple mongo database use one docker container.

Edit file: init-mongo.js

```javascript
print('Start #######################');

db = db.getSiblingDB('db_01');
db.createUser(
  {
    user: 'myuser',
    pwd: 'mypassword',
    roles: [{ role: 'readWrite', db: 'db_01' }],
  },
);
db.createCollection('example');

db = db.getSiblingDB('db_02');
db.createUser(
  {
    user: 'myuser',
    pwd: 'mypassword',
    roles: [{ role: 'readWrite', db: 'db_02' }],
  },
);
db.createCollection('example');

print('END #######################');
```

