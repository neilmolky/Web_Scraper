# the list "meals" is already defined
# your code here
kcal_total = 0
for meal in meals:
    kcal_total += meal.get("kcal")
print(kcal_total)
