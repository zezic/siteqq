from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine

from backend.api.site import SiteAPI
from backend.api.answer_set import AnswerSetAPI

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
api = Api(app)
db = MongoEngine(app)

api.add_resource(SiteAPI, '/api/sites')
api.add_resource(SiteAPI, '/api/sites/<site_id>', endpoint='site.by.id')
api.add_resource(
    AnswerSetAPI,
    '/api/sites/<site_id>/answer_sets',
    endpoint='answer_sets.by.site_id'
)
api.add_resource(
    AnswerSetAPI,
    '/api/sites/<site_id>/answer_sets/<set_id>',
    endpoint='answer_sets.by.set_id'
)
