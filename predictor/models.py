from django.db import models

class Scenario(models.Model):

    attack_type = models.CharField(max_length=100)
    attack_vector = models.CharField(max_length=100)
    system_affected = models.CharField(max_length=100)
    security_level = models.CharField(max_length=50)
    downtime = models.IntegerField()
    detection_delay = models.IntegerField()
    records_compromised = models.IntegerField()
    predicted_loss = models.FloatField()

    def __str__(self):
        return self.attack_type
    

from django.db import models

class CyberScenario(models.Model):

    attack_type = models.CharField(max_length=50)
    system = models.CharField(max_length=50)
    downtime = models.IntegerField()
    records = models.IntegerField()

    predicted_loss = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.attack_type