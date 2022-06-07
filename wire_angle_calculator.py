# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:55:37 2022

@author: bonny
"""
from tkinter import *
from tkinter import Label, LabelFrame, Tk, Entry, END, Button, W
from math import cos,acos

root = Tk()
root.title('Wire Calc')
root.iconbitmap("triangle_icon.ico")

#define frame
entry_frame=LabelFrame(root, width=150, height=150, padx=10,pady=10, bg='white')
entry_frame.pack(padx=10,pady=10)

#define entry widgets
enter_depth = Entry(entry_frame, width=10, borderwidth=5)
enter_wire = Entry(entry_frame, width=10, borderwidth=5)
enter_angle = Entry(entry_frame, width=10, borderwidth=5)

#define label widgets
message_depth = Label(entry_frame, text= 'instrument depth' ,font=( ' Verdana ' , 12), bg='white')
message_wire = Label(entry_frame, text= 'wire out' ,font=( ' Verdana ' , 12), bg='white')
message_angle = Label(entry_frame, text='wire angle' ,font=( ' Verdana ' , 12), bg='white')
output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='                                                                   \n', wraplength=150, justify="center", bg='white')


#grid widgets
enter_depth.grid(row=0, column=1)
enter_wire.grid(row=1, column=1)
enter_angle.grid(row=2, column=1)
message_depth.grid(row=0, column=0)
message_wire.grid(row=1, column=0)
message_angle.grid(row=2, column=0)
output_label.grid(row=4, column=0, columnspan=2)

#insert default entry vals
enter_depth.insert(END, "0")
enter_wire.insert(END, "0")
enter_angle.insert(END, "0")

def validate_entry():
    wire_out = enter_wire.get()
    instrument_depth = enter_depth.get()
    wire_angle = enter_angle.get()

    #validate only integers were entered
    if wire_out.isnumeric() == False or instrument_depth.isnumeric() == False or wire_angle.isnumeric() == False:
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='                                                                   \n', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='all entries must be positive integers', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        
    #validate that only two values were entered
    elif int(wire_out) != 0 and int(instrument_depth) != 0 and int(wire_angle) != 0:
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='                                                                   \n', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='enter only two values', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        
    #vaidate atleast two values were entered
    elif int(instrument_depth) == 0 and int(wire_out) == 0:
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='                                                                   \n', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='enter atleast two values', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
    
    #vaidate atleast two values were entered
    elif int(instrument_depth) == 0 and int(wire_angle) == 0:
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='                                                                   \n', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='enter atleast two values', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)

    #vaidate atleast two values were entered
    elif int(wire_angle) == 0 and int(wire_out) == 0:
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='                                                                   \n', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='enter atleast two values', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)   
        
    #validate that instrument depth is not larger than wire out
    elif int(wire_out) != 0 and int(instrument_depth) > int(wire_out):
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='                                                                   \n', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        output_label = Label(entry_frame, font=( ' Verdana ' , 10), text='wire out must be larger than instrument depth', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        return
    
    #if entries pass validation, calculate output
    else:
        calculate_output()
    
def calculate_output():
    
    #get integer entries 
    wire_out = int(enter_wire.get())
    instrument_depth = int(enter_depth.get())
    wire_angle = int(enter_angle.get())
    
    #if instrument angle and wire out were entered, calculate instrument depth
    if wire_angle != 0 and wire_out != 0:
        angle_rad=float(wire_angle)*0.0174533
        depth=float(wire_out)*(cos(angle_rad))
        depth=round(depth)
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='                                                                   \n', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='instrument depth is '+str(depth)+' m', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        
    #if instrument depth and wire angle were entered, calculate wire out
    elif instrument_depth != 0 and wire_angle != 0:
        angle_rad=float(wire_angle)*0.0174533
        wire=float(instrument_depth)/(cos(angle_rad))
        wire=round(wire)
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='                                                                   \n', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='wire out is '+str(wire)+' m', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        
    #if instrument depth and wire out were entered, calculate wire angle
    elif instrument_depth != 0 and wire_out != 0:
        angle_rad=float(wire_angle)*0.0174533
        cos_ang=float(instrument_depth)/float(wire_out)
        angle=acos(cos_ang)
        angle=angle/0.0174533
        angle=round(angle)
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='                                                                   \n', wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)
        output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='angle is '+str(angle), wraplength=150, justify="center", bg='white')
        output_label.grid(row=4, column=0, columnspan=2)

def clear_values():
    #clear output label
    output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='                                                                   \n', wraplength=150, justify="center", bg='white')
    output_label.grid(row=4, column=0, columnspan=2)
    output_label = Label(entry_frame, font=( ' Verdana ' , 12), text='enter two values', wraplength=150, justify="center", bg='white')
    output_label.grid(row=4, column=0, columnspan=2)
    
    #delete entires
    enter_depth.delete(0,END)
    enter_wire.delete(0,END)
    enter_angle.delete(0,END)
    
    #insert default values of 0
    enter_depth.insert(END, "0")
    enter_wire.insert(END, "0")
    enter_angle.insert(END, "0")

#define button widgets
calc_button = Button(entry_frame, text= ' Calculate' , font=( ' Verdana ' , 12), padx=1, pady=1,command=validate_entry)
clear_button = Button(entry_frame, text= ' Clear' , font=( ' Verdana ' , 12), padx=1, pady=1,command=clear_values)

#grid buttons
calc_button.grid(row=3, column=0)
clear_button.grid(row=3, column=1, sticky =W)

root.mainloop()