import wx
from file_menu import FileMenu
from edit_menu import EditMenu

# menu list for the textpad
MENUS = [
        {
            'name': 'File',
            'call_back_class': FileMenu,
            'frame_attribute': 'file_menu', # this is an attribute in TextPad 
            'sub_menus': [
                {
                    'id': wx.ID_NEW,
                    'help_text': 'Creats a new file',
                    'call_back': 'new_file',
                    'display': True,
                    'name': 'New'
                },
                {
                    'id': wx.ID_OPEN,
                    'help_text': 'Open a new file',
                    'call_back': 'open_file',
                    'display': True,
                    'name': 'Open'
                },
                {},
                {
                    'id': wx.ID_SAVE,
                    'help_text': 'Save the current file',
                    'call_back': 'save_file',
                    'display_order' : 2,
                    'display': True,
                    'name': 'Save'
                },
                {
                    'id': wx.ID_SAVEAS,
                    'help_text': 'Save the file under a different name',
                    'call_back': 'save_as_file',
                    'display_order' : 3,
                    'display': True,
                    'name': 'Save As\tShift+Ctrl+S'
                },
                {},
                {
                    'id': wx.ID_EXIT,
                    'help_text': 'Terminate the program',
                    'call_back': 'exit_program',
                    'display_order' : 5,
                    'display': True,
                    'name': 'Exit'
                }
            ],
            'display_order': 1,
            'display': True
        },
        {
            'name': 'Edit',
            'call_back_class': EditMenu,
            'frame_attribute': 'edit_menu',
            'sub_menus': [
                {
                    'id': wx.ID_CUT,
                    'help_text': 'Cuts the selected text',
                    'call_back': 'cut_text',
                    'display': True,
                    'name': 'Cut'
                },
                {
                    'id': wx.ID_COPY,
                    'help_text': 'Copies the selected text',
                    'call_back': 'copy_text',
                    'display': True,
                    'name': 'Copy'
                },
                {
                    'id': wx.ID_PASTE,
                    'help_text': 'Paste the selected text',
                    'call_back': 'paste_text',
                    'display': True,
                    'name': 'Paste'
                },
                {
                    'id': wx.ID_DELETE,
                    'help_text': 'Deletes the selected text',
                    'call_back': 'delete_text',
                    'display': True,
                    'name': 'Delete'
                },
                {},
                {
                    'id': wx.ID_UNDO,
                    'help_text': 'Removes the last change on the files',
                    'call_back': 'undo_text',
                    'display': True,
                    'name': 'Undo\tCtrl+Z'
                },
                {
                    'id': wx.ID_REDO,
                    'help_text': 'Brings back the last change on the file',
                    'call_back': 'redo_text',
                    'display': True,
                    'name': 'Redo\tCtrl+R'
                },
                {},
                {
                    'id': wx.ID_SELECTALL,
                    'help_text': 'Selects all the text in the editor',
                    'call_back': 'select_all_text',
                    'display': True,
                    'name': 'Select All\tCtrl+A'
                }
            ],
            'display_order': 2,
            'display': True
         
       }
]

def set_menu_bar(frame):
    """
        Description: Sets the list of menu/submenu items 
                     with the given frame object
        input_param: frame - frame to which menu should be attached
        input_type: frame - wx.Frame instance
        
    """
    menu_bar = wx.MenuBar()
    # traverse through the sorted list of menus
    for menu_group in sorted(
                  MENUS, key=lambda x: x['display_order']
                 ):
        # Create the menu Item and its instance 
        # and assigns the menu instance to one of the
        # Frame class(Textpad) attribute
        menu = wx.Menu()
        menu_object = menu_group['call_back_class'](frame)
        setattr(frame, menu_group['frame_attribute'], menu_object)
        
        # Traverse the submenu items and append it to main menu
        # Assign event call back funtions for each menu item 
        for sub_menu_item in menu_group.get('sub_menus', []):
            if not sub_menu_item:
                menu.AppendSeparator()
            else:
                menu_item = wx.MenuItem(menu, 
                                         sub_menu_item['id'], 
                                         sub_menu_item['name'],
                                         sub_menu_item['help_text']
                            )
                #menu_item.SetBitmap(wx.Bitmap('exit.png'))
                menu.AppendItem(menu_item)
                frame.Bind(
                    wx.EVT_MENU, 
                    getattr(menu_object, 
                             sub_menu_item['call_back'], 
                             None
                    ), 
                    menu_item
                )
        menu_bar.Append(menu, menu_group['name'])
    frame.SetMenuBar(menu_bar)
