from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from testapp.models import UserLoginActivity

User = get_user_model()


def log_request(request, serializer, stage):
    print(serializer.initial_data)
    user_agent_info = request.META.get("HTTP_USER_AGENT", "<unknown>")
    if stage == 1:
        try:
            user = User.objects.get(
                username=serializer.initial_data.get("username", None)
            )
        except ObjectDoesNotExist:
            user = None
    else:
        try:
            user_id = serializer.initial_data["token"].split("-")[0]
        except KeyError:
            user_id = None
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
            except ObjectDoesNotExist:
                user = None
        else:
            user = None
    print(serializer.errors)
    UserLoginActivity.objects.create(
        login_success=not bool(serializer.errors),
        user=user,
        login_username=serializer.initial_data.get("username"),
        login_IP=get_client_ip(request),
        user_agent_info=user_agent_info,
        errors=serializer.errors.values,
        stage=stage,
    )


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
