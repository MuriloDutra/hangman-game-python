#A tuple can't be changed, it's immutable

print("\n* DAYS *")
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(f"Type: {type(days)}")
print(f"Days of the week: {days}")
print(f"Quantity of days: {len(days)}")
print(f"Maximum day: {max(days)}")
print(f"Minimum day: {min(days)}")

print("\n* PEOPLE *")
person01 = ("Murilo", 21)
person02 = ("Yasmin", 21)
people = [person01, person02]
print(f"First person name: {people[0][0]}")
print(f"First person age: {people[0][1]}")

print("\n* CONVERTING FROM LIST TO TUPLE AND VICE VERSA *")
teams = ["PSG", "Barcelona", "Real Madrid"]
tuple_teams = tuple(teams)
print(f"teams: {teams}")
print(f"tuple_teams: {tuple_teams}\n")
names = ("Murilo", "Ana", "Everson", "Camila")
names_list = list(names)
print(f"names: {names}")
print(f"names_list: {names_list}")
