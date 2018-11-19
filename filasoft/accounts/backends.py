from django.contrib.auth.models import User

class EmailBackend(object):

    def authenticate(self,request,username=None,password = None):

        try:
            user = User.objects.get(email = username)
        except:
            return None

        return user

    def get_user(self,user_id):

        try:
            return User.objects.get(pk = user_id)
        except:
            return None