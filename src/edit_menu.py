import wx
import re

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
        self.frame.show_status_text(None)
    
    def copy_text(self, event):
        """
            Description: Copies the selected text from the editor
                         to system buffer
            input_param: event - Copy Event 
            input_type: Event instance

        """
        if self.frame.control.CanCopy():
            self.frame.control.Copy()
        self.frame.show_status_text(None)
    
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
        self.frame.show_status_text(None)
    
    def delete_text(self, event):
        """
            Description: Deletes the selected text from the editor
            input_param: event - Delete Event 
            input_type: Event instance

        """
        select_range = self.frame.control.GetSelection()
        self.frame.control.Remove(select_range[0], select_range[1])
        self.frame.content_saved = False
        self.frame.show_status_text(None)
    
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
            self.frame.SetTitle(self.frame.file_name + "*")
        self.frame.content_saved = False
        self.frame.show_status_text(None)
    
    def redo_text(self, event):
        """
            Description: Brings back the last change to the editor
            input_param: event - Redo Event 
            input_type: Event instance

        """
        if self.frame.redo_list:
            self.frame.control.SetValue(self.frame.redo_list.pop())
            self.frame.control.SetInsertionPointEnd()
        self.frame.content_saved = False
        self.frame.show_status_text(None)
    
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
                            wx.FR_NOUPDOWN
                         )
        self.find_replace_register_events(replace_dialog)
        return_value = replace_dialog.ShowModal()
        self.frame.show_status_text(None)
    
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
            flags = self.replace_data.GetFlags()
            find_text = self.replace_data.GetFindString()
            # If match by word option is set on the dialog
            pattern = "\\b" + find_text + "\\b" if flags & 2 else find_text
            match = re.search(pattern, 
                 editor_text[self.start_search_index:], 
                 flags=0 if flags & 4 else re.I
            )
            if match:
                start = self.start_search_index + match.start()
                end = self.start_search_index + match.end()
                self.frame.control.SetSelection(start, end)
                self.start_search_index = self.start_search_index + end
    
    def replace_string(self, max_occurence=0):
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
            flags = self.replace_data.GetFlags()
            find_text = self.replace_data.GetFindString()
            replace_text = self.replace_data.GetReplaceString()
            # If match by word option is set on the dialog
            pattern = "\\b" + find_text + "\\b" if flags & 2 else find_text
            new_text = re.sub(pattern, 
                 replace_text,
                 editor_text, 
                 count=max_occurence,
                 flags=0 if flags & 4 else re.I
            )
            self.frame.control.SetValue(new_text)

