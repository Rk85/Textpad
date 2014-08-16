import wx
import os.path
import menu

class Textpad(wx.Frame):
    """
        Description: Base Frame class for the editor
        
    """
    def __init__(self):
        """
            Description: Initialize the Frame class
        """
        super(Textpad, self).__init__(None, size=(800,400))
        self.create_panel_components()
        self.create_menu_components()
        self.Show()

    def create_panel_components(self):
        """
            Description: Create Frame's Panel components. 
                         In this case it is just a simple multiline 
                         text control. 
        """
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

    def create_menu_components(self):
        """
            Description:  Create all the menu components, 
                          such as top menu and status bar. 
        """
        menu.set_menu_bar(self)
        self.CreateStatusBar()
        self.SetTitle("New File.txt")

    def SetTitle(self, title):
        """
            Description: Sets the Frame's Tile with the give value
        """
        super(Textpad, self).SetTitle('Editor %s'%title)

if __name__ == '__main__':
	app = wx.App()
	frame = Textpad()
	app.MainLoop()
