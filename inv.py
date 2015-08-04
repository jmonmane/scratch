################################################################################
#MPPInventory.py
#
#Purpose:  An inventory database interface for adding and modifying product
#   information.
#
#Author:  Cody Jackson
#Date:  12/1/06
#
#Copyright 2006 Cody Jackson
#This program is free software; you can redistribute it and/or modify it 
#under the terms of the GNU General Public License as published by the Free 
#Software Foundation; either version 2 of the License, or (at your option) 
#any later version.
#
#This program is distributed in the hope that it will be useful, but 
#WITHOUT ANY WARRANTY; without even the implied warranty of 
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#General Public License for more details.
#
#You should have received a copy of the GNU General Public License 
#along with this program; if not, write to the Free Software Foundation, 
#Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#----------------------------------------------------------------------
#Version 0.4
#   Added ability to update product entry
#   Removed button instructions
#Version 0.3
#   Added MultiListbox class for inventory display
#   Removed text box display area
#   Updated display area methods to work with MultiListbox
#Version 0.2
#   Added "Delete Item" functionality
#   Added instructions
#   Added text box scrollbar
#Version 0.1
#   Initial build
######################################################################
#TODO: sort items by product number
#TODO: add printing ability

#!/usr/bin/env python

from Tkinter import *
from tkMessageBox import *
from MultiListBox import MultiListbox
import shelve

shelvename = "inventory.slv"

class ProductEntry(Frame):
    """Interface for product entry."""
    
    def __init__(self, parent = None):
        """Create, pack, and bind entry boxes and buttons for product entry."""
        
        Frame.__init__(self)
        self.pack()
        self.master.title("Product Inventory Entry")
        
        #---Instructions
        self.instructionFrame = Frame(self)
        self.instructionFrame.pack()
        
        Label(self.instructionFrame, text = "Enter the product information below.  Each product number must be unique.").pack()
        
        #---Entry boxes and column headers
        self.entryFrame = Frame(self)
        self.entryFrame.pack()
        
        #---Column headings
        self.col1 = Label(self.entryFrame, text = "Product Number")
        self.col1.grid(row = 0, column = 0)
        
        self.col2 = Label(self.entryFrame, text = "Description")
        self.col2.grid(row = 0, column = 1)
        
        self.col3 = Label(self.entryFrame, text = "Color")
        self.col3.grid(row = 0, column = 2)
        
        self.col4 = Label(self.entryFrame, text = "Unit cost")
        self.col4.grid(row = 0, column = 3)
        
        self.col5 = Label(self.entryFrame, text = "Selling price")
        self.col5.grid(row = 0, column = 4)
        
        self.col6 = Label(self.entryFrame, text = "Quantity")
        self.col6.grid(row = 0, column = 5)
        
        #---Entry boxes
        self.prodNum = Entry(self.entryFrame, name = "prodNum")
        self.prodNum.grid(row = 1, column = 0)
        
        self.description = Entry(self.entryFrame, name = "description")
        self.description.grid(row = 1, column = 1)
        
        self.color = Entry(self.entryFrame, name = "color")
        self.color.grid(row = 1, column = 2)
        
        self.userCost = Entry(self.entryFrame, name = "cost")
        self.userCost.grid(row = 1, column = 3)
        
        self.sellPrice = Entry(self.entryFrame, name = "price")
        self.sellPrice.grid(row = 1, column = 4)
        
        self.quantity = Entry(self.entryFrame, name = "quantity")
        self.quantity.grid(row = 1, column = 5)
        
        #---Product entry buttons
        self.entryBtnFrame = Frame(self)
        self.entryBtnFrame.pack()
        
        self.newEntryBtn = Button(self.entryBtnFrame, text = "Enter product",
            command = self.clickNewEntry)
        self.newEntryBtn.pack(side = LEFT)
        
    def clickNewEntry(self):
        """Get all entry boxes and write to inventory database."""
        
        self.key = self.prodNum.get()
        self.record = [self.description.get(), self.color.get(),
            self.userCost.get(), self.sellPrice.get(), self.quantity.get()]
        self.writeShelf(self.key, self.record)
        
        #clear data fields
        self.prodNum.delete(0, END)
        self.description.delete(0, END)
        self.color.delete(0, END)
        self.userCost.delete(0, END)
        self.sellPrice.delete(0, END)
        self.quantity.delete(0, END)
    
    def writeShelf(self, key, record):
        """Opens DB, writes entries, then closes DB."""
        
        self.database = shelve.open(shelvename)
        self.database[self.key] = self.record
        self.database.close()
    
