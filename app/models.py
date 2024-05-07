from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class MachineOrEquipment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MachineOrEquipment, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    machine = models.ForeignKey(MachineOrEquipment, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Exercise, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.user.username}-{self.date}")
        super(Workout, self).save(*args, **kwargs)

    def __str__(self):
        return f"Session on {self.date} by {self.user.username}"

class WorkoutExercises(models.Model):
    id = models.AutoField(primary_key=True)
    workout = models.ForeignKey(Workout, related_name='exercises', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    reps = models.IntegerField()
    weight = models.FloatField()
    sets = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.workout.id}-{self.exercise.name}")
        super(WorkoutExercises, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.exercise.name} on {self.workout.date}"
