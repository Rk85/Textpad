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
            input_param: event - Menu Event 
            input_type: Event instance

        """
        if self.frame.status_bar.IsShown():
            self.frame.status_bar.Hide()
        else:
            self.frame.status_bar.Show()
            self.frame.show_status_text(None)
    
    def view_font_change(self, event):
        """
            Description: Allows the user to change the font on 
                         the editor
            input_param: event - Menu Event 
            input_type: Event instance

        """
        font_dialog = wx.FontDialog(self.frame, wx.FontData())
        if font_dialog.ShowModal() == wx.ID_OK:
            font_details = font_dialog.GetFontData().GetChosenFont()
            self.frame.control.SetFont(font_details)
