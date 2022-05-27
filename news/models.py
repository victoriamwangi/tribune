from django.db import models
import datetime as dt

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name
    def save_editor(self):
        self.save()
    def delete_editor(self):
        self.delete()
    
    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name_plural = 'Editors'
        ordering = ('first_name',)
        
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'tags'
    
class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField(max_length= 1000)
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/', null=True, blank=True)
    
    def save_articles(self):
        self.save()
    
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Articles'
    
    