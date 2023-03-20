from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField( max_length=254)

    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.fullname()

class Tag(models.Model):
    tag=models.CharField(max_length=20)
    def __str__(self):
        return self.tag


   
class Blog(models.Model):
    title =models.CharField(max_length=100)
    excerpt=models.TextField(max_length=500)
    image=models.ImageField(upload_to='Blogs',null=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,related_name='blogs',null=True)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    tags=models.ManyToManyField(Tag,related_name='blogs')
    content=models.TextField(validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user_name=models.CharField(max_length=50)
    emailid=models.EmailField(max_length=254)
    comment=models.TextField(max_length=400)
    post=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments') 
    
