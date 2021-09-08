from tkinter import *
from tkinter import ttk

#The main window where selection will be made
class Selection:
    def __init__(self, master):
        self.master = master
        
        master.title('Converter Deluxe')

        mainframe = ttk.Frame(self.master, padding='80 70 110 100')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text='Select', command=self.new_window).grid(column=1, row=2, sticky=(W, E), pady=20)
        #TODO: Create an option list
        ttk.Label(mainframe, text='Filler').grid(column=1, row=1, sticky=(W, E), pady=20)

    #TODO: chooses what converter to open based on selection
    def new_window(self):
        self.master.destroy() # close the current window
        self.master = Tk() # create another Tk instance
        self.app = FeetToMeters(self.master) # create FeetToMeters window
        self.master.mainloop()

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

        
        info = ttk.OptionMenu(self.mainframe, variable, *OPTIONS, command=self.func).grid(column=3, row=1, sticky=W)
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
            ttk.Label(self.mainframe, text='Meters', width=15).grid(column=3, row=2, sticky=W)
        else: 
            ttk.Label(self.mainframe, text='Feet', width=15).grid(column=3, row=2, sticky=W)
    
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