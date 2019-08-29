from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person, Subject
from .forms import PersonCreateForm

# Create your views here. 
def load_subjects(request):
    department_id = request.GET.get('department')
    subjects = Subject.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'subject_dropdown_list_options.html', {'subjects': subjects})


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'person_list.html'

class PersonCreateView(CreateView):
    model = Person 
    form_class = PersonCreateForm
    template_name = 'person.html'
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    fields = ('name', 'birthdate', 'department', 'subject')
    success_url = reverse_lazy('person_changelist')


    
