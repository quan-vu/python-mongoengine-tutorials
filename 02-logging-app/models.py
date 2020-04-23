import datetime
from mongoengine import *

connect(host='mongodb://myuser:mypassword@127.0.0.1:27017/db_02')


class MicroserviceLog(Document):
    title = StringField(required=True, max_length=200)
    log_type = StringField(required=True, max_length=50)
    log_details = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)