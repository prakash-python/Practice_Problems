# Write a decorator that:

#  Takes a function returning a list
#  Returns only even numbers from that list

def even_filter(f):
    def exec_fun():
        lst = f()
        return [i for i in lst if i % 2 == 0]
    return exec_fun

@even_filter
def get_numbers():
    return [1, 2, 3, 4, 5, 6]

print(get_numbers())