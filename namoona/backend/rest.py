from sanic import Blueprint
from sanic.response import json
from sanic_openapi import doc

# NOTE: The URL Prefix for your backend has to be the name of the backend
blueprint = Blueprint("namoona", url_prefix="/namoona")


@doc.summary("Say namoon to the world!")
@blueprint.get("/")
async def hello(request):
    return json("Namoona!")
