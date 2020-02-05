from django.db import models

## How to create models

# Create a blog model

class Blog(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

# Add the blog app to the settings

# Create a migration

# Migrate

# Add to the admin