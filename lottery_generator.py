# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:nomarker
#     text_representation:
#       extension: .py
#       format_name: nomarker
#       format_version: '1.0'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %config Completer.use_jedi = False

import tkinter as tk

import numpy as np

# Start a random number generator using standard bit generator.
rng = np.random.default_rng()

# Choose a random array of 6 numbers (default), 0-50 exclusively,
# without replacing the sample. Sort the array and return it.
def get_nums(n=6, rng=rng):
    rand_nums = rng.choice(range(1, 50), n, False)
    ordered_num = np.sort(rand_nums)
    
    return ordered_num


# Use the generated numbers and assign a colour based on the 
# dictionary of colours. Return a list of lists.
def get_num_colour():
    numbers = get_nums()
    
    colour_list = []
    
    colour_limits = {
        10: 'grey',
        20: 'blue',
        30: '#AE388B',
        40: 'green',
        50: 'yellow'
    }
    
    for num in numbers:
        for limit in colour_limits.keys():
            if num < limit:
                colour_list.append([num, colour_limits[limit]])
                break
    return colour_list


# Function to be called by tkinter, on button press, to display
# selected numbers with their assigned colours.
def show_numbers():
    for widget in nums_frame.winfo_children():
        widget.destroy()
        
    colour_list = get_num_colour()
    
    for x in colour_list:
        label = tk.Label(nums_frame, text=f'{x[0]}', fg=f'{x[1]}', bg='black', font=('courier', 35))
        label.pack(side='left', ipadx=20)


# Create instance of tkinter 
root = tk.Tk()

# Create a frame to place the title in.
title_frame = tk.Frame(root)
title_frame.pack()

# Add title to the title_frame.
title = tk.Label(title_frame, text='Your winning numbers are!', font=('courier', 35))
title.pack()

# Add a frame to display the genererated lottery numbers.
nums_frame = tk.Frame(root, bg='black')
nums_frame.pack()

# Create button to call show_numbers function.
show_num = tk.Button(title_frame, text='Show Lottery Numbers', padx=1, pady=5, fg='white', bg='blue', command=show_numbers)
show_num.pack()

# Create button that exits the tkinter window.
exit = tk.Button(title_frame, text='Exit', padx=1, pady=5, fg='white', bg='blue', command=root.destroy)
exit.pack(ipadx=50)

root.mainloop()
