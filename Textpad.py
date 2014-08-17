import wx
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
        self.update_list = [""]
        self.redo_list = [""]
        self.max_count = 10

    def create_panel_components(self):
        """
            Description: Create Frame's Panel components. 
                         In this case it is just a simple multiline 
                         text control. 
        """
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Bind(wx.EVT_TEXT, self.text_changed, self.control)
    
    def text_changed(self, event):
        """
            Description: call back function for text change 
                         event on the editor
            input_param: event - text change event
            input_type: event - Event instance
            
        """
        if len(self.update_list) > self.max_count:
            self.update_list = self.update_list[1:self.max_count]
        self.update_list.append(self.control.GetValue())

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
            input_param: title - Title string to set on the window
            input_type: title - string
            
        """
        super(Textpad, self).SetTitle('Editor %s'%title)

if __name__ == '__main__':
	app = wx.App()
	frame = Textpad()
	app.MainLoop()
