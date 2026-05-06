# Django ORM Practice Questions with Independent Models

from django.db import models
from django.db.models import Max, Avg, Q, Sum, Count, F
from datetime import date

---

# marks > 50 AND name contains 'a' (case insensitive), order by marks descending

class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.IntegerField()

output = Student.objects.filter(marks__gt=50, name__icontains='a').order_by('-marks')

---

# Get top 3 Student with highest marks, but return only names and marks

class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.IntegerField()

output = Student.objects.values('name', 'marks').order_by('-marks')[:3]

---

# Get the maximum salary only from employees in "IT" department

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)

output = Employee.objects.filter(department__iexact='IT').aggregate(Max('salary'))

---

# Get all books where author name contains "ra" (case insensitive)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

output = Book.objects.select_related('author').filter(author__name__icontains='ra')

---

# Get department-wise average salary from employee model

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)

output = Employee.objects.values('department').annotate(avg_salary=Avg('salary'))

---

# Get all customers who have orders greater than 500

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()

output = Customer.objects.prefetch_related('order_set').filter(order__amount__gt=500).distinct()

---

# Get products whose price is between 100 and 500

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

output = Product.objects.filter(price__range=(100, 500)).order_by('price')

---

# Get students whose marks are NOT less than 35 order by name ascending

class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.IntegerField()

output = Student.objects.filter(marks__gte=35).order_by('name')

---

# Get employees whose department is "IT" OR salary greater than 70000

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)

output = Employee.objects.filter(Q(department__exact='IT') | Q(salary__gt=70000))

---

# Get products where stock is either less than 10 OR greater than 100

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()

output = Product.objects.filter(Q(stock__lt=10) | Q(stock__gt=100))

---

# Get all customers along with their total order amount

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()

output = Customer.objects.values('name').annotate(total_amount=Sum('order__amount'))

---

# Get all authors along with number of books written by each author

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

output = Author.objects.values('name').annotate(number_of_books=Count('book'))

---

# ORM query to check whether any user exists with email "[test@gmail.com](mailto:test@gmail.com)"

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

output = User.objects.filter(email__exact='test@gmail.com').exists()

---

# Get employees whose salary is NOT between 30000 and 50000

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

output = Employee.objects.exclude(salary__range=(30000, 50000))

---

# Get only student names as a flat list

class Student(models.Model):
    name = models.CharField(max_length=100)

output = Student.objects.values_list('name', flat=True)

---

# Count total orders where amount is greater than 1000

class Order(models.Model):
    amount = models.IntegerField()

output = Order.objects.filter(amount__gt=1000).count()

---

# Get employees whose department name starts with "D" and salary is greater than 50000

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

output = Employee.objects.select_related('department').filter(department__name__startswith='D', salary__gt=50000).order_by('-salary')

---

# Get students who scored greater than 90 in subject "Maths"

class Student(models.Model):
    name = models.CharField(max_length=100)

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()

output = Student.objects.filter(mark__subject='Maths', mark__score__gt=90).distinct()

---

# Get category names along with total number of products in each category

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

output = Category.objects.annotate(num_of_products=Count('product'))

---

# Get authors who have at least one published book

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

output = Author.objects.filter(book__published=True).distinct()

---

# Get customers who have NO orders

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

output = Customer.objects.filter(order__isnull=True)

---

# Get departments along with highest employee salary in each department

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

output = Department.objects.annotate(salaries=Max('employee__salary'))

---

# Get blogs which have at least 5 comments

class Blog(models.Model):
    title = models.CharField(max_length=100)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()

output = Blog.objects.annotate(comments=Count('comment')).filter(comments__gte=5)

---

# Get teachers who teach NO subjects

class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

output = Teacher.objects.filter(subject__isnull=True)

---

# Get companies having more than 10 employees

class Company(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

output = Company.objects.annotate(total_emps=Count('employee')).filter(total_emps__gt=10)

---

# Get customers along with their average order amount

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()

output = Customer.objects.annotate(avg_amount=Avg('order__amount'))

---

# Get publishers whose average book price is greater than 500

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

output = Publisher.objects.annotate(book_avgs=Avg('book__price')).filter(book_avgs__gt=500)

---

# Get students who have more than 5 attendance records marked as present

class Student(models.Model):
    name = models.CharField(max_length=100)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField()

output = Student.objects.annotate(student_presence=Count('attendance', filter=Q(attendance__status=True))).filter(student_presence__gt=5)

---

# Get all courses which have no students enrolled

class Course(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

output = Course.objects.filter(student__isnull=True)

---

# Get department-wise total salary from employee

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)

output = Employee.objects.values('department').annotate(total_sal=Sum('salary'))

---

# Check whether a user exists whose username starts with "admin"

class User(models.Model):
    username = models.CharField(max_length=100)

output = User.objects.filter(username__startswith='admin').exists()

---

# Get employees along with their department names

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

output = Employee.objects.select_related('department')

---

# Increase stock by 10 for all products in a single optimized query

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()

output = Product.objects.update(stock=F('stock') + 10)

---

# Increase views by 1 only for blogs where views are less than 100

class Blog(models.Model):
    title = models.CharField(max_length=100)
    views = models.IntegerField()

output = Blog.objects.filter(views__lt=100).update(views=F('views') + 1)

---

# Increase salary by 20% for employees whose salary is less than 50000

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

output = Employee.objects.filter(salary__lt=50000).update(salary=F('salary') * 1.2)

---

# Get products where sold quantity is greater than stock quantity

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    sold = models.IntegerField()

output = Product.objects.filter(sold__gt=F('stock'))

---

# Get employees who joined in the year 2025

class Employee(models.Model):
    name = models.CharField(max_length=100)
    joining_date = models.DateField()

output = Employee.objects.filter(joining_date__year=2025)

---

# Get orders created in current month

class Order(models.Model):
    amount = models.IntegerField()
    created_at = models.DateField()

today = date.today()

output = Order.objects.filter(created_at__month=today.month, created_at__year=today.year)

---

# Get top 3 most expensive products

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

output = Product.objects.order_by('-price')[:3]

---

# Get employee with second highest salary

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

output = Employee.objects.order_by('-salary')[1:2]
