from tkinter import *
from tkinter import ttk


#The main window where selection will be made
class Selection:
    def __init__(self, master):
        self.master = master
        self.opt = "FeetToMeters"
        
        OPTIONS =[
            "FeetToMeters",
            "FeetToMeters",
            "WeightConverter",
            "DistanceConverter"
        ]
        variable = StringVar(master)
        variable.set(OPTIONS[0])

        master.title('Converter Deluxe') #Test comment again

        mainframe = ttk.Frame(self.master, padding='80 70 110 100')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text='Select', command=self.new_window).grid(column=1, row=2, sticky=(W, E), pady=20)
        #TODO: Create an option list
        ttk.OptionMenu(mainframe, variable, *OPTIONS, command=self.func).grid(column=3, row=1, sticky=W)

    #TODO: chooses what converter to open based on selection
    def new_window(self):
        self.master.destroy() # close the current window
        self.master = Tk() # create another Tk instance
        if self.opt == 'FeetToMeters':
            self.app = FeetToMeters(self.master) # create FeetToMeters window
            self.master.mainloop()
        elif self.opt == 'WeightConverter':
            self.app = WeightConverter(self.master) # create WeightConverter window
            self.master.mainloop()
        elif self.opt == 'DistanceConverter':
            self.app = DistanceConverter(self.master) # create WeightConverter window
            self.master.mainloop()

    def func(self,value):
        #sets the value
        self.opt=value

class FeetToMeters:
    def __init__(self, master):
        #set up the window and give it a title
        self.master = master
        #setting the default selection value
        self.opt = 'Feet'
        master.title('Feet to Meters Converter')

        OPTIONS =[
            "Feet",
            "Meters",
            "Feet"
        ]
        variable = StringVar(master)
        variable.set(OPTIONS[0])

        #create the application widget; a frame that will hold content
        self.mainframe = ttk.Frame(self.master, padding='15 30 45 120')
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        #all the widgets contained in the frame and their position in the grid
        self.feet = StringVar()
        self.feet_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.feet)
        self.feet_entry.focus()
        self.feet_entry.grid(column=2, row=1, sticky=(W, E))

        self.meters = StringVar()
        ttk.Label(self.mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self.mainframe, text='Calculate', command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Button(self.mainframe, text='Back', command=self.new_window).grid(column=1, row=3, sticky=W)

        
        ttk.OptionMenu(self.mainframe, variable, *OPTIONS, command=self.func).grid(column=3, row=1, sticky=W)
        ttk.Label(self.mainframe, text='is equivalent to:').grid(column=1, row=2, sticky=E)
        ttk.Label(self.mainframe, text='Meters').grid(column=3, row=2, sticky=W)

        #shortcut for adding padding to all children rather than putting it in the grid method for each one
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        #puts cursor in field so you dont have to click on it
        self.feet_entry.focus()

        #pressing enter has the same function as clicking calculate
        self.master.bind("<Return>", self.calculate)

    #calculate function
    def calculate(self, *args):
        # for going feet to meters
        if self.opt == 'Feet':
            try:
                #gets the StringVar() feet and converts to a float
                value = float(self.feet.get())
                #sets meters variable and does the calculation
                conversion = float(round((0.3048 * value), 3))
                self.meters.set(conversion)
            except ValueError:
                pass
        #For going meters to feet
        else:
            try:
                value = float(self.feet.get())
                conversion = float(round((3.2808 * value), 3))
                self.meters.set(conversion)
            except ValueError:
                pass
    
    #updates the resulting text when selecting an option
    def func(self, value):
        #sets the value
        self.opt=value
        if self.opt == 'Feet':
            ttk.Label(self.mainframe, text='Meters', width=15).grid(column=3, row=2, sticky=W, padx=5, pady=5)
        else: 
            ttk.Label(self.mainframe, text='Feet', width=15).grid(column=3, row=2, sticky=W, padx=5, pady=5)
    
    #for going back to the main window
    def new_window(self):
        self.master.destroy() # close the current window
        self.master = Tk() # create another Tk instance
        self.app = Selection(self.master) # create Selection window
        self.master.mainloop()

class WeightConverter:
    def __init__(self, master):
        #set up the window and give it a title
        self.master = master
        #setting the default selection value
        self.opt = 'Pounds'
        master.title('Pounds to Kilogram Converter')

        OPTIONS =[
            "Pounds",
            "Kilograms",
            "Pounds"
        ]
        variable = StringVar(master)
        variable.set(OPTIONS[0])

        self.mainframe = ttk.Frame(self.master, padding='15 30 45 120')
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.weight = StringVar()
        self.weight_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.weight)
        self.weight_entry.focus()
        self.weight_entry.grid(column=2, row=1, sticky=(W, E))

        self.conv = StringVar()
        ttk.Label(self.mainframe, textvariable=self.conv).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self.mainframe, text='Calculate', command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Button(self.mainframe, text='Back', command=self.new_window).grid(column=1, row=3, sticky=W)

        ttk.OptionMenu(self.mainframe, variable, *OPTIONS, command=self.func).grid(column=3, row=1, sticky=W)
        ttk.Label(self.mainframe, text='is equivalent to:').grid(column=1, row=2, sticky=E)
        ttk.Label(self.mainframe, text='Kilograms').grid(column=3, row=2, sticky=W)

        #shortcut for adding padding to all children rather than putting it in the grid method for each one
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        #puts cursor in field so you dont have to click on it
        self.weight_entry.focus()

        #pressing enter has the same function as clicking calculate
        self.master.bind("<Return>", self.calculate)

    def calculate(self, *args):
        # for going feet to meters
        if self.opt == 'Pounds':
            try:
                #gets the StringVar() feet and converts to a float
                value = float(self.weight.get())
                #sets meters variable and does the calculation
                conversion = float(round((0.45359237 * value), 3))
                self.conv.set(conversion)
            except ValueError:
                pass
        #For going meters to feet
        else:
            try:
                value = float(self.weight.get())
                conversion = float(round((value / 0.45359237), 3))
                self.conv.set(conversion)
            except ValueError:
                pass
    
    #updates the resulting text when selecting an option
    def func(self, value):
        #sets the value
        self.opt=value
        if self.opt == 'Pounds':
            ttk.Label(self.mainframe, text='Kilograms', width=15).grid(column=3, row=2, sticky=W, padx=5, pady=5)
        else: 
            ttk.Label(self.mainframe, text='Pounds', width=15).grid(column=3, row=2, sticky=W, padx=5, pady=5)
    
    #for going back to the main window
    def new_window(self):
        self.master.destroy() # close the current window
        self.master = Tk() # create another Tk instance
        self.app = Selection(self.master) # create Selection window
        self.master.mainloop()

