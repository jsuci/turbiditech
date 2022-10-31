from functools import wraps
from django.core.exceptions import PermissionDenied
from . models import Device, Component

def device_user_only(function):

  @wraps(function)
  def wrap(request, *args, **kwargs):

        try:
            managed_by_id = Device.objects.get(id=kwargs['device_id']).managed_by_id

            if request.user.id == managed_by_id:
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        except:
            raise PermissionDenied

  return wrap


def component_user_only(function):

    @wraps(function)
    def wrap(request, *args, **kwargs):

        try:
            managed_by_id = Component.objects.filter(id=kwargs['component_id']).values(
                'device_link__managed_by_id')[0]['device_link__managed_by_id']

            if request.user.id == managed_by_id:
                    return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        except:
            raise PermissionDenied

    return wrap