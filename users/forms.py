from allauth.account.forms import LoginForm, PasswordField, SignupForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email',)


class MyCustomLoginForm(LoginForm):
    error_messages = {
        'account_inactive':
        _("Denne kontoen er ikke aktiv."),

        'email_password_mismatch':
        _("E-postadressen og / eller passordet du oppga er feil."),

        'username_password_mismatch':
        _("Brukernavn og / eller passordet du oppga er feil."),
    }
    password = PasswordField(label=_("Passord"))

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['placeholder'] = _('Passord')
        login_widget = forms.TextInput(attrs={'type': 'email',
                                              'placeholder': _('E-postadresse'),
                                              'autofocus': 'autofocus'})
        login_field = forms.EmailField(label=_("E-post"), widget=login_widget)
        self.fields["login"] = login_field

    def login(self, *args, **kwargs):
        return super(MyCustomLoginForm, self).login(*args, **kwargs)


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'] = PasswordField(label=_("Passord"))
        signup_widget = forms.TextInput(attrs={'type': 'email',
                                              'placeholder': _('E-postadresse'),
                                              'autofocus': 'autofocus'})
        signup_field = forms.EmailField(label=_("E-post"), widget=signup_widget)
        self.fields["email"] = signup_field


    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        return user