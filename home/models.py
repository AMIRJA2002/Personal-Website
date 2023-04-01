from django.db import models


class PDFUpload(models.Model):
    file = models.FileField(upload_to="media/pdf")

    def __str__(self):
        return self.file.name



class AboutMe(models.Model):
    image = models.ImageField(upload_to='media/profile', blank=True, null=True)
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    experience_years = models.CharField(max_length=2)
    completed_project = models.CharField(max_length=4)
    about_me = models.TextField(max_length=5000)

    class Meta:
        verbose_name = 'about me'
        verbose_name_plural = 'about me'

    def __str__(self):
        return f'{self.name}, {self.job_title}'


class Ability(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    name2 = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Abilities'
        verbose_name_plural = 'Abilities'

    def __str__(self):
        if not self.name:
            return self.name2
        if not self.name2:
            return self.name
        if self.name and self.name2:
            return f'{self.name}, {self.name2}'


class WhatIOffer(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}, {self.description[40]}'



class MyOfferHints(models.Model):
    offer = models.ForeignKey(WhatIOffer, related_name='offers', on_delete=models.CASCADE)
    topic = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.offer}, {self.topic}'


class App(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to='media/img/')

    def __str__(self):
        return f'{self.title} {self.link}'



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=400)
    text = models.TextField(max_length=5000)

    def __str__(self):
        return f'{self.name}, {self.email}'


class WhoAmIPicture(models.Model):
    image = models.ImageField(upload_to='media/img')

    def __str__(self):
        return self.image.name
