from datetime import datetime
name = input('What is your name? \n')
age = int(input('How old are you? \n'))
hundred = int((95-age) + datetime.now().year)
print ('Hello %s. You are %s years old. You will turn 95 years old in %s.' % (name, age, hundred))
