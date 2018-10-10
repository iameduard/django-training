from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=5)
	email   = forms.EmailField(required=False,label='your e-mail id')
	message = forms.CharField(widget=forms.Textarea)
