from app import db
from sqlalchemy.dialects.postgresql import JSON

class EmailJson(db.Model):
    __tablename__ = 'emailjson'

    id = db.Column(db.Integer, primary_key=True)
    email_from = db.Column(db.String())
    subject = db.Column(db.String())
    json_value = db.Column(JSON)

    def __init__(self, email_from, subject, json_value):
        self.email_from = email_from
        self.subject = subject
        self.json_value = json_value

    def __repr__(self):
        return '<id {}>'.format(self.id)