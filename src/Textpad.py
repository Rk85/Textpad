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
        self.dir_name = '.'
        self.file_name = "New File.txt"
        self.update_list = []
        self.redo_list = []
        self.max_count = 10
        self.content_saved = True
        self.icon_dir = "../icons/"
        
        self.status_bar = None
        self.tool_bar = None
        
        self.file_menu = None
        self.edit_menu = None
        self.view_menu = None
        
        # Create the panels for our components to stay
        self.toolbar_panel = wx.Panel(self, -1)
        self.editor_panel = wx.Panel(self, -1)
        
        # call the menu and other component creation functions
        self.create_editor_components()
        self.register_event_callbacks()
        
        # Create the sizer and add our panels into that
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.toolbar_panel, 0, flag=wx.EXPAND)
        sizer.Add(self.editor_panel, 1, flag=wx.EXPAND|wx.BOTTOM)
        self.SetSizer(sizer)
        self.SetIcon(wx.Icon(self.icon_dir + 'short_icon.ico', 
                             wx.BITMAP_TYPE_ICO)
                    )
        
        self.Show()
        
        

    def create_editor_components(self):
        """
            Description: Create all the components(TextArea, Menus,etc...)
                          for the editor
                         
        """
        menu.set_menu_bar(self)
        menu.set_tool_bar(self)
        
        # Create a sizer for our editor text area
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.control = wx.TextCtrl(self.editor_panel, style=wx.TE_MULTILINE)
        hbox.Add(self.control, 1, flag=wx.EXPAND)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, 1, flag=wx.EXPAND)
        self.editor_panel.SetSizer(vbox)
        
        self.status_bar = self.CreateStatusBar()
        self.SetTitle(self.file_name)
        
    def register_event_callbacks(self):
        """
            Description:  Registers the editor component for 
                         required event callbacks
            
        """
        self.control.Bind(wx.EVT_TEXT, self.text_changed)
        self.control.Bind(wx.EVT_LEFT_UP, self.show_status_text)
        self.control.Bind(wx.EVT_KEY_UP, self.show_status_text)
        self.Bind(wx.EVT_CLOSE, self.window_close)

    def window_close(self, event):
        """
            Description: Window close event handling function
            input_param: event - close Event 
            input_type: Event instance

        """
        
        if event.CanVeto() and not self.content_saved:
            close_dialog = wx.MessageDialog(self, 
                            "Do you want to save before closing?",
                            "Save Check",
                            wx.YES_NO|wx.CANCEL|wx.ICON_QUESTION)
            return_value = close_dialog.ShowModal()
            window_closed = False
            if return_value == wx.ID_YES:
                self.file_menu.save_file(event)
                window_closed = True
                self.Destroy()
            elif return_value == wx.ID_NO:
                window_closed = True
                self.Destroy()
            elif return_value == wx.ID_CANCEL:
                pass
            event.Veto(window_closed)
        else:
            self.Destroy()
     
    def text_changed(self, event):
        """
            Description: call back function for text change 
                         event on the editor
            input_param: event - text change event
            input_type: event - Event instance
            
        """
        if not self.content_saved:
            if len(self.update_list) > self.max_count:
                del self.update_list[0]
        else:
            self.SetTitle(self.file_name + "*")
            self.content_saved = False
        self.update_list.append(self.control.GetValue())

    def SetTitle(self, title):
        """
            Description: Sets the Frame's Tile with the give value
            input_param: title - Title string to set on the window
            input_type: title - string
            
        """
        super(Textpad, self).SetTitle('TextPad - %s'%title)
    
    def show_status_text(self, event):
        """
            Description: Show the text on the status bar if
                         it is visible
            input_param: event - menu change event
            input_type: event - Event instance
            
        """
        if self.status_bar and self.status_bar.IsShown():
            start_pos, end_pos = self.control.GetSelection()
            col, line = self.control.PositionToXY(end_pos)
            self.status_bar.SetStatusText("line no :{0}, col no:{1}".format(line+1, col+1))
        if event:
            event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frame = Textpad()
    app.MainLoop()