class ProductDisplay(Frame):
    """Interface for product display"""
    
    def __init__(self, parent = None):
        """Create, pack, and bind entry boxes and buttons for product display"""
        
        Frame.__init__(self)
        self.pack()
        
        self.frameHeading = Frame(self)
        self.frameHeading.pack()
        
        self.frameHeadingTitle = Label(self.frameHeading, text = "Current inventory",
            font = ("Arial", "12", "bold"))
        self.frameHeadingTitle.pack()      
        
        #---Database output
        self.showInventoryFrame = Frame(self).pack()
        
        ##Imported table-like multilist box
        self.listBox = MultiListbox(self.showInventoryFrame, (("Product Number", 10), 
            ("Description", 40), ("Color", 10), ("Unit cost", 5), ("Sell price", 5)
            , ("Quantity", 5)))
        self.listBox.pack(expand = YES, fill = BOTH)
        
        #---Inventory display buttons
        self.inventoryBtnFrame = Frame(self).pack()
        self.fetchInven = Button(self.inventoryBtnFrame, text = "Get inventory",
            command = self.getInven)
        self.fetchInven.pack(side = LEFT)
        
        self.modifyInven = Button(self.inventoryBtnFrame, text = "Update listing",
            command = self.changeInven)
        self.modifyInven.pack(side= LEFT)
        
        self.deleteInven = Button(self.inventoryBtnFrame, text = "Delete entry",
            command = self.clearEntry)
        self.deleteInven.pack(side = LEFT)
        
        self.clearInven = Button(self.inventoryBtnFrame, text = "Clear inventory",
            command = self.delInven)
        self.clearInven.pack(side = LEFT)
    
    def getInven(self):
        """Gets products from DB and displays them.
        
        Opens the shelve, loops through each entry, prints the unpacked tuple
        for each record, then closes the shelve."""
        self.listBox.delete(0, END)
        self.productList = shelve.open(shelvename)
        for item in self.productList.keys():
            (self.descrip, self.colors, self.cost, self.price, 
                self.quan) = self.productList[item]    #unpack tuple
            self.listBox.insert(END, (item, self.descrip, self.colors, self.cost,
                self.price, self.quan))
        self.productList.close()
    
    def clearEntry(self):
        """Deletes an entry from the database.
        
        Gets the highlighted selection, makes a list of the the separate words,
        'pops' the product number entry, finds the product number in the shelve,
        deletes the product, then updates the inventory screen."""
        
        ans = askokcancel("Verify delete", "Really remove item?")   #popup window
        if ans:
            self.productList = shelve.open(shelvename)
            self.getSelection = self.listBox.curselection() #get index of selection
            self.selectedEntry = self.listBox.get(self.getSelection)    #get tuple from selection
            (self.productNum, self.descrip, self.colors, self.cost, self.price, 
                self.quan) = self.selectedEntry    #unpack tuple
            self.entry = self.selectedEntry[0]
            del self.productList[self.entry]
            self.productList.close()
            showinfo(title = "Product removed",
                message = "The product has been removed from inventory.")
            self.getInven()

    def changeInven(self):
        """Allows modification of a database entry.
        
        Called by modifyInven Button"""
        
        try:    #see if a selection was made
            self.getSelection = self.listBox.curselection() #get index of selection
            self.selectedEntry = self.listBox.get(self.getSelection)    #get tuple from selection
            (self.prodnum, self.descrip, self.colors, self.cost, self.price, 
                self.quan) = self.selectedEntry    #unpack tuple
            
            #---New 'edit product' window
            self.editWindow = Toplevel()    
            self.editWindow.title("Edit selected entry")
            
            #---Edit product window widgets
            Label(self.editWindow, text = "Product Number").grid(row = 0, column = 0)
            Label(self.editWindow, text = "Description").grid(row = 0, column = 1)
            Label(self.editWindow, text = "Color").grid(row = 0, column = 2)
            Label(self.editWindow, text = "Unit cost").grid(row = 0, column = 3)
            Label(self.editWindow, text = "Sell price").grid(row = 0, column = 4)
            Label(self.editWindow, text = "Quantity").grid(row = 0, column = 5)
            
            self.oldNum = Entry(self.editWindow, name = "prodNum")
            self.oldNum.grid(row = 1, column = 0)
            self.oldDescrip = Entry(self.editWindow, name = "descrip")
            self.oldDescrip.grid(row = 1, column = 1)
            self.oldColor = Entry(self.editWindow, name = "color")
            self.oldColor.grid(row = 1, column = 2)
            self.oldCost = Entry(self.editWindow, name = "cost")
            self.oldCost.grid(row = 1, column = 3)
            self.oldPrice = Entry(self.editWindow, name = "price")
            self.oldPrice.grid(row = 1, column = 4)
            self.oldQuan = Entry(self.editWindow, name = "quan")
            self.oldQuan.grid(row = 1, column = 5)
            
            self.update = Button(self.editWindow, text = "Update product",
                command = self.updateProduct).grid(row = 2, column = 2)
            self.cancel = Button(self.editWindow, text = "Cancel",
                command = self.cancelProduct).grid(row = 2, column = 3) 
           
            #---Edit product data
            self.oldNum.insert(END, self.prodnum)
            self.oldDescrip.insert(END, self.descrip)
            self.oldColor.insert(END, self.colors)
            self.oldCost.insert(END, self.cost)
            self.oldPrice.insert(END, self.price)
            self.oldQuan.insert(END, self.quan)
            
        except TclError:    #tell user to make a selection first
            showerror(title = "Error!", message = "You must make a selection first!")
    
    def updateProduct(self):
        """Change the values of a database entry.
        
        Called by changeInven Button."""
        
        self.productList = shelve.open(shelvename)
        self.oldEntry = self.oldNum.get()
        self.newQuan = self.oldQuan.get()
        self.newCost = self.oldCost.get()
        self.newPrice = self.oldPrice.get()
        self.newRecord = [self.descrip, self.colors,
            self.newCost, self.newPrice, self.newQuan]
        self.productList[self.oldEntry] = self.newRecord
        self.productList.close()
        self.editWindow.destroy()
    
    def cancelProduct(self):
        """Verify canceling of product update."""
        
        self.editWindow.destroy()
    
    def delInven(self):
        """Deletes all entries in database."""
        
        ans = askokcancel("Verify delete", "Really clear inventory?")   #popup window
        if ans: 
            self.productList = shelve.open(shelvename)
            self.productList.clear()
            self.productList.close()
            showinfo(title = "Inventory cleared",
                message = "Your inventory database has been deleted.")

def main():
    root = Tk()
    entry = ProductEntry(root)
    display = ProductDisplay(root)
    entry.pack()
    display.pack()
    root.mainloop()
    
if __name__ == "__main__":
    main()
