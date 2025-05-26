from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class chaiVariety(models.Model):
    CHAI_TYPES_CHOICE = [
        ('ML', 'masala'),
        ('GR', 'ginger'),
        ('KL', 'KIVI'),
        ('EL', 'Elaichi'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    
    type = models.CharField(max_length=2, choices=CHAI_TYPES_CHOICE)

    def __str__(self):
        return self.name

# ONE TO MANY - e.g. comments on a post
class ChaiReview(models.Model):
    chai = models.ForeignKey(chaiVariety, on_delete=models.CASCADE, related_name='reviews')
    
    # Corrected to reference Django's built-in User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField()
    comment = models.TextField()
    uploadDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'

# MANY TO MANY
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    chai_varities = models.ManyToManyField(chaiVariety, related_name='stores')

    def __str__(self):
        return self.name

# ONE TO ONE
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(chaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    # Fixed incorrect attribute reference
    def __str__(self):
        return f'Certificate for {self.chai.name}'