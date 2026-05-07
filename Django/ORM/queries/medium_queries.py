# Django ORM Practice Questions - Medium

from django.db import models
from django.db.models import Max, Avg, Q, Sum, Count, F
from datetime import date


# Get all books where author name contains "ra" (case insensitive)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

output = Book.objects.select_related('author').filter(author__name__icontains='ra')

# Get department-wise average salary from employee model

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)

output = Employee.objects.values('department').annotate(avg_salary=Avg('salary'))

# Get all customers who have orders greater than 500

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()

output = Customer.objects.prefetch_related('order_set').filter(order__amount__gt=500).distinct()

# Get all customers along with their total order amount

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()

output = Customer.objects.values('name').annotate(total_amount=Sum('order__amount'))

# Get all authors along with number of books written by each author

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

output = Author.objects.values('name').annotate(number_of_books=Count('book'))

# Get employees whose department name starts with "D" and salary is greater than 50000

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

output = Employee.objects.select_related('department').filter(department__name__startswith='D', salary__gt=50000).order_by('-salary')

# Get students who scored greater than 90 in subject "Maths"

class Student(models.Model):
    name = models.CharField(max_length=100)

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()

output = Student.objects.filter(mark__subject='Maths', mark__score__gt=90).distinct()

# Get category names along with total number of products in each category

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

output = Category.objects.annotate(num_of_products=Count('product'))

# Get authors who have at least one published book

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

output = Author.objects.filter(book__published=True).distinct()

# Get customers who have NO orders

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

output = Customer.objects.filter(order__isnull=True)

# Get departments along with highest employee salary in each department

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

output = Department.objects.annotate(salaries=Max('employee__salary'))

# Get blogs which have at least 5 comments

class Blog(models.Model):
    title = models.CharField(max_length=100)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()

output = Blog.objects.annotate(comments=Count('comment')).filter(comments__gte=5)

# Get teachers who teach NO subjects

class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

output = Teacher.objects.filter(subject__isnull=True)

# Get companies having more than 10 employees

class Company(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

output = Company.objects.annotate(total_emps=Count('employee')).filter(total_emps__gt=10)

# Get customers along with their average order amount

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()

output = Customer.objects.annotate(avg_amount=Avg('order__amount'))

# Get publishers whose average book price is greater than 500

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

output = Publisher.objects.annotate(book_avgs=Avg('book__price')).filter(book_avgs__gt=500)

# Get students who have more than 5 attendance records marked as present

class Student(models.Model):
    name = models.CharField(max_length=100)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField()

output = Student.objects.annotate(student_presence=Count('attendance', filter=Q(attendance__status=True))).filter(student_presence__gt=5)

# Get all courses which have no students enrolled

class Course(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

output = Course.objects.filter(student__isnull=True)

# Get department-wise total salary from employee

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)

output = Employee.objects.values('department').annotate(total_sal=Sum('salary'))

# Get employees along with their department names

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

output = Employee.objects.select_related('department')

# Increase stock by 10 for all products in a single optimized query

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()

output = Product.objects.update(stock=F('stock') + 10)

# Increase views by 1 only for blogs where views are less than 100

class Blog(models.Model):
    title = models.CharField(max_length=100)
    views = models.IntegerField()

output = Blog.objects.filter(views__lt=100).update(views=F('views') + 1)

# Increase salary by 20% for employees whose salary is less than 50000

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

output = Employee.objects.filter(salary__lt=50000).update(salary=F('salary') * 1.2)

# Get products where sold quantity is greater than stock quantity

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    sold = models.IntegerField()

output = Product.objects.filter(sold__gt=F('stock'))

# Get students Whose marks are equal to class average marks

class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.IntegerField()

avg_marks = Student.objects.aaggregate(avg=Avg('marks'))['avg']

output = Student.objects.filter(marks=avg_marks)

# Get customers Who have more than 3 orders

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()

output = Customer.objects.annotate(customer_order=Count('order')).filter(customer_order__gt=3)

# Get authors Who have books priced greater than 1000

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

output = Author.objects.filter(book__price__gt=1000).distinct()

# Get departments Which have more than 5 employees

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

output = Department.objects.annotate(employees_in_dept=Count('employee')).filter(employees_in_dept__gt=5)

# Get customers Along with their highest order amount

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()

output = Customer.objects.annotate(highest_ord_amount=Max('order__amount'))

# Get publishers Who have no books

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

output = Publisher.objects.filter(book__isnull=True)

# Get teachers Who teach subject "Maths"

class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

output = Teacher.objects.filter(subject__name__exact='Maths')

# Get books Along with author details efficiently

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

output = Book.objects.select_related('author')

# Get students Whose average marks are greater than 80

class Student(models.Model):
    name = models.CharField(max_length=100)

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()

output = Student.objects.annotate(avg_marks=Avg('mark__score')).filter(avg_marks__gt=80)

# Get companies Which have no employees

class Company(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

output = Company.objects.filter(employee__isnull=True)

# Get departments Along with average employee salary

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

output = Department.objects.annotate(avg_emp_sal=Avg('employee__salary'))

# Get products Along with category details efficiently

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

output = Product.objects.select_related('category')

# Get authors Whose books have at least one review with rating greater than 4

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()

output = Author.objects.filter(book__review__rating__gt=4)

# Get courses Having more than 10 students enrolled

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

output = Course.objects.annotate(total_students=Count('students')).filter(total_students__gt=10)

# Get customers Whose orders contain items priced greater than 5000

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.IntegerField()

output = Customer.objects.filter(order__item__price__gt=5000)

# Get teachers Whose subjects have exams with total marks greater than 90 Avoid duplicate teachers

class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_marks = models.IntegerField()

output = Teacher.objects.filter(subject__exam__total_marks__gt=90).distinct()
