from django.db import models

# Create your models here.

class User(models.Model):

    #fields
    UserID = models.CharField(MaxLength = 6, primary_key = True)
    Password = models.CharField(MaxLength = 100)
    UserFirstName = models.CharField(MaxLength = 20)
    UserLastName = models.CharField(MaxLength = 20)
    PhoneNumber = models.CharField(MaxLength = 6)
    Email = models.EmailField()
    AddressLine1 = models.CharField(MaxLength = 50)
    AddressLine2 = models.CharField(MaxLength = 50)
    City = models.CharField(MaxLength = 50)
    State = models.CharField(MaxLength = 20)
    ZipCode = models.CharField(MaxLength = 5)
    UserTypeID = models.ForeignKey('UserType.UserTypeID')
    NumBooksLost = models.IntegerField(MaxLength = 6, default=0)
    TotalFeesDue = models.IntegerField(MaxLength = 6, default = 0)


class UserType(models.Model):
    UserTypeID = models.CharField(MaxLength = 5, primary_key=True)
    UserType = models.CharField()
