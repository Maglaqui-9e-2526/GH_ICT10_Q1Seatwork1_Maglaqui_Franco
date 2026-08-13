from pyscript import display, document


name = 'Franco Ethan S. Maglaqui' #String
age = 15 #Integer
height67 = 162.56 #Float-Point
countr1es = ['Switzerland', 'Alaska', 'France'] #List
student_type = False #Boolean
color = {'Color': 'Purple'} #Dictionary
car_brand = {'car_brand':'Mitsuoka'} #Dictionary
shoe_size = {'shoe_size': '6.5'} #Dictionary
best_friend = {'best_friend': 'Joel'} #Dictionary
fruity = {'Banana', 'Mango', 'Apple', 'Grapes', 'Pomelo'} #Set
six_or_seven_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') #Tuple

display(f'Hello my name is {name}. I am {age} years old. My height is {height67}cm. Am I a new student {student_type}. The countries I want to visit are {countr1es}. My favorite color is {color["Color"]}. The car brand I like is {car_brand["car_brand"]}, my shoes size is {shoe_size['shoe_size']}, and my best friend is {best_friend["best_friend"]}. My favorite fruits are {fruity}. The days of the week are {six_or_seven_days}.', target='result')
document.getElementById('result').innerHTML = f'Hello my name is {name}. I am {age} years old. My height is {height67}cm. Am I a new student {student_type}.The countries I want to visit are {countr1es}. My favorite color is {color["Color"]}. The car brand I like is {car_brand["car_brand"]}, my shoes size is {shoe_size['shoe_size']}, and my best friend is {best_friend["best_friend"]}. My favorite fruits are {fruity}. The days of the week are {six_or_seven_days}.'