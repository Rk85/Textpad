import wx
import os.path

class FileMenu(object):
    """
        Description: FileMenu class - contains the callback functions
                     for each of submenu found under the File Menu
        
    """
    def __init__(self, frame):
        """
            Description: Initialize the File Menu
            
        """
        self.frame = frame
        self.default_file_dialog_options = {
            'message': 'Choose a file', 
            'defaultDir': self.frame.dirname,
            'wildcard': '*.*'
        }
    
    def askUserForFilename(self):
        """
            Description: Find whether the user has provided the 
                         file name to access on 
            return_param: userProvidedFilename - user selected the file ot not
            return_type: Boolean
            
        """
        # show the file dialog
        dialog = wx.FileDialog(self.frame, **self.default_file_dialog_options)
        
        # user has selected a file name
        if dialog.ShowModal() == wx.ID_OK:
            userProvidedFilename = True
            self.frame.filename = dialog.GetFilename()
            self.frame.dirname = dialog.GetDirectory()
            self.frame.SetTitle(self.frame.filename) # Update the window title with the new filename
        else:
            userProvidedFilename = False
        dialog.Destroy()
        return userProvidedFilename

    def new_file(self, event):
        """
            Description: Clears previous content from editor 
                         and creats new file
            input_param: event - Create Event 
            input_type: Event instance

        """
        self.frame.control.Clear()
        self.frame.filename = "New File.txt"
        self.frame.SetTitle(self.frame.filename)
        self.frame.content_saved = True
        
    def open_file(self, event):
        """
            Description: Open the selected file
            input_param: event - Open Event 
            input_type: Event instance
            
        """
        self.default_file_dialog_options.update(
            {
                'defaultDir': self.frame.dirname,
                'style': wx.FD_OPEN
            }
        )
        if self.askUserForFilename():
            with open(os.path.join(self.frame.dirname, self.frame.filename), 'r') as textfile:
                self.frame.control.SetValue(textfile.read())
                textfile.close()
        self.frame.content_saved = True
        self.frame.SetTitle(self.frame.filename)
        self.frame.update_list = []
        self.frame.redo_list = []
    
    def save_file(self, event):
        """
            Description: Save the text content into a file
            input_param: event - Save Event 
            input_type: Event instance
            
        """
        with open(os.path.join(self.frame.dirname, self.frame.filename), 'w') as textfile:
            textfile.write(self.frame.control.GetValue())
            textfile.close()
        self.frame.SetTitle(self.frame.filename) 
        self.frame.content_saved = True
    
    def save_as_file(self, event):
        """
            Description: Save the file into different name
            input_param: event - save Event 
            input_type: Event instance
            
        """
        self.default_file_dialog_options.update(
            {
            'message': 'Choose a file',
            'defaultDir': self.frame.dirname,
            'wildcard': '*.*',
            'style': wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT,
            'defaultFile': self.frame.filename
            }
        )
        if self.askUserForFilename():
            self.save_file(event)
            self.frame.SetTitle(self.frame.filename) 
            self.frame.content_saved = True
    
    def exit_program(self, event):
        """
            Description: Exit from TextPad application
            input_param: event - Exit Event 
            input_type: Event instance
            
        """
        self.frame.Close()
    
