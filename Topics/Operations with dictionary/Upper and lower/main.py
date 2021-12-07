# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
words_big_and_small = {iterable.upper(): iterable.lower() for iterable in some_iterable}
print(words_big_and_small)