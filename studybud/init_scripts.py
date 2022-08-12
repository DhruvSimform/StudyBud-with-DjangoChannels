from base.models import User

def set_user_connections_count_to_zero():
    User.objects.all().update(connections_count=0)