import wx

class ViewMenu(object):
    """
        Description: ViewMenu class - contains the callback functions
                     for each of submenu found under the View Menu
        
    """
    def __init__(self, frame):
        """
            Description: Initialize the View Menu
            
        """
        self.frame = frame
    
    def view_status_bar(self, event):
        """
            Description: Toggles the Status Bar Visiblity
            input_param: event - Mouse Event 
            input_type: Event instance

        """
        if self.frame.status_bar.IsShown():
            self.frame.status_bar.Hide()
        else:
            self.frame.status_bar.Show()
            self.frame.show_status_text(None)
