from django.contrib import admin
from .models import MachineOrEquipment, Exercise, Workout, WorkoutExercises
# Register your models here.
class MachineOrEquipmentAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'description',)
admin.site.register(MachineOrEquipment, MachineOrEquipmentAdmin)

class ExerciseAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'description', 'machine',)
admin.site.register(Exercise, ExerciseAdmin)

class WorkoutAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('date', 'user', 'notes',)
    list_filter = ('date',)
    search_fields = ('date', 'notes',)
admin.site.register(Workout, WorkoutAdmin)

class WorkoutExercisesAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('workout', 'exercise', 'reps', 'weight', 'sets',)
admin.site.register(WorkoutExercises, WorkoutExercisesAdmin)