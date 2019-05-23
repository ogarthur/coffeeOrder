from django.core.exceptions import PermissionDenied
from .models import CustomUser,UserGroup


def is_group_admin(group_id,user_id):
    group = UserGroup.objects.get(id=group_id)

    if group.group_admin.filter(pk=user_id).exists():
        return True
    else:
        raise PermissionDenied
