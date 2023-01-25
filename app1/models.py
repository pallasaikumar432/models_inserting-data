from django.db import models
# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name

class webpages(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True)
    url=models.URLField()
    def __str__(self):
        return self.topic_name

class access_records(models.Model):
    name=models.ForeignKey(webpages,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)