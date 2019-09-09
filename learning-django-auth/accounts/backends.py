from django.contrib.auth.models import User

class EmailAuth:
    """ Authenticate a user by email """
    
    def authenticate(self, username=None, password=None):
        """ Get instance of user based on email and password """
        
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password):
                return user
            return None
        except User.DoestNotExist:
            return None
    
    def get_user(self, user_id):
        """Used by django authentication system"""
        
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
        except User.DoestNotExist:
            return None