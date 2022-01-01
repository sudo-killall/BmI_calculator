from tkinter import *

root = Tk()
root.title('BMI Calculator')
root.config(pady=10, padx=10)


def bmi_formula():
    height_meters = float(height_input.get())
    weight_kg = float(weight_input.get())
    bmi = weight_kg / height_meters ** 2
    bmi_output['text'] = round(bmi, 2)


# header label
header_title = Label(text='BMI Calculator', font=('Arial', 24, 'bold'))
header_title.grid(columnspan=3, row=0)

# height data
height_label = Label(text='Height in meters: ')
height_label.grid(column=0, row=1)

height = StringVar()
height_input = Entry(root, textvariable=height, justify='center')
height_input.grid(column=1, row=1)

# weight data
weight_label = Label(text='Weight in Kg: ')
weight_label.grid(column=0, row=2)

weight = StringVar()
weight_input = Entry(root, textvariable=weight, justify='center')
weight_input.grid(column=1, row=2)

# BMI Data
bmi_label = Label(text='BMI: ')
bmi_label.grid(column=0, row=3)

bmi_output = Label(text=0, justify='center')
bmi_output.grid(column=1, row=3)

# Calculate button
calc_btn = Button(root, text='Calculate BMI', command=bmi_formula, width=20)
calc_btn.grid(columnspan=3, row=4)

# mainloop
root.mainloop()
