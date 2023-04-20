from django.db import models
# from myapp.models import User
# Create your models here.
#  createing model for user
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    hostel_name = models.CharField(max_length=50)
    is_participant = models.BooleanField(default=False)
    organiser=models.IntegerField(default=0)

    class Meta:
        db_table = "users"

class TeamRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    # game_team = models.ForeignKey(GameTeam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "team_registration"