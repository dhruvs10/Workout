from django.urls import path, re_path
from .views import WorkoutListView, WorkoutDetailView, workout_list, workout_detail, new_post

urlpatterns = [
    # path('workout-list/', WorkoutListView.as_view(), name='workout_list_view'),
    #re_path(r'^(?P<slug>[-\w]+)/$', WorkoutDetailView.as_view(), name='workout_detail_view'),
    path('workout-list/', workout_list, name='workout_list'),
    #re_path(r'^(?P<slug>[-\w]+)/$', workout_detail, name='workout_detail'),

    #custom admin
    path('new-post/', new_post, name='new_post')
]
