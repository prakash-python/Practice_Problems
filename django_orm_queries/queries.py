# marks > 50 AND name contains 'a' (case insensitive), order by marks descending
Students = None
output = Students.objects.filter(marks__gt=50, name__contains='a').order_by('marks')

# Get top 3 students with highest marks, but return only names and marks:
output = Students.objects.values('name', 'marks').order_by('-marks')[:3]