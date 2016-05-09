from django import forms

class ClerkLog(forms.Form):
    clerk_name = forms.CharField(max_length=64, required=True)
    entry_subject = forms.CharField(max_length=256, required=True)
    phone_number = forms.NumberInput()
    description = forms.Textarea()
    # date
    prostaff = forms.CharField(max_length=64)
    radvisor = forms.CharField(max_length=64)

