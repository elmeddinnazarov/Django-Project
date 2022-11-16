from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    updated = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now=True)
    
    
    
    def __str__(self):
        return self.title
    
    

"""
SQL Commands  

CREATE TABLE blog_author (
    id SERIAL PRIMARY KEY, 
    title VARCHAR(100) NOT NULL
    )



CREATE TABLE blog_article (
    id SERIAL PRIMARY KEY, 
    title VARCHAR(100) NOT NULL),
    description TEXT,
    blog_author_id INT,
    updated DATE NOT NULL,
    created DATE NOT NULL,
    
    ADD CONSTRAINT fk_blog_author_id
        FOREIGN KEY (blog_author_id)
        REFERENCES blog_author(id)
        ON DELETE SET NULL
    )

"""