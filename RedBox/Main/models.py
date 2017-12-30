
# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,db_index=True)
    #slug = models.SlugField(max_length=200,db_index=True, unique=True)
    #created_at = models.DateTimeField(auto_now_add=True) # fetches and stores the current date and time
    #updated_at = models.DateTimeField(auto_now=True) # fetches and stores the latest date and time

    class Meta:
        db_table = 'categories' # to maually name the database table. if not mentioned the db table will be named [app_name]_[model_name]
        #ordering = ['-created_at'] #reverse sort order
        verbose_name_plural = 'Categories' #django adds an s at the end of the word to make it plural in admin interface.

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[str(self.id)])


class Product(models.Model):
    name = models.CharField(max_length=100)
    #slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField()
    IMDB_rating = models.FloatField(default=0.0,blank=True)
    image = models.ImageField()
    price = models.DecimalField(max_digits=9, decimal_places=2,default=0.0)
    #quantity = models.IntegerField(default=0)
    Director = models.CharField(max_length=100, blank=True)
    Actors = models.TextField(max_length=255,blank=True)
    Genre = models.CharField(max_length=100)
    Sub_titles = models.CharField(max_length=200,blank=True)
    trailer = models.CharField(max_length=150, default=None, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)  # fetches and stores the current date and time
    updated_at = models.DateTimeField(auto_now=True)
    sort = (
        ('ascending', 'A-Z'),
        ('Hr', 'Highest Rating'),
    )
    choices = models.CharField(max_length=9, choices=sort, default='ascending')

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie_detail',args= [str(self.id)])



