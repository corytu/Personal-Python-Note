# Here is a list of faculty teaching this MOOC. Write a function and apply it using map() to get a list of all faculty titles and last names.

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
  splits = person.split(' ')
  return splits[0] + splits[-1]

# list(map(split_title_and_name, people))
# Explicit priting
print(list(map(split_title_and_name, people)))


# Solution for reference
# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
#
# def split_title_and_name(person):
#     title = person.split()[0]
#     lastname = person.split()[-1]
#     return '{} {}'.format(title, lastname)
#
# list(map(split_title_and_name, people))
