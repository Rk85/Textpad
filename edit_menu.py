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
    
    def delete_text(self, event):
        """
            Description: Deletes the selected text from the editor
            input_param: event - Delete Event 
            input_type: Event instance

        """
        select_range = self.frame.control.GetSelection()
        self.frame.control.Remove(select_range[0], select_range[1])
    
    def undo_text(self, event):
        """
            Description: Removes the last change from the editor
            input_param: event - Undo Event 
            input_type: Event instance

        """
        total_updates = len(self.frame.update_list)-1
        if total_updates > 0:
            last_update = self.frame.update_list[total_updates-1]
            self.frame.control.ChangeValue(last_update)
            
            if len(self.frame.redo_list) > self.frame.max_count:
                self.frame.redo_list = self.frame.redo_list[1:self.frame.max_count]
            self.frame.redo_list.append(self.frame.update_list[total_updates])
            
            self.frame.update_list = self.frame.update_list[:total_updates]
        self.frame.control.SetInsertionPointEnd()
    
    def redo_text(self, event):
        """
            Description: Brings back the last change to the editor
            input_param: event - Redo Event 
            input_type: Event instance

        """
        total_updates = len(self.frame.redo_list)-1
        self.frame.control.ChangeValue(self.frame.redo_list[total_updates])
        self.frame.control.SetInsertionPointEnd()
        self.frame.text_changed(None)

