import datetime
from mongoengine import (
    BooleanField,
    Document,
    EmbeddedDocument,
    EmbeddedDocumentListField,
    EmbeddedDocumentField,
    ListField,
    StringField,
    DateTimeField,
    ObjectIdField
)
from bson.objectid import ObjectId
# from marshmallow.fields import Nested
from marshmallow.fields import Int
from marshmallow_mongoengine import ModelSchema


class Answer(EmbeddedDocument):
    question = StringField(required=True)
    text = StringField(required=True)


class AnswerSet(EmbeddedDocument):
    _id = ObjectIdField(required=True, default=ObjectId)
    answers = ListField(EmbeddedDocumentField(Answer))
    new = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now)


class Site(Document):
    name = StringField(max_length=200, required=True)
    url = StringField(max_length=200, required=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    questions = ListField(StringField())
    answer_sets = EmbeddedDocumentListField(AnswerSet)

    @property
    def new_answers_count(self):
        return self.answer_sets.filter(new=True).count()


class SiteSchema(ModelSchema):
    class Meta:
        model = Site
    new_answers_count = Int(dump_only=True)
    # forms = Nested(
    #     'FormSchema',
    #     many=True,
    #     exclude=['questions', 'answer_sets']
    # )


class AnswerSetSchema(ModelSchema):
    class Meta:
        model = AnswerSet


class AnswerSchema(ModelSchema):
    class Meta:
        model = Answer
