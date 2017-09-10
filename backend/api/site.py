from flask import request
from flask_restful import Resource
from backend.models import Site, SiteSchema


class SiteAPI(Resource):
    def get(self, site_id=None):
        if not site_id:
            return SiteSchema(
                many=True,
                exclude=['answer_sets']
            ).dump(Site.objects).data
        site = Site.objects.get(id=site_id)
        if not site:
            return {}, 404
        return SiteSchema(
            exclude=['answer_sets']
        ).dump(site).data

    def post(self):
        data = request.get_json()
        site = Site(**data).save()
        return SiteSchema().dump(site).data

    def patch(self, site_id):
        data = request.get_json()
        schema = SiteSchema()
        loaded = schema.load(data).data
        site = Site.objects.get(id=site_id)
        for field in loaded:
            print(field)
            setattr(site, field, data.get(field))
        site.save()
        return {}

    def delete(self, site_id=None):
        if not site_id:
            Site.objects.delete()
            return {}
        site = Site.objects.get(id=site_id)
        if not site:
            return {}, 404
        site.delete()
        return {}
