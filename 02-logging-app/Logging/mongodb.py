import datetime
from .settings import DATABASE_URI
from mongoengine import connect, Document, StringField, DateTimeField, DynamicField

connect(host=DATABASE_URI)


class MicroserviceLog(Document):
    title = StringField(required=True, max_length=200)
    log_type = StringField(required=True, max_length=50)
    log_details = DynamicField(required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)
