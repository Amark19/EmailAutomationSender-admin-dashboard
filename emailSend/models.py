from django.db import models
from django.core.exceptions import ValidationError
import smtplib
import datetime
from email.message import EmailMessage
import base64
import requests, json
# Create your models here.
class AddUserData(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=122)
    Enter_email_to_send=models.CharField(max_length=122)
    cities = models.CharField(max_length=256, choices=[('mumbai', 'mumbai'), ('delhi', 'delhi'), ('bangalore', 'bangalore'),('chennai', 'chennai'),('kolkata', 'kolkata')])
    
    def clean(self):
        if self.pk is None and self.Enter_email_to_send!="" and self.username!="" and self.cities!="": 
            self.time_of_send_mail = datetime.datetime.now();
            send_email(self.Enter_email_to_send,self.username,self.cities)
        else:
            raise ValidationError("Enter the valid details")
    def __str__(self):
        return self.username

class SuccessFullySentEmail(models.Model):
    username=models.CharField(max_length=122)
    Enter_email_to_send=models.CharField(max_length=122)
    cities = models.CharField(max_length=256)
    time_of_send_mail = models.DateTimeField()
    def __str__(self):
        return self.username

def send_email(email,username,city):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("amarkhamkar694@gmail.com", str(base64.b64decode('''S2hhbWthckFAMDI=''').decode()))

    #calculating the temperature
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    API_KEY = "5f85e6bc59c265032121d322c2e4819c"

    URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
    response = requests.get(URL)
    
    msg = EmailMessage()
    msg['Subject'] = f'Hi {username}, interested in our services'
    if response.status_code == 200:
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        
        msg.set_content(f"Your city '{city}', has an temperature of {round((temperature - 273.15),1)} degree celcius.")

        
    else:
    # showing the error message
        msg.set_content(f'could not fetch your city"s temperature')
    
    try:
        print(msg)
        s.sendmail('amarkhamkar694@gmail.com',str(email),str(msg))
        SuccessFullySentEmail.objects.create(username=username,Enter_email_to_send=email,cities=city,time_of_send_mail=datetime.datetime.now())
    except Exception as e:
        pass



