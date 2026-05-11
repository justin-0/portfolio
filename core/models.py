from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    headline = models.CharField(max_length=200, help_text="Short description like 'Full Stack Developer'")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.URLField(blank=True, null=True, help_text="Direct link to your resume (Google Drive, Dropbox, etc.)")
    contact_email = models.EmailField()
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Tools', 'Tools / Other'),
    )
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Frontend')
    order = models.IntegerField(default=0, help_text="Order in which it appears")

    def __str__(self):
        return f"{self.name} ({self.category})"
    
    class Meta:
        ordering = ['order', 'name']

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(max_length=200, help_text="Comma separated e.g. Django, React, PostgreSQL")
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Certificate(models.Model):
    title = models.CharField(max_length=150)
    issuer = models.CharField(max_length=100)
    date_issued = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    certificate_url = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['order']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"
