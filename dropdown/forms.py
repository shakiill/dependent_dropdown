# import datetime
from django import forms

from .models import Person, Subject, Department


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.none()

        # if 'department' in self.data:
        #     try:
        #         department_id = int(self.data.get('department'))
        #         self.fields['subject'].queryset = Subject.objects.filter(department_id=department_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset

        # elif self.instance.pk:
        #     self.fields['subject'].queryset = self.instance.department.subject_set.order_by('name')
