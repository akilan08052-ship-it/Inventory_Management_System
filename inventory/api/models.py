from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Enter email")
        
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)

        return self.create_user(email,password,**extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    role_choice=(
        ('Owner','owner'),
        ('Manager','manger'),
        ("Staff","staff"),
        ('Supplier','supplier'
        '')
    )
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    email=models.EmailField(max_length=150,unique=True,null=False)
    phone_no=models.IntegerField(null=True)
    date_of_birth=models.DateField(null=True)
    role=models.CharField(max_length=100,choices=role_choice)

    def user_name(self):
        return self.first_name +" "+ self.last_name


    objects=CustomUserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]




class Product(models.Model):
    name=models.CharField(max_length=150,null=False)
    product_id=models.IntegerField(unique=True,null=True)
    catogery=models.CharField(null=False)
    stock=models.IntegerField(null=False)
    creation_date=models.DateField(auto_now_add=True)


