from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField



class Builder(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)  # 1BHK, 2BHK, etc

    def __str__(self):
        return self.name

class Flat(models.Model):
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=20, help_text="Example: 45 Lac, 56 Lac, 1 Cr, 2.5 Cr")

    image = ResizedImageField(
            size=[800, 600],
            quality=75,
            upload_to='flats/images/',
            force_format='WEBP'
        )

    blueprint = ResizedImageField(
                size=[1000, 800],
                quality=75,
                upload_to='flats/blueprints/',
                force_format='WEBP', blank=True, null=True
            )


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    


# Independent Table which i will be use for future analytics

class Lead(models.Model):
    BUILDER_CHOICES = (
        ('RUNWAL', 'Runwal'),
        ('SAI PARADISE', 'Sai Paradise'),
        ('LODHA', 'Lodha'),
        ('OTHER', 'Other'),
    )

    FLAT_CHOICES = (
        ('1BHK', '1BHK'),
        ('1.5BHK', '1.5BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
    )

    PURPOSE_CHOICES = (
        ('RENT', 'Rent'),
        ('RESALE', 'Resale'),
        ('NEW', 'New'),
    )

    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    builder = models.CharField(max_length=50, choices=BUILDER_CHOICES, blank=True, null=True)
    other_builder = models.CharField(max_length=100, blank=True, null=True)

    flat_type = models.CharField(max_length=20, choices=FLAT_CHOICES, default='1BHK')
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, default='NEW')

    source = models.CharField(max_length=50, default='dashboard')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


class Campaign(models.Model):
    STATUS_CHOICES = (
        ('SCHEDULED', 'Scheduled'),
        ('RUNNING', 'Running'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    )

    message = models.TextField()
    scheduled_time = models.DateTimeField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SCHEDULED')

    total_leads = models.IntegerField(default=0)
    sent_count = models.IntegerField(default=0)
    failed_count = models.IntegerField(default=0)

    executed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Campaign {self.id} - {self.status}"


# Table for Resale flat not related with new flat or any other table

class ResaleFlat(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=20, help_text="Example: 45 Lac, 56 Lac, 1 Cr, 2.5 Cr")
    image = models.ImageField(upload_to='resale/images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RentFlat(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    deposite = models.DecimalField(max_digits=12, decimal_places=2, default=50000)
    monthly_rent = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='rent/images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
