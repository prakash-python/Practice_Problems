# Django ORM Practice Questions - Basic

from django.db import models
from django.db.models import Max, Avg, Q, Sum, Count, F
from datetime import date


# marks > 50 AND name contains 'a' (case insensitive), order by marks descending

class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.IntegerField()

output = Student.objects.filter(marks__gt=50, name__icontains='a').order_by('-marks')

# Get top 3 Student with highest marks, but return only names and marks

class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.IntegerField()

output = Student.objects.values('name', 'marks').order_by('-marks')[:3]

# Get the maximum salary only from employees in "IT" department

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)

output = Employee.objects.filter(department__iexact='IT').aggregate(Max('salary'))

# Get products whose price is between 100 and 500

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

output = Product.objects.filter(price__range=(100, 500)).order_by('price')

# Get students whose marks are NOT less than 35 order by name ascending

class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.IntegerField()

output = Student.objects.filter(marks__gte=35).order_by('name')

# Get employees whose department is "IT" OR salary greater than 70000

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)

output = Employee.objects.filter(Q(department__exact='IT') | Q(salary__gt=70000))

# Get products where stock is either less than 10 OR greater than 100

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()

output = Product.objects.filter(Q(stock__lt=10) | Q(stock__gt=100))

# ORM query to check whether any user exists with email "[test@gmail.com](mailto:test@gmail.com)"

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

output = User.objects.filter(email__exact='test@gmail.com').exists()

# Get employees whose salary is NOT between 30000 and 50000

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

output = Employee.objects.exclude(salary__range=(30000, 50000))

# Get only student names as a flat list

class Student(models.Model):
    name = models.CharField(max_length=100)

output = Student.objects.values_list('name', flat=True)

# Count total orders where amount is greater than 1000

class Order(models.Model):
    amount = models.IntegerField()

output = Order.objects.filter(amount__gt=1000).count()

# Check whether a user exists whose username starts with "admin"

class User(models.Model):
    username = models.CharField(max_length=100)

output = User.objects.filter(username__startswith='admin').exists()

# Get employees who joined in the year 2025

class Employee(models.Model):
    name = models.CharField(max_length=100)
    joining_date = models.DateField()

output = Employee.objects.filter(joining_date__year=2025)

# Get orders created in current month

class Order(models.Model):
    amount = models.IntegerField()
    created_at = models.DateField()

today = date.today()

output = Order.objects.filter(created_at__month=today.month, created_at__year=today.year)

# Get top 3 most expensive products

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

output = Product.objects.order_by('-price')[:3]

# Get employee with second highest salary

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

output = Employee.objects.order_by('-salary')[1:2]

# Delete all products Where stock is 0

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()

output = Product.objects.filter(stock=0).delete()

# Update salary to 60000 For employees whose salary is less than 30000

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

output = Employee.objects.filter(salary__lt=30000).update(salary=60000 )

# Get total number of students

class Student(models.Model):
    name = models.CharField(max_length=100)

output = Student.objects.count()

# Get employees Ordered by salary ascending Then by name descending

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

output = Employee.objects.order_by('salary','-name')

# Get cheapest product

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

output = Product.objects.order_by('price').first()

# Get highest marks value only

class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.IntegerField()

output = Student.objects.aggregate(highest_score=Max('marks'))['highest_score']

# Get products Whose name starts with "A" And price greater than 1000
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

output = Product.objects.filter(name__startswith='A', price__gt=1000)

# Get employees Whose name ends with "n"
class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

output = Employee.objects.filter(name__endswith='n')

# Get average product price

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

output = Product.objects.aggregate(avg_price=Avg('price'))['avg_price']

# Get students Whose marks are in: [40, 50, 60]

class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.IntegerField()

output = Student.objects.filter(marks__in=[40,50,60])

# Get employees Whose salary is between 30000 and 50000

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

output = Employee.objects.filter(salary__range=(30000, 50000))

# Check whether any product exists Whose stock is less than 5

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()

output = Product.objects.filter(stock__lt=5).exists()
