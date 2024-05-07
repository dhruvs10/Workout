from re import A
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db import connection

from .models import Workout
from .forms import WorkoutForm

# Create your views here.

def get_workouts_by_user(username):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT workout.id, workout.date, workout.notes, user.username
            FROM app_workout workout
            JOIN auth_user user ON workout.user_id = user.id
            WHERE user.username = %s
            ORDER BY workout.date
        """, [username])
        rows = cursor.fetchall()
    return [{'id': row[0], 'date': row[1], 'notes': row[2], 'username': row[3]} for row in rows]


class WorkoutListView(ListView):
    
    model = Workout

    def get_context_data(self, **kwargs):
        context = super(WorkoutListView, self).get_context_data(**kwargs)
        return context

class WorkoutDetailView(DetailView):

    model = Workout

    def get_context_data(self, **kwargs):
        context = super(WorkoutDetailView, self).get_context_data(**kwargs)
        return context

def workout_list(request):
    filter_type = request.GET.get('filter', None)
    selected_date = request.GET.get('date', None)

    dates = Workout.objects.order_by('date').values_list('date', flat=True).distinct()

    if filter_type == 'user':
        object_list = get_workouts_by_user('test')
    elif selected_date:
        parsed_date = parse_date(selected_date)
        if parsed_date:
            object_list = Workout.objects.filter(date=parsed_date).order_by('date')
        else:
            object_list = Workout.objects.none()
    else:
        object_list = Workout.objects.all().order_by('date')

    context = {
        'object_list': object_list,
        'dates': dates,
        'selected_date': selected_date,
        'filter_type': filter_type
    }
    return render(request, 'app/workout_list.html', context)


def workout_detail(request, slug):
    template = 'app/workout_detail.html'

    workout = get_object_or_404(Workout, slug = slug)
    context = {
        'workout': workout,
    }
    return render(request, template, context)

def new_post(request):
    template = 'app/new_post.html'
    form = WorkoutForm(request.POST or None)

    if form.is_valid():
        form.save()
    else: 
        form = WorkoutForm()
    
    context = {
        'form':form,
    }

    return render(request, template, context)
