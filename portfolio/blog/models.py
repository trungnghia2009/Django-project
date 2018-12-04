from django.db import models

# Create A Blog models here

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    def summary(self):
        if len(self.body) > 40:
            return self.body[:40] + '...'
        else:
            return self.body[:40]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')



# Add the Blog app to the settings

# Create a migration

# Migrate

# Add to the admin 
