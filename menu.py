import wx
from file_menu import FileMenu
from edit_menu import EditMenu

FRAME = None

# menu list for the textpad
MENUS = [
        {
            'name': 'File',
            'call_back_class': FileMenu,
            'sub_menus': [
                {
                    'id': wx.ID_OPEN,
                    'help_text': 'Open a new file',
                    'call_back': 'open_file',
                    'display': True,
                    'name': 'Open'
                },
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
                    'name': 'Save As'
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
            'sub_menus': [
                {
                    'id': wx.ID_CUT,
                    'help_text': 'Cuts the selected text',
                    'call_back': 'cut_text',
                    'display': True,
                    'name': 'Cut'
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
    global FRAME 
    FRAME = frame
    menu_bar = wx.MenuBar()
    for menu_item in sorted(
                  MENUS, key=lambda x: x['display_order']
                 ):
        menu = wx.Menu()
        menu_instance = menu_item['call_back_class'](FRAME)
        for sub_menu_item in menu_item.get('sub_menus', []):
            if not sub_menu_item:
                menu.AppendSeparator()
            else:
                item = menu.Append(
                               sub_menu_item['id'], 
                               sub_menu_item['name'], 
                               sub_menu_item['help_text']
                             )
                frame.Bind(wx.EVT_MENU, getattr(menu_instance, sub_menu_item['call_back'], None), item)
        menu_bar.Append(menu, menu_item['name'])
    frame.SetMenuBar(menu_bar)
