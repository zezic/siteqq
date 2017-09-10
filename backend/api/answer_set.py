from flask import request
from flask_restful import Resource
from backend.models import (
    Site,
    AnswerSet,
    AnswerSetSchema
)


class AnswerSetAPI(Resource):
    def get(self, site_id, set_id=None):
        if set_id:
            return AnswerSetSchema().dump(
                AnswerSet.objects.get(id=set_id)
            ).data
        answer_sets = Site.objects.get(id=site_id).answer_sets
        return AnswerSetSchema(many=True).dump(answer_sets).data

    def post(self, site_id):
        data = request.get_json()
        site = Site.objects.get(id=site_id)
        site.answer_sets.append(AnswerSet(**data))
        site.save()
        return {}

    def patch(self, site_id, set_id):
        data = request.get_json()
        site = Site.objects.get(id=site_id)
        answer_set = site.answer_sets.get(_id=set_id)
        for field in data:
            setattr(answer_set, field, data.get(field))
        site.save()
        return {}

    def delete(self, site_id, set_id=None):
        site = Site.objects.get(id=site_id)
        if not set_id:
            site.answer_sets.delete()
        else:
            site.answer_sets.filter(_id=set_id).delete()
        site.save()
        return {}
