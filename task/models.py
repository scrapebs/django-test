from django.db import models


class Sending_Info(models.Model):
    email_from = models.CharField(max_length=60)
    sending_status = models.BooleanField()
    created_date =  models.DateTimeField()

    def __str__(self):
        return self.email_from + ' ' + str(self.sending_status)


