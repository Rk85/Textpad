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
                   ["src/icons/about.png",
                    "src/icons/copy.png",
                    "src/icons/cut.png",
                    "src/icons/new.png",
                    "src/icons/open.png",
                    "src/icons/paste.png",
                    "src/icons/save.png",
                    "src/icons/separator.png",
                    "src/icons/short_icon.ico"
                    ]
                   ),
                  ('.', ['src/icons/short_cut.vbs'])
                  ]
)
