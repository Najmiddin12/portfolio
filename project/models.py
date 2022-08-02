from django.db import models

class Card(models.Model):
    APP = "app"
    CARD = "card"
    WEB = "web"
    CATEGORY = (
        (APP, "App"),
        (CARD, "Card"),
        (WEB, "Web"),
    )

    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=50, choices=CATEGORY)
    product_picture = models.ImageField(upload_to='images/')
    product_client = models.CharField(max_length=100)
    product_date = models.DateField()
    product_url = models.URLField(max_length=300, blank=True, null=True)


class App(models.Model):
    APP = "app"
    CARD = "card"
    WEB = "web"
    CATEGORY = (
        (APP, "App"),
        (CARD, "Card"),
        (WEB, "Web"),
    )

    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=50, choices=CATEGORY)
    product_picture = models.ImageField(upload_to='images/')
    product_client = models.CharField(max_length=100)
    product_date = models.DateField()
    product_url = models.URLField(max_length=300, blank=True, null=True)

class Web(models.Model):
    APP = "app"
    CARD = "card"
    WEB = "web"
    CATEGORY = (
        (APP, "App"),
        (CARD, "Card"),
        (WEB, "Web"),
    )

    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=50, choices=CATEGORY)
    product_picture = models.ImageField(upload_to='images/')
    product_client = models.CharField(max_length=100)
    product_date = models.DateField()
    product_url = models.URLField(max_length=300, blank=True, null=True)

class Teammate(models.Model):
    teammate_name = models.CharField(max_length=100)
    teammate_photo = models.ImageField(upload_to='images/')
    teammate_job = models.CharField(max_length=100)
    teammate_twitter = models.CharField(max_length=500, blank=True, null=True)
    teammate_facebook = models.CharField(max_length=500, blank=True, null=True)
    teammate_instagram = models.CharField(max_length=500, blank=True, null=True)
    teammate_linkedln = models.CharField(max_length=500, blank=True, null=True)





















