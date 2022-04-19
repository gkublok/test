#fruit_stock = {'bananas': 12, 'apples': 10, 'mangos': 52, 'kiwis': 104}
#print(fruit_stock.items())
#input_one = input("Which stock do you want to know? ")
#print("There are " + str(fruit_stock[input_one]) + " " + input_one + " in stock")
marks = {'Math_s': 1.3, 'Math_m': 2.0, 'German_s': 2.5, 'German_m': 2.0, 'English_s': 3.0, 'English_m': 2.5}
def avg_subject(subject):
    if(subject == 'Math'):
        return (marks['Math_s'] + marks['Math_m']*2)/3
    if (subject == 'German'):
        return (marks['German_s'] + marks['German_m'] * 2) / 3
    if (subject == 'English'):
        return (marks['English_s'] + marks['English_m'] * 2) / 3

print(avg_subject('Math'))
def avg_student():
    return (avg_subject('Math') + avg_subject('German') + avg_subject('English'))/3
print(avg_student())