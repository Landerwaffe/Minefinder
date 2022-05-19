from django import forms


class UserForm(forms.Form):
    email = forms.CharField(label="Email or Username", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'company@gmail.com'}))
    password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email or Username", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'company@gmail.com'}))
    password1 = forms.CharField(label="Password", max_length=256,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Reinput Password", max_length=256,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
