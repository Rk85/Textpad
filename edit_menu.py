import wx
import os

class EditMenu(object):
    """
        Description: EditMenu class - contains the callback functions
                     for each of submenu found under the Edit Menu
        
    """
    def __init__(self, frame):
        """
            Description: Initialize the Edit Menu
            
        """
        self.frame = frame
    
    def cut_text(self, event):
        """
            Description: Cuts the selected text from the editor
            input_param: event - Cut Event 
            input_type: Event instance

        """
        if self.frame.control.CanCut():
            self.frame.control.Cut()
