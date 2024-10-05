from django.db import models
from . models import *
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models





# Custom QuerySet for Soft Delete
class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        """Override delete to perform a soft delete."""
        return self.update(deleted_at=timezone.now())

    def hard_delete(self):
        """Perform permanent delete."""
        return super().delete()

    def alive(self):
        """Return objects that are not soft-deleted."""
        return self.filter(deleted_at__isnull=True)

    def dead(self):
        """Return only soft-deleted objects."""
        return self.filter(deleted_at__isnull=False)


# Custom Manager using the SoftDeleteQuerySet
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).alive()

    def all_with_deleted(self):
        return SoftDeleteQuerySet(self.model, using=self._db)

    def deleted(self):
        return SoftDeleteQuerySet(self.model, using=self._db).dead()


# Create your models here.
class login(models.Model):
      firstname=models.CharField(max_length=256)
      lastname=models.CharField(max_length=256,null=True, blank=True)
      email=models.EmailField()
      password=models.CharField(max_length=256)
      role=models.IntegerField(default=2)
      phone=models.IntegerField(null=True, blank=True)
      whatsapp=models.IntegerField(null=True, blank=True)
      address=models.TextField(null=True, blank=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      deleted_at = models.DateTimeField(null=True, blank=True)
      
      objects = SoftDeleteManager()        
      def soft_delete(self):
            self.deleted_at = timezone.now()
            self.save()
      def restore(self):
            self.deleted_at = None
            self.save()
      def is_deleted(self):
            return self.deleted_at is not None          
      def __str__(self):
          return self.name
    #   def __str__(self):
    #     return self.name

      
class Category(models.Model):
    name = models.CharField(max_length=256)
    status = models.IntegerField(default=1)    
    created_at = models.DateTimeField(default=timezone.now)  # Temporary field without auto_now_add
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = SoftDeleteManager()        
    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()
    def restore(self):
        self.deleted_at = None
        self.save()
    def is_deleted(self):
        return self.deleted_at is not None      
    def __str__(self):
        return self.name

class projectss(models.Model) :     
        name=models.CharField(max_length=256)
        address=models.TextField(null=True, blank=True)
        amount=models.CharField(max_length=256,null=True, blank=True)
        description=models.TextField(null=True, blank=True)
        area=models.TextField(null=True, blank=True)
        location=models.CharField(max_length=500)
        cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects',null=True, blank=True)
        image = models.TextField(blank=True,null=True)
        
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        deleted_at = models.DateTimeField(null=True, blank=True)
      
        objects = SoftDeleteManager()        
        def soft_delete(self):
            self.deleted_at = timezone.now()
            self.save()
        def restore(self):
            self.deleted_at = None
            self.save()
        def is_deleted(self):
            return self.deleted_at is not None          
        def __str__(self):
            return self.name
class tbl_blogs(models.Model):
        
        name=models.CharField(max_length=100)
        slug=models.CharField(max_length=500)
        status=models.CharField(max_length=500)
        description=models.TextField(blank=True,null=True)
        metatag=models.CharField(max_length=500,blank=True,null=True)
        metakeyword=models.CharField(max_length=500,blank=True,null=True)
        metadescription=models.TextField(blank=True,null=True)
        blog_image = models.TextField(blank=True,null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        deleted_at = models.DateTimeField(null=True, blank=True)
        
        objects = SoftDeleteManager()        
        def soft_delete(self):
            self.deleted_at = timezone.now()
            self.save()
        def restore(self):
            self.deleted_at = None
            self.save()
        def is_deleted(self):
            return self.deleted_at is not None          
        def __int__(self):
            return self.id
class tbl_blog_sub(models.Model):
    blog_id = models.ForeignKey(tbl_blogs, on_delete=models.CASCADE)
    sub_title=models.TextField(max_length=255, null=True, blank=True)
    sub_title_content=models.TextField(max_length=255, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = SoftDeleteManager()        
    def soft_delete(self):
            self.deleted_at = timezone.now()
            self.save()
    def restore(self):
                self.deleted_at = None
                self.save()
    def is_deleted(self):
                return self.deleted_at is not None          
    def __str__(self):
                return self.name        
class Contactus(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(max_length=50,null=True, blank=True)
    message=models.TextField(null=True, blank=True)
    status=models.IntegerField(default=1)
    reply=models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
        
    objects = SoftDeleteManager()        
    def soft_delete(self):
            self.deleted_at = timezone.now()
            self.save()
    def restore(self):
            self.deleted_at = None
            self.save()
    def is_deleted(self):
            return self.deleted_at is not None          
    def __str__(self):
            return self.name
    
    