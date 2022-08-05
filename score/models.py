from django.db import models
from twilio.rest import Client
# Create your models here.


class Score(models.Model):
    test_result = models.PositiveBigIntegerField()


    def __str__(self):
        return str(self.test_result)

    def save(self, *args, **kwargs):
        #if test result less than 80 execut this
        if self.test_result < 80:
            #twilio code
            account_sid ='AC4794da9855891cc86ad99b95bed55417'
            auth_token ='6eb0fe0369579a3584edfdaed12045ab'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body = f'Hi, your test reuslt is  {self.test_result}. Great Job',
                from_ ='+15484890144',
                to='+15196707469'
            )

            print(message.sid)
        return super().save(*args, **kwargs)

       