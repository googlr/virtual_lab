from django.forms import ModelForm
from django import forms
import datetime
from vital.models import Virtual_Machine_Type, Course, Virtual_Machine


class CreateCourseForm(forms.Form):
    course_name = forms.CharField(widget=forms.widgets.TextInput)
    course_number = forms.CharField(widget=forms.widgets.TextInput)
    start_date = forms.DateField(initial=datetime.date.today)
    created_date = forms.DateField(initial=datetime.date.today, widget=forms.HiddenInput())


class CreateVmsForm(ModelForm):
    class Meta:
        model = Virtual_Machine
        fields = ['name', 'type']

    def __init__(self, *args, **kwargs):
        super(CreateVmsForm, self).__init__(*args, **kwargs)
        self.fields['course'].required = False
    # vm_name = forms.CharField(widget=forms.widgets.TextInput)
    # vm_type = forms.ModelChoiceField(queryset=Virtual_Machine_Type.objects)
