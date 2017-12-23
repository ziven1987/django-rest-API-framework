from channels import Group
from django.shortcuts import render_to_response


def index(request):
    Group("chat").send({
        "text": "dfasdfs",
    })
    return render_to_response('index.html')
