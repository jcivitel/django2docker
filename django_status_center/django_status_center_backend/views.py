import json

from django.http import HttpResponse

from django_status_center_model.models import *


def conv_to_json(querry_obj):
    obj = {}
    obj["error_id"] = querry_obj.fk_error.id
    obj["impacted_systems"] = querry_obj.fk_error.impacted_systems
    obj["updates"] = {
        "id": querry_obj.id,
        "state": {
            "state_id": querry_obj.status.state,
            "state": querry_obj.status.desc,
        },
        "update_desc": querry_obj.reason,
        "timestamp": str(querry_obj.timestamp),
    }

    return obj


# Create your views here.
def export_all(request):
    my_list = []
    my_errors = error_updates.objects.all()
    for error_obj in my_errors:
        my_list.append(conv_to_json(error_obj))
    return HttpResponse(json.dumps(my_list, indent=4, sort_keys=True), content_type="application/json")


def export_category(request, cat_id):
    my_list = []
    my_errors = error_updates.objects.filter(fk_error__fk_category_id=cat_id)
    for error_obj in my_errors:
        my_list.append(conv_to_json(error_obj))
    return HttpResponse(json.dumps(my_list, indent=4, sort_keys=True), content_type="application/json")
