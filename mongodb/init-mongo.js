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