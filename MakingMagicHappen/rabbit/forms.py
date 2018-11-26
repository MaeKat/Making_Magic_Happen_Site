from django import forms 
from django.contrib.auth.models import User 

class newUserForm(forms.Form): 
    username = forms.CharField(max_length = 150, required = True) 
    password = forms.CharField(max_length = 128, required = True) 
    email = forms.EmailField(max_length = 254, required = True) 
    first_name = forms.CharField(max_length = 30, required = False) 
    last_name = forms.CharField(max_length = 150, required = False)
    is_superuser = forms.BooleanField(required=False)

class changingUserInfoForm(forms.Form): 
    username = forms.CharField(max_length = 150, required = False) 
    password = forms.CharField(max_length = 128, required = False) 
    email = forms.EmailField(max_length = 254, required = False) 
    first_name = forms.CharField(max_length = 30, required = False) 
    last_name = forms.CharField(max_length = 150, required = False)
    is_superuser = forms.BooleanField(required=False)

"""
class usernameListForm(forms.Form):
    users = []
    for i in range(100):
        try:
            users.append(User.objects.get(id=i).username)
        except:
            pass
    print(users)
    theOneYouPick = forms.ChoiceField(choices = users)
    """