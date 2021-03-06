# Defining functions in R
```r
# Defined function
add_num <- function(a, b) {a + b}

# Anonymous function (No one-expression limit, and the syntax is the same.)
function(a, b) {a + b}
```

# Defining functions in Python
```python
# Defined function
# Can't be written within one line because the need of indent
def add_num(a, b):
  a + b
  
# Anonymous function (Only one expression, and use lambda.)
lambda a, b: a + b
```

## More demonstration in Python
```python
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
  return person.split()[0] + ' ' + person.split()[-1]

# Option 1
for person in people:
  print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

# Option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))
```
### R way to simulate the above solution
```r
people <- c('Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero')

# Option 1
split_people <- strsplit(people, " ")
paste_tile_and_name <- function(splits) {
  paste(splits[1], splits[length(splits)])
}
sapply(split_people, paste_tile_and_name)

# Option 2
split_title_and_name <- function(person) {
  splits <- unlist(strsplit(person, " "))
  paste(splits[1], splits[length(splits)])
}
unname(sapply(people, split_title_and_name))
```
