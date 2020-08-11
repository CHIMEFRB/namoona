from sanic import Blueprint
from sanic.response import json
from sanic_openapi import doc

# NOTE: The URL Prefix for your backend has to be the name of the backend
blueprint = Blueprint(
    "{{cookiecutter.backend}}", url_prefix="/{{cookiecutter.backend}}"
)


@doc.summary("Hello from {{cookiecutter.backend}}!")
@blueprint.get("/")
async def hello(request):
    return json("Hello from {{cookiecutter.backend}} 🦧")
