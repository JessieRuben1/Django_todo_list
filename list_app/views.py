from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task


# Create your views here.
class CustomLoginView(LoginView):
    """
    This is a class based view that is inheriting from the LoginView class.
    """
    template_name = 'list_app/index.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        """
        The function get_success_url() is a method that returns the URL of the page that the user will be redirected to
        after successfully submitting the form
        :return: The url for the tasks page.
        """
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    """
    The RegisterPage class inherits from the FormView class, and it uses the UserCreationForm form to create a new user
    """
    template_name = 'list_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        """
        The form_valid function is called when the form is submitted and valid.

        The form_valid function is called when the form is submitted and valid.

        The form_valid function is called when the form is submitted and valid.

        The form_valid function is called when the form is submitted and valid.

        The form_valid function is called when the form is submitted and valid.

        The form_valid function is called when the form is submitted and valid.

        The form_valid function is called when the form is submitted and valid.

        The form_valid function is called when the form is submitted and valid.

        The form_valid function is called when the form is submitted and valid.

        The form_valid function is called when the form is submitted and valid.

        The form_valid function is called when the form is submitted and valid.

        :param form: The form that was submitted
        :return: The super class of the RegisterPage class.
        """
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        """
        If the user is authenticated, redirect to the tasks page, otherwise, return the super class's get method
        :return: The super class of RegisterPage is being returned.
        """
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    """
    This is a list view of the Task model, and the context object name is 'tasks'.
    The context object name is the name of the variable that will be passed to the template. In this case, the template will.
    receive a variable called tasks, which will contain a list of all the tasks in the database.
    """
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        """
        We're overriding the get_context_data function of the ListView class, and adding a new key to the context dictionary
        called 'tasks' which is equal to the queryset of all tasks, but filtered by the current user
        :return: The context is being returned.
        """
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(task_complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    """
    This is a class based view that is inheriting from the DetailView class.
    """
    model = Task
    context_object_name = 'task'
    template_name = 'list_app/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    """
    Creating a new task.
    """
    model = Task
    fields = ['title', 'description', 'task_complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        """
        The form_valid function is a function that is called when the form is submitted.

        The form_valid function is a function that is called when the form is submitted.

        The form_valid function is a function that is called when the form is submitted.

        The form_valid function is a function that is called when the form is submitted.

        The form_valid function is a function that is called when the form is submitted.

        The form_valid function is a function that is called when the form is submitted.

        The form_valid function is a function that is called when the form is submitted.

        The form_valid function is a function that is called when the form is submitted.

        The form_valid function is a function that is called when the form is submitted.

        The form_valid function is a function that is called when the form is submitted.

        :param form: The form that was submitted
        :return: The form is being returned.
        """
        """
        The form_valid function is a function that is called when the form is submitted. 
        
        The form_valid function is a function that is called when the form is submitted. 
        
    # Creating a new task.
        The form_valid function is a function that is called when the form is submitted. 
        
        The form_valid function is a function that is called when the form is submitted. 
        
        The form_valid function is a function that is called when the form is submitted. 
        
        The form_valid function is a function that is called when the form is submitted. 
        
        The form_valid function is a function that is called when the form is submitted. 
        
        The form_valid function is a function that is called when the form is submitted. 
        
        The form_valid function is a function that is called when the form is submitted. 
        
        The form_valid function is a function that is called when the form is submitted.
        
        :param form: The form that was submitted
        :return: The form is being returned.
        """
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    """
    This is a view that allows a user to update a task.
    The first line of the class is the name of the class. The name of the class is TaskUpdate
    """
    model = Task
    fields = ['title', 'description', 'task_complete']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    """
    This is a view that allows a user to delete a task.
    The first line of the class is the name of the class. The name of the class is TaskDelete
    """
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
