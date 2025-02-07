from django import forms
from django.contrib.auth.models import User
from .models import Sender, Receiver, Transaction

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class SenderForm(forms.ModelForm):
    class Meta:
        model = Sender
        fields = ['address', 'date_of_birth', 'nationality', 'government_issued_id', 'contact_number']

class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = ['full_name', 'address', 'date_of_birth', 'nationality', 'government_issued_id', 'contact_number']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['receiver', 'agent', 'amount', 'currency', 'purpose']