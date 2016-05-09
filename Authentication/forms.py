from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=24, required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(render_value=False))

# class SignupForm(forms.Form):
#     username = forms.CharField(max_length=24, required=True)
#     email    = forms.EmailField(max_length=64, required=True)
#     password = forms.CharField(max_length=32, widget=forms.PasswordInput(render_value=False))
#     conf_pwd = forms.CharField(label=(u'Confirm Password'), max_length=32, widget=forms.PasswordInput(render_value=False))