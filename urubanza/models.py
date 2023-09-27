from django.db import models
from django.contrib.auth.models import User



class agenda(models.Model):
   date = models.DateField()
   time = models.TimeField()
   
   def __str__(self):
       return f"{self.date} - {self.time}"

class Meta():
       verbose_name_plural = "agenda"   

class Club(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adress = models.CharField(max_length=15)
    agenda = models.ForeignKey(agenda ,null=False ,on_delete=models.PROTECT)
    style_de_danse = models.CharField(max_length=100)
    uwayishizemwo = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self): 
        return self.nom
    
    class Meta():
       verbose_name_plural = "Club"
    
class Video(models.Model):
    id = models.BigAutoField(primary_key=True)
    club = models.ForeignKey(Club ,null=False ,on_delete=models.PROTECT) 
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uwayishizemwo = models.ForeignKey(User, on_delete=models.PROTECT)

    
    class Meta():
       verbose_name_plural = "Video"   


class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta():
       verbose_name_plural = "Client"

class Booking(models.Model):
  user =  models.ForeignKey(User ,null=False ,on_delete=models.PROTECT) 
  club = models.ForeignKey(Club, on_delete=models.CASCADE)
  client = models.ForeignKey(Client, on_delete=models.CASCADE)  
  date = models.DateField()
  time = models.TimeField()

  def __str__(self):
    return f'{self.client} has booked {self.club} from {self.date} to {self.time} comfirm by {self.user} '

class Meta():
  verbose_name_plural = "Booking"


