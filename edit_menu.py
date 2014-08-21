import wx

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
        self.frame.content_saved = False
    
    def copy_text(self, event):
        """
            Description: Copies the selected text from the editor
                         to system buffer
            input_param: event - Copy Event 
            input_type: Event instance

        """
        if self.frame.control.CanCopy():
            self.frame.control.Copy()
    
    def paste_text(self, event):
        """
            Description: Paste the selected text to the editor
                         from system buffer
            input_param: event - Paste Event 
            input_type: Event instance

        """
        if self.frame.control.CanPaste():
            self.frame.control.Paste()
        self.frame.content_saved = False
    
    def delete_text(self, event):
        """
            Description: Deletes the selected text from the editor
            input_param: event - Delete Event 
            input_type: Event instance

        """
        select_range = self.frame.control.GetSelection()
        self.frame.control.Remove(select_range[0], select_range[1])
        self.frame.content_saved = False
    
    def undo_text(self, event):
        """
            Description: Removes the last change from the editor
            input_param: event - Undo Event 
            input_type: Event instance

        """
        if self.frame.update_list:
            if len(self.frame.redo_list) > self.frame.max_count:
                del self.frame.redo_list[0]
            self.frame.redo_list.append(self.frame.update_list.pop())
            
        self.frame.control.ChangeValue(
                  self.frame.update_list[-1] if self.frame.update_list 
                  else ""
        )
        self.frame.control.SetInsertionPointEnd()
        if self.frame.content_saved:
            self.frame.SetTitle(self.frame.filename + "*")
        self.frame.content_saved = False
    
    def redo_text(self, event):
        """
            Description: Brings back the last change to the editor
            input_param: event - Redo Event 
            input_type: Event instance

        """
        if self.frame.redo_list:
            self.frame.control.SetValue(self.frame.redo_list.pop())
            self.frame.control.SetInsertionPointEnd()
            #self.frame.text_changed(None)
        self.frame.content_saved = False
    
    def select_all_text(self, event):
        """
            Description: Selects all the text in the editor
            input_param: event - Select All Event 
            input_type: Event instance

        """
        self.frame.control.SelectAll()
    
    def replace_text(self, event):
        """
            Description: Search/Replace the text in the editor
            input_param: find/replace - Menu selection Event 
            input_type: Event instance

        """
        self.start_search_index = 0
        self.replace_data = wx.FindReplaceData()
        replace_dialog = wx.FindReplaceDialog(self.frame.control,
                            self.replace_data,
                            'Replace Text',
                            wx.FR_REPLACEDIALOG|
                            wx.FR_NOUPDOWN|
                            wx.FR_NOMATCHCASE|
                            wx.FR_NOWHOLEWORD
                         )
        self.find_replace_register_events(replace_dialog)
        return_value = replace_dialog.ShowModal()
    
    def find_replace_register_events(self, replace_dialog):
        """
            Description: Registers the find/replace dialog for 
                         required events
            input_param: replace_dialog - Find/Replace Dialog 
                           to which event have to registered 
            input_type: FindReplaceDialog instance

        """
        replace_dialog.Bind(wx.EVT_FIND, 
                            self.replace_text_call_back
                           )
        replace_dialog.Bind(wx.EVT_FIND_NEXT, 
                            self.replace_text_call_back
                           )
        replace_dialog.Bind(wx.EVT_FIND_REPLACE, 
                           self.replace_text_call_back
                           )
        replace_dialog.Bind(wx.EVT_FIND_REPLACE_ALL, 
                            self.replace_text_call_back
                           )
        replace_dialog.Bind(wx.EVT_FIND_CLOSE, 
                            self.replace_text_call_back
                           )
        
    
    def replace_text_call_back(self, event):
        """
            Description: Handling call back events for find/replace buttons 
            input_param: event - find, replace, replace events
            input_type: Event instance

        """
        if event.GetEventType() == wx.wxEVT_COMMAND_FIND:
            self.set_search_string_selected(0)
        elif event.GetEventType() == wx.wxEVT_COMMAND_FIND_NEXT:
            self.set_search_string_selected(self.start_search_index)
        elif event.GetEventType() == wx.wxEVT_COMMAND_FIND_REPLACE:
            self.replace_string(1)
        elif event.GetEventType() == wx.wxEVT_COMMAND_FIND_REPLACE_ALL:
            self.replace_string()
        elif event.GetEventType() == wx.wxEVT_COMMAND_FIND_CLOSE:
            event.GetDialog().Destroy()
    
    def set_search_string_selected(self, start_index):
        """
            Description: Sets the searching string as selected string 
                         in the editor when a match is found from the 
                         given start index
            input_param: start_index - from which position, 
                          we should satrt search
            input_type: Int

        """
        editor_text = self.frame.control.GetValue()
        if editor_text:
            find_string = self.replace_data.GetFindString()
            index = editor_text.find(find_string, start_index)
            if index != -1 :
                self.frame.control.SetSelection(index, index+len(find_string))
                self.start_search_index = index+len(find_string)
    
    def replace_string(self, max_occurence=None):
        """
            Description: Replaces the searching string in the editor 
                         when a match is found and for given max occurence
                         times
            input_param: max_occurence - No of times replace of string 
                         should be done.
            input_type: Int

        """
        editor_text = self.frame.control.GetValue()
        if editor_text:
            find_string = self.replace_data.GetFindString()
            replace_string = self.replace_data.GetReplaceString()
            if max_occurence:
                editor_text = editor_text.replace(find_string, replace_string, max_occurence)
            else:
                editor_text = editor_text.replace(find_string, replace_string)
            self.frame.control.SetValue(editor_text)

