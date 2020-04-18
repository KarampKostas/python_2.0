from django import forms

from .models import Student
from django.contrib.auth import authenticate

class StudentForm(forms.ModelForm):
    first_name = forms.CharField(label='First name',widget=forms.TextInput(attrs={"placeholder":"Your first name"}))
    last_name = forms.CharField(label='Last name',widget=forms.TextInput(attrs={"placeholder":"Your last name"}))
    email = forms.EmailField()
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={"placeholder":"username"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={"placeholder":"password"}))
    school = forms.CharField(label='School',widget=forms.TextInput(attrs={"placeholder":"Your school"}))
    
    #αν σαν ορισμα στην πανω κλαση περασω μονο το forms.Form την Meta δεν την χρειαζομαι
    class Meta:
        model = Student
        fields = [

            'first_name',
            'last_name',
            'username',
            'school',
            'age',
            'email',
            'password',
            'password1'

        ]

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        #if not email.endswith("gr"):
        if not "@" in email: 
            raise forms.ValidationError("This is not a valid email")
        return email
    def clean_password(self,*args,**kwargs):
        password = self.cleaned_data.get("password")
        confpassword = self.cleaned_data.get("password1")
        if password != confpassword:
            raise forms.ValidationError("Passwords does not match")
        return password
         

class LoginStudentForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={"placeholder":"username"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # class Meta:
    #     model = Student
    #     fields = ['username','password' ]
    #     # username = forms.CharField()
    #     # password = forms.CharField(widget=forms.PasswordInput)
    

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            elif not user.check_password(password):
                raise forms.ValidationError('Incorrect password')

        return super(LoginStudentForm, self).clean(*args, **kwargs)



 

