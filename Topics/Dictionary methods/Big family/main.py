# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

# Work with the 'first_family' and 'second_family' and create a new dictionary
our_family = {}
our_family.update(first_family)
our_family.update(second_family)
print(our_family)