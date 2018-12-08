from django.db import models


class Institute(models.Model):
    institute = models.CharField(max_length = 50)

    def __str__(self):
        return self.institute 


class PresentAddress(models.Model):

    present_address = models.CharField(max_length = 33)

    def __str__(self):
        return self.present_address


class Member_dtl(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    present_address = models.ForeignKey(PresentAddress, on_delete=models.CASCADE)

    name = models.CharField(max_length = 30)
    age = models.IntegerField()

    permanent_add = models.CharField(max_length = 30)
    photo = models.ImageField()
    video = models.FileField()

    post_date = models.DateTimeField()

    def __str__(self):
        return self.name


