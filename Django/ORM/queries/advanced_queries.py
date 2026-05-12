# Django ORM Practice Questions - Advanced

from django.db import models
from django.db.models import Max, Avg, Q, Sum, Count, F, OuterRef, Subquery
from datetime import date


# Get departments Whose employees are assigned to projects named "AI Project" Avoid duplicate departments

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee)

output = Department.objects.filter(employees__project__name='AI Project').distinct()

# Get students Whose courses have assignments with marks greater than 80 Avoid duplicate students

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.IntegerField()

output = Student.objects.filter(course__assignment__marks__gt=80).distinct()

# Get authors Whose total book sales amount is greater than 50000 Avoid duplicate authors

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.IntegerField()

output = Author.objects.annotate(total_book_sale_amount=Sum('book__sale__amount')).filter(total_book_sale_amount__gt=50000).distinct()


# get all customers whose successful payment amount is greater than 20000? Also make sure duplicate customers should not come in the result.

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateField()

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=20)

output = Customer.objects.filter(order__payment__status='Success', order__payment__amount__gt=20000).distinct()

# get authors whose average review rating across all their books is greater than 4.5? Also avoid duplicate authors and avoid unnecessary optimization methods.

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.FloatField()

output = Author.objects.annotate(avg_review_rate=Avg('book__review__rating')).filter(avg_review_rate__gt=4.5).distinct()


# highest paid employee from each department
class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()

max_sal_subquery = Employee.objects.filter(department=OuterRef('department')).values('departement').annotate(max_sal= Max('salary'))[:1]
output = Employee.objects.filter(salary=Subquery(max_sal_subquery))