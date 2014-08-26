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
        if self.frame.status_bar and self.frame.status_bar.IsShown():
            self.frame.status_bar.Destroy()
        else:
            self.frame.status_bar = self.frame.CreateStatusBar()
            self.frame.show_status_text(event)
    
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
    
    def view_about_info(self, event):
        """
            Description: Allows the user to change the font on 
                         the editor
            input_param: event - Menu Event 
            input_type: Event instance

        """
        info = wx.AboutDialogInfo()
        description = """This application helps the user to
create/edit the text documents"""
        licence = """TextPad is free software; you can redistribute 
it and/or modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation; either version 2 of the License, 
or (at your option) any later version.

TextPad is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details."""
        info.SetIcon(wx.Icon('icons/about.png', wx.BITMAP_TYPE_PNG))
        info.SetName('TextPad')
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2014 - 2014 Radhakrishnan Raji rachandkrishnan@gmail.com')
        info.SetLicence(licence)
        info.AddDeveloper('Radhakrishnan Raji')
        wx.AboutBox(info)

