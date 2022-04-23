"""
import random

class Human:
    '''Creation of the human object'''
    number = 0  # global class variable, starting value 0
    total_height = 0.0
    avg_height = 0.0
    def __init__(self, name, age, height, password):
        '''The arguments of the human being are defined
        (string) name: name of the person
        (int) age: the age of the person
        (float) height: height of the human being
        (string) password: password to access all properties
        '''
        Human.number += 1
        Human.total_height += height
        Human.avg_height = Human.total_height/Human.number
        self.__name = name
        self.__age = age
        self.__height = height
        self.__password = password
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        self.__age = new_age
    def greet(self):
            print('Hello, my name is', self.__name)
    def outputter(self, pw):
        if(pw == self.__password):
            print(self.__name, self.__age, self.__height)
        else:
            print("Error! Wrong password!")

human1 = Human('Tom', 26, 1.84, 'abc')#
#human1.greet()
human1.outputter('abcd')

class Programmer(Human):
    def __init__(self, name, age, height, password, prog_lang):
        Human.__init__(self, name,age, height, password)
        self.__prog_lang = prog_lang
    def get_prog_lang(self):
        return self.__prog_lang
    def set_prog_lang(self, new_prog_lang):
        self.__prog_lang = new_prog_lang

programmer1 = Programmer('Karl', 16, 1.86, 'abc', 'Python')
print(programmer1.get_prog_lang())

class LotteryPlayer:
    def __init__(self, name, numbers):
        self.__name = name
        self.__numbers = numbers
    def get_name(self):
        return self.__name
    def check_win(self, win_list):
        number_hits = 0
        for i in win_list:
            for j in self.__numbers:
                if(i == j):
                    number_hits += 1
        return number_hits

number_list = list(range(1, 50))
win_list = random.sample(number_list, 6)
print(number_list)
print(win_list)

player1 = LotteryPlayer('A', [1,3,14,36,39,45])
player2 = LotteryPlayer('B', [31, 35, 37, 44, 45, 49])
player3 = LotteryPlayer('C', [6, 9, 16, 24, 22, 46])

print(player1.get_name(), player1.check_win(win_list))
print(player2.get_name(), player2.check_win(win_list))
print(player3.get_name(), player3.check_win(win_list))
"""
from keras.applications.densenet import layers

"""
from tkinter import *

window = Tk()
window.title("Calculator")
#window.geometry('500x300')

def output():
    if check1.get():
        label2.delete(0, 'end')
        label2.insert(0, int(input1.get()) + int(input2.get()))
    if check2.get():
        label2.delete(0, 'end')
        label2.insert(0, int(input1.get()) - int(input2.get()))
    if check3.get():
        label2.delete(0, 'end')
        label2.insert(0, int(input1.get()) * int(input2.get()))
    if check4.get():
        label2.delete(0, 'end')
        label2.insert(0, int(input1.get()) / int(input2.get()))

label1 = Label(window, text='Calculator', font=('Bold', 16))
input1 = Entry(window)
input2 = Entry(window)
check1 = IntVar()
checkbox1 = Checkbutton(window, text='Plus', variable=check1)
check2 = IntVar()
checkbox2 = Checkbutton(window, text='Minus', variable=check2)
check3 = IntVar()
checkbox3 = Checkbutton(window, text='Times', variable=check3)
check4 = IntVar()
checkbox4 = Checkbutton(window, text='divided', variable=check4)
button1 = Button(window, text='Calculate', command=output)
label2 = Entry(window)

label1.grid(row=0, column=1, columnspan=2)
input1.grid(row=1, column=1)
input2.grid(row=1, column=2)
checkbox1.grid(row=2, column=0)
checkbox2.grid(row=2, column=1)
checkbox3.grid(row=2, column=2)
checkbox4.grid(row=2, column=3)
button1.grid(row=3, column=1, columnspan=2)
label2.grid(row=4, column=1, columnspan=2)

window.mainloop()
"""

from keras import *

model = Sequential()
# Input layer input must be 1
model.add(layers.Dense(units=3, input_shape=[4]))
# Interlayer
model.add(layers.Dense(units=2, input_shape=[1]))
# Output layer units must be 1
model.add(layers.Dense(units=1, input_shape=[1]))

input_list = [1,2,3,4,5]
output_list = [3,6,9,12,15]

# Creating the network (adam would be an alternative to sgd)
model.compile(loss='mean_squared_error', optimizer='sgd')

# Training the net with 1000 runs
model.fit(x=input_list, y=output_list, epochs=1000)

# Predicting the numbers
print(model.predict([6]))
print(model.predict([7]))
print(model.predict([8]))