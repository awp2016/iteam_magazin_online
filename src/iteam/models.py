from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.urlresolvers import reverse
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        ShoppingCart.objects.create(user=user)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
                                password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True,
                              db_index=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    description = RichTextField()
    avatar = models.ImageField(upload_to="user")

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.firstName + " " + self.lastName

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    @property
    def get_shopping_active(self):
        return ShoppingCart.objects.get(date__isnull=True, user=self)

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_staff

    @property
    def username(self):
        return self.email

    class Meta:
        db_table = 'users'


class Product(models.Model):
    PRODUCT_GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    productName = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=PRODUCT_GENDER)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):  # __str__ for Python 3, __unicode__ for Python 2
        return self.productName

    def get_absolute_url(self):
        return reverse('product_details',
                       kwargs={'pk': self.pk})


class Image(models.Model):
    source = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):  # __str__ for Python 3, __unicode__ for Python 2
        return self.product.productName + " - " + self.source.name

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cart')
    products = models.ManyToManyField(Product, through='Order')
    date = models.DateField(blank=True, null=True)

    def getNrOrders(self):
        return len(Order.objects.filter(cart=self))


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
