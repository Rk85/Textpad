from distutils.core import setup
import py2exe

setup(name="Textpad",
      windows=["src/Textpad.py"],
      package_dir = {'': 'src'},
      py_modules = ['file_menu',
                    'edit_menu',
                    'menu',
                    'Textpad',
                    'view_menu'],
      data_files=[("icons",
                   ["icons/about.png",
                    "icons/copy.png",
                    "icons/cut.png",
                    "icons/new.png",
                    "icons/open.png",
                    "icons/paste.png",
                    "icons/save.png",
                    "icons/separator.png",
                    "icons/short_icon.ico"
                    ]
                   )
                  ]
)
