from django import forms


class MyFirstForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data['username']
        if username == 'benoit':
            raise forms.ValidationError('This username is not valid!')

        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if not password or not len(password):
            raise forms.ValidationError('This must be set')

        return password

    def clean(self):
        data = super(MyFirstForm, self).clean()
        if data.get('username') == 'ben' and data.get('password') == 'pass':
            self._errors['password'] = self.error_class(["Invalid password"])

        return data
