from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.IntegerField()

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField() 

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()

class Department(models.Model):
    name = models.CharField(max_length=100)

class Company(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    price = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Blog(models.Model):
    title = models.CharField(max_length=100)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()

class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)