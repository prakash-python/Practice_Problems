# marks > 50 AND name contains 'a' (case insensitive), order by marks descending
from .models import (
    Student,
    Employee,
    Author,
    Book,
    Customer,
    Product,
    User,
    Order,
    Category,
    Department,
    Blog, Comment, Teacher, Company, Publisher, Course
)

from django.db.models import Max, Avg, Q, Sum, Count, F
from datetime import date

output = Student.objects.filter(marks__gt=50, name__contains='a').order_by('marks')

# Get top 3 Student with highest marks, but return only names and marks:
output = Student.objects.values('name', 'marks').order_by('-marks')[:3]

# Get the maximum salary Only from employees in "IT" department
output = Employee.objects.filter(department__iexact='IT').order_by('salary').first()

# or second version like 
output = Employee.objects.filter(department__iexact='IT').aggregate(Max('salary'))

# Get all books Where author name contains "ra" (case insensitive)
output = Book.objects.select_related('author').filter(author__name__icontains='ra')

# Get department-wise average salary from employee model
output = Employee.objects.values('department').annotate(avg_salary=Avg('salary'))

# Get all customers Who have orders greater than 500
output = Customer.objects.prefetch_related('order_set').filter(order__amount_gt = 500).distinct()

# Get products Whose price is between 100 and 500
output = Product.objects.filter(price__range=(100,500)).order_by('price')

# Get Student Whose marks are NOT less than 35 Order by name ascending
output = Student.objects.filter(marks__gte=35).order_by('name')

# get employees Whose department is "IT" OR Salary greater than 70000
output = Employee.objects.filter(Q(department__exact='IT') | Q(salary__gt=70000))

# Get products Where stock is either less than 10 OR greater than 100
output = Product.objects.filter(Q(stock__lt=10) | Q(stock__gt=100))

# Get all customers Along with their total order amount
output = Customer.objects.values('name').annotate(total_amount=Sum('order__amount'))

# Get all authors Along with number of books written by each author
output = Author.objects.values('name').annotate(number_of_books=Count('book'))

# ORM query to check Whether any user exists With email "test@gmail.com"
output = User.objects.filter(email__exact="test@gmail.com").exists()

# Get employees Whose salary is NOT between 30000 and 50000
output = Employee.objects.exclude(salary__range=(30000,50000))

# Get only student names As a flat list
output = Student.objects.values_list('name', flat=True)

# Count total orders Where amount is greater than 1000
output = Order.objects.filter(amount__gt=1000).count()

# Get employees Whose department name starts with "D" And salary is greater than 50000
output = Employee.objects.select_related('departement').filter(department__name__startswith='D', salary__gt=50000).order_by('-salary')

# Get students Who scored greater than 90 In subject "Maths"
output = Student.objects.filter(mark__subject__exact="Maths", mark__score__gt=90).distinct()

# Get category names Along with total number of products in each category
output = Category.objects.annotate(num_of_products=Count('product'))

# Get authors Who have at least one published book
output = Author.objects.filter(book_published=True).distinct()

# Get customers who have NO orders
output = Customer.objects.filter(order__isnull=True)

# Get departments Along with highest employee salary in each department
output = Department.objects.annotate(salaries=Max('employee__salary'))  

# Get blogs Which have at least 5 comments
output = Blog.objects.annotate(comments=Count('comment')).filter(comments__gte=5)

# Get teachers Who teach NO subjects
output = Teacher.objects.filter(subject__isnull=True)

# Get companies Having more than 10 employees
output = Company.objects.annotate(total_emps=Count('employee')).filter(total_emps__gt=10)

# Get customers Along with their average order amount
output = Customer.objects.annotate(Avg('order__amount'))

# Get publishers Whose average book price is greater than 500
output = Publisher.objects.annotate(book_avgs=Avg('book__price')).filter(book_avgs__gt=500)

# Get students Who have more than 5 attendance records marked as present
output = Student.objects.annotate(student_presence=Count('attendance',filter=Q(attendence__status=True))).filter(student_presence__gt=5)

# Get all courses Which have no students enrolled
output = Course.objects.filter(student__isnull=True)

# Get department-wise total salary from employee 
output = Employee.objects.values('department').annotate(total_sal=Sum('salary'))

# Check whether a user exists Whose username starts with "admin"
output = User.objects.filter(username__startswith="admin").exists()

# Get employees Along with their department names
output = Employee.objects.select_related('department')

# Increase stock by 10 For all products In a single optimized query
output = Product.objects.update(stock = F('stock')+10)

# Increase views by 1 Only for blogs where views are less than 100
output = Blog.objects.filter(views__lt=100).update(views=F('views')+1)

# Increase salary by 20% For employees whose salary is less than 50000
output = Employee.objects.filter(salary__lt=50000).update(salary =F('salary') + F('salary')*0.2)

# Get products Where sold quantity is greater than stock quantity
output = Product.objects.filter(sold__gt = F('stock'))

# Get employees Who joined in the year 2025
output = Employee.objects.filter(joining_date__year='2025')

# Get orders Created in current month
today = date.today()
output = Order.objects.filter(created_at__month=today.month)  

# Get top 3 most expensive products
output = Product.objects.order_by('-price')[:3]