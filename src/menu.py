import wx
from file_menu import FileMenu
from edit_menu import EditMenu
from view_menu import ViewMenu

VIEW_STATUS_BAR_ID = 30001
VIEW_FONT_ID = 30002
VIEW_ABOUT_ID = 30003
VIEW_TOOL_BAR_ID = 30004

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
                    'name': 'New',
                    'tool_menu': True,
                    'icon_name': 'new.png'
                },
                {
                    'id': wx.ID_OPEN,
                    'help_text': 'Open a new file',
                    'call_back': 'open_file',
                    'display': True,
                    'name': 'Open',
                    'tool_menu': True,
                    'icon_name': 'open.png'
                },
                {},
                {
                    'id': wx.ID_SAVE,
                    'help_text': 'Save the current file',
                    'call_back': 'save_file',
                    'display_order' : 2,
                    'display': True,
                    'name': 'Save',
                    'tool_menu': True,
                    'icon_name': 'save.png'
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
                    'name': 'Cut',
                    'tool_menu': True,
                    'icon_name': 'cut.png'
                },
                {
                    'id': wx.ID_COPY,
                    'help_text': 'Copies the selected text',
                    'call_back': 'copy_text',
                    'display': True,
                    'name': 'Copy',
                    'tool_menu': True,
                    'icon_name': 'copy.png'
                },
                {
                    'id': wx.ID_PASTE,
                    'help_text': 'Paste the selected text',
                    'call_back': 'paste_text',
                    'display': True,
                    'name': 'Paste',
                    'tool_menu': True,
                    'icon_name': 'paste.png'
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
                },
                {
                    'id': wx.ID_REPLACE,
                    'help_text': 'Replace the text in the editor',
                    'call_back': 'replace_text',
                    'display': True,
                    'name': 'Replace\tCtrl+H'
                }
            ],
            'display_order': 2,
            'display': True
         
       },
       {
            'name': 'View',
            'call_back_class': ViewMenu,
            'frame_attribute': 'view_menu',
            'sub_menus': [
                {
                    'id': VIEW_STATUS_BAR_ID,
                    'help_text': 'Shows/Hides the Status Bar in the editor',
                    'call_back': 'view_status_bar',
                    'display': True,
                    'name': 'Show Status Bar',
                    'kind_type': wx.ITEM_CHECK,
                    'kind_value': True
                },
                {
                    'id': VIEW_TOOL_BAR_ID,
                    'help_text': 'Shows/Hides the Tool Bar in the editor',
                    'call_back': 'view_tool_bar',
                    'display': True,
                    'name': 'Show Tool Bar',
                    'kind_type': wx.ITEM_CHECK,
                    'kind_value': True
                },
                {
                    'id': VIEW_FONT_ID,
                    'help_text': 'Enables the user to change the font',
                    'call_back': 'view_font_change',
                    'display': True,
                    'name': 'Font'
                },
                {
                    'id': VIEW_ABOUT_ID,
                    'help_text': 'shows About Window',
                    'call_back': 'view_about_info',
                    'display': True,
                    'name': 'About'
                }
            ],
            'display_order': 3,
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
        create_sub_menus(menu,
                         menu_group['sub_menus']
        )
        register_menu_call_backs(frame,
                              menu.GetMenuItems(),
                              menu_group['sub_menus'],
                              menu_object
        ) 
        menu_bar.Append(menu, menu_group['name'])
    frame.SetMenuBar(menu_bar)

def create_sub_menus(menu, sub_menu_list):
    """
        Description: Creates all the required submenus under 
                     the given menu item 
        input_param: menu - Main menu to which the new sub-menus
                     need to be attached
        input_type: menu - wx.Menu Instance
        input_param: sub_menu_list - Details of the Sub Menus
                     that need to be created
        input_type: sub_menu_list - list of dictionary
        
    """
    # Traverse the submenu items and append it to main menu
    # Assign event call back funtions for each menu item 
    for sub_menu_item in sub_menu_list:
        if not sub_menu_item:
            menu.AppendSeparator()
        else:
            menu_item = wx.MenuItem(menu,
                          sub_menu_item['id'],
                          sub_menu_item['name'],
                          sub_menu_item['help_text'],
                          sub_menu_item.get('kind_type', wx.ITEM_NORMAL)
                        )
            #menu_item.SetBitmap(wx.Bitmap('exit.png'))
            menu.AppendItem(menu_item)
            if menu_item.IsCheckable():
                menu_item.Check(sub_menu_item.get('kind_value', False))

def register_menu_call_backs(frame,
                             menu_items,
                             sub_menu_details,
                             menu_object, 
                            ):
    """
        Description: Registers the Menu Call back event for  
                     each SubMenu that is created
        input_param: frame - Main Editor frame window
        input_type: frame - wx.Frame
        input_param: menu_items - list of MenuItem to which
                     event call back need to be registered
        input_type: menu_items - list of wx.MenuItem Instance
        input_param: sub_menu_list - Details of the Sub Menus
                     that is being registered for events
        input_type: sub_menu_list - list of dictionary
        input_param: menu_object - Menu class instance which is
                     having call back functions
        input_type: menu_object - Class Instance
        
    """
    for menu_item in menu_items:
        for sub_menu_detail in sub_menu_details:
            if menu_item.GetId() == sub_menu_detail.get('id'):
                frame.Bind(wx.EVT_MENU,
                        getattr(menu_object,
                              sub_menu_detail['call_back'],
                              None
                        ),
                        menu_item
                )

def set_tool_bar(frame):
    """
        Description: Sets the Toolbar items on the UI 
                     with the given frame object
        input_param: frame - frame to which tool bar should be attached
        input_type: frame - wx.Frame instance
        
    """
    frame.tool_bar = wx.ToolBar(frame.toolbar_panel, 0, 
                         style=wx.TB_HORIZONTAL | wx.NO_BORDER| wx.TB_NODIVIDER
    )
    for menu_group in sorted(
                  MENUS, key=lambda x: x['display_order']
                 ):
        handler_instance = getattr(frame, 
                                   menu_group['frame_attribute'], 
                                   None
                           )
        add_separator = False
        if handler_instance:
            for sub_menu in menu_group.get('sub_menus', []):
                if sub_menu.get('tool_menu'):
                    frame.tool_bar.AddSimpleTool(sub_menu['id'], 
                                       wx.Bitmap(frame.icon_dir + sub_menu['icon_name'], 
                                                   wx.BITMAP_TYPE_PNG), 
                                       sub_menu['name'])
                    frame.Bind(wx.EVT_TOOL, 
                               getattr(handler_instance, 
                                        sub_menu['call_back'], 
                                        None),
                               id=sub_menu['id'])
                    add_separator = True
        if add_separator:
            frame.tool_bar.AddSimpleTool(wx.ID_ANY, 
                            wx.Bitmap(frame.icon_dir+'separator.png', 
                                                   wx.BITMAP_TYPE_PNG), 
                                      '')
    frame.tool_bar.Realize()
    
    # Set the Sizer for the ToolBar
    vbox = wx.BoxSizer(wx.VERTICAL)
    hbox = wx.BoxSizer(wx.HORIZONTAL)
    hbox.Add(frame.tool_bar, 0, wx.EXPAND)
    vbox.Add(hbox, 0, flag=wx.EXPAND)
    frame.toolbar_panel.SetSizer(vbox)
