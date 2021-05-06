"""Sample RESTful Framework."""
from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse
from sanic.response import json
from sanic_openapi import doc

# NOTE: The URL Prefix for your backend has to be the name of the backend
blueprint = Blueprint("{{cookiecutter.project}} Backend", url_prefix="/")


@doc.summary("Hello from {{cookiecutter.backend}}!")
@blueprint.get("/")
async def hello(request: Request) -> HTTPResponse:
    """Hello World.

    Parameters
    ----------
    request : Request
        Request object from sanic app

    Returns
    -------
    HTTPResponse
    """
    return json("Hello from {{cookiecutter.backend}} 🦧")


@doc.summary("Seeder Routine")
@blueprint.get("/seeder")
async def get_seeder(request: Request) -> HTTPResponse:
    """Run Seeder Routine.

    Parameters
    ----------
    request : Request
        Request object from sanic app

    Returns
    -------
    HTTPResponse
    """
    return json()


@doc.summary("Composite Routine")
@blueprint.get("/composite")
async def get_composite(request: Request) -> HTTPResponse:
    """Run Composite Routine

    Parameters
    ----------
    request : Request
        Request object from sanic app

    Returns
    -------
    HTTPResponse
    """
    return json()