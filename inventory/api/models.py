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
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

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
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    def user_name(self):
        return self.first_name +" "+ self.last_name


    objects=CustomUserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
class Manager(models.Model):
    manager=models.OneToOneField(CustomUser,on_delete=models.PROTECT)
    udai_no=models.IntegerField()
    Address=models.CharField(max_length=300)
    joined_date=models.DateField(auto_now_add=True)

class Supplier(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.PROTECT)
    company_name=models.CharField(max_length=200)
    gst_number=models.CharField(max_length=30)
    city=models.CharField(max_length=90)
    state=models.CharField(max_length=90)

    cerated_at=models.DateField(auto_now_add=True)
    
    def supplier_name(self):
        return self.user.user_name()
    def email(self):
        return self.user.email
    def __str__(self):
        return self.user.user_name()
    def dob(self):
        return self.user.date_of_birth
    def phone_number(self):
        return self.user.phone_no

class Catogery(models.Model):
    category_choice=(
        ("Groceries","groceries"),
        ("Snacks","snacks"),
        ("Household","household")
    )
    name=models.CharField(max_length=100,null=False,choices=category_choice)
    description=models.TextField(max_length=200,null=True)

    def __str__(self):
        return  self.name
class Unit(models.Model):
    unit_choice=(
        ("KG","Kg",),
        ("L","l",),
        ("PK","pk"),

    )

    name=models.CharField(max_length=100)
    symbol=models.CharField(max_length=10,choices=unit_choice,unique=True)
   
    def __str__(self):
        return self.name



class Product(models.Model):
    catogery=models.ForeignKey(Catogery,on_delete=models.PROTECT)
    supplier=models.ForeignKey(Supplier,on_delete=models.PROTECT)
    unit=models.ForeignKey(Unit,on_delete=models.PROTECT)
    name=models.CharField(max_length=100)
    stock=models.IntegerField()
    selling_price=models.IntegerField()
    purchase_price=models.IntegerField()
    created_at=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name


class Purchase(models.Model):
    supplier=models.ForeignKey(Supplier,on_delete=models.PROTECT)
    date=models.DateField(auto_now_add=True)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    unit=models.ForeignKey(Unit,on_delete=models.PROTECT)
    stock=models.DecimalField(decimal_places=2,max_digits=4)
    price=models.DecimalField(decimal_places=2,max_digits=7)
    created_at=models.DateField(auto_now_add=True)


    def save(self,*args,**kwargs):
        if self.supplier:
             self.product.stock+=self.stock
             self.product.save()

        super().save(*args,**kwargs)
    

    
    def __str__(self):
        return self.product.name



    