class DistanceConverter:
    def __init__(self, master):
        #set up the window and give it a title
        self.master = master
        #setting the default selection value
        self.opt = 'Miles'
        master.title('Distance Converter')

        OPTIONS =[
            "Miles",
            "Kilometers",
            "Miles"
        ]
        variable = StringVar(master)
        variable.set(OPTIONS[0])

        self.mainframe = ttk.Frame(self.master, padding='15 30 45 120')
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.dist = StringVar()
        self.dist_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.dist)
        self.dist_entry.focus()
        self.dist_entry.grid(column=2, row=1, sticky=(W, E))

        self.conv = StringVar()
        ttk.Label(self.mainframe, textvariable=self.conv).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self.mainframe, text='Calculate', command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Button(self.mainframe, text='Back', command=self.new_window).grid(column=1, row=3, sticky=W)

        ttk.OptionMenu(self.mainframe, variable, *OPTIONS, command=self.func).grid(column=3, row=1, sticky=W)
        ttk.Label(self.mainframe, text='is equivalent to:').grid(column=1, row=2, sticky=E)
        ttk.Label(self.mainframe, text='Kilometers').grid(column=3, row=2, sticky=W)

        #shortcut for adding padding to all children rather than putting it in the grid method for each one
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        #puts cursor in field so you dont have to click on it
        self.dist_entry.focus()

        #pressing enter has the same function as clicking calculate
        self.master.bind("<Return>", self.calculate)

    def calculate(self, *args):
        # for going miles to kilometers
        if self.opt == 'Miles':
            try:
                #gets the StringVar() feet and converts to a float
                value = float(self.dist.get())
                #sets meters variable and does the calculation
                conversion = float(round((1.60934 * value), 3))
                self.conv.set(conversion)
            except ValueError:
                pass
        #For going kilometers to miles
        else:
            try:
                value = float(self.dist.get())
                conversion = float(round((value / 1.60934), 3))
                self.conv.set(conversion)
            except ValueError:
                pass
    
    #updates the resulting text when selecting an option
    def func(self, value):
        #sets the value
        self.opt=value
        if self.opt == 'Miles':
            ttk.Label(self.mainframe, text='Kilograms', width=15).grid(column=3, row=2, sticky=W, padx=5, pady=5)
        else: 
            ttk.Label(self.mainframe, text='Miles', width=15).grid(column=3, row=2, sticky=W, padx=5, pady=5)
    
    #for going back to the main window
    def new_window(self):
        self.master.destroy() # close the current window
        self.master = Tk() # create another Tk instance
        self.app = Selection(self.master) # create Selection window
        self.master.mainloop()

def main(): 
    root = Tk()
    app = Selection(root)
    root.mainloop()

if __name__ == '__main__':
    main()