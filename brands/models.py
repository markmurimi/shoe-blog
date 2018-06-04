from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length =30)
    brand_details = models.TextField()
    brand_owner = models.CharField(max_length = 30)
    brand_origin = models.CharField(max_length = 30)
    release_date = models.CharField(max_length =30)
    profile = models.ForeignKey('Profile', null=True)


    def __str__(self):
        return self.brand_name

class Profile(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length =30)
    profile_pic = models.ImageField(upload_to='profiles/')
    image = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length =30)
    picture = models.ImageField(upload_to='posts/')
    post_caption = models.TextField()
    price = models.IntegerField()
    brand = models.ForeignKey('Brand')
    profile = models.ForeignKey('Profile')
    released_date = models.CharField(max_length =30)
    
    def __str__(self):
        return self.name   

    @classmethod
    def get_posts(cls):
        '''
        Method that gets all image posts from the database
        Returns:
            get_posts : list of image post objects from the database
        ''' 
        images = Post.objects.all()
        return images 

    @classmethod
    def search_by_brand_name(cls,search_term):
        images = cls.objects.filter(brand__brand_name__icontains=search_term)
        return images