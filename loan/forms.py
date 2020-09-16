from django import forms
from .models import Contributor, Help, Prediction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('', 'Select Gender'),
    (0, 'Male'),
    (1, 'Female')
)
CREDIT_HISTORY_CHOICES = (
    ('', 'Select Credit History'),
    (1, 'Yes'),
    (0, 'No')
)

MARRIED_CHOICE = (
('', 'Select Marital Status'),
    (0, 'yes'),
    (1, 'No')
)

EDUCATION_CHOICE = (
('', 'Select Educational Status'),
    (0, 'Graduate'),
    (1, 'Not Graduate')
)

SELF_EMPLOYED_CHOICE = (
('', 'Select Employment Status'),
    (0, 'Yes'),
    (1, 'No')
)

PROPERTY_AREA_CHOICE = (
('', 'Select Property Area'),
    (0, 'Semiurban'),
    (1, 'Urban'),
    (2, 'Rural')
)

DEPENDENTS_CHOICE = (
('', 'Select Number of Dependents'),
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3+')
)


class PredictionForm(forms.ModelForm):
    gender = forms.ChoiceField(choices= GENDER_CHOICES)
    married = forms.ChoiceField(choices= MARRIED_CHOICE)
    education = forms.ChoiceField(choices= EDUCATION_CHOICE )
    self_employed = forms.ChoiceField(choices= SELF_EMPLOYED_CHOICE)
    property_area = forms.ChoiceField(choices= PROPERTY_AREA_CHOICE)
    dependents = forms.ChoiceField(choices= DEPENDENTS_CHOICE)
    credit_history = forms.ChoiceField(choices= CREDIT_HISTORY_CHOICES)
    dependents = forms.ChoiceField(choices= DEPENDENTS_CHOICE)
    class Meta:
        model=Prediction
        fields=[
            'name',
            'gender',
            'married',
            'dependents',
            'education',
            'self_employed',
            'applicant_income',
            'coapplicant_income',
            'loan_amount_term',
            'credit_history',
            'property_area',
            'loan_amount',
            'loan_status',
            ]
    def __init__(self, *args, **kwargs):
        super(PredictionForm, self).__init__(*args, **kwargs)
        self.fields['gender'].label = 'Gender'
        self.fields['married'].label = 'Married'
        self.fields['education'].label = 'Education'
        self.fields['self_employed'].label = 'Self Employed'
        self.fields['property_area'].label = 'Property Area'
        self.fields['credit_history'].label = 'Credit History'
        self.fields['loan_amount_term'].label = 'Loan Term (Days)'
        self.fields['applicant_income'].label = 'Applicant Income'
        self.fields['coapplicant_income'].label = 'Coapplicant Income'
        self.fields['loan_amount'].label = 'Loan Amount'

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name',
                                                             'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name',
                                                             'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username',
                                                             'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'user@email.com',
                                                             'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'******',
                                                             'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'******',
                                                             'class':'form-control'}))

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

class UserLoginForm(forms.Form):
    username = forms.ChoiceField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.ChoiceField(widget=forms.PasswordInput(attrs={'placeholder':'******'}))