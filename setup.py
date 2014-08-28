from distutils.core import setup
import py2exe

setup(name="Textpad",
      windows=["Textpad.py"],
      data_files=[("icons",
                   ["icons/about.png",
                    "icons/copy.png",
                    "icons/cut.png",
                    "icons/new.png",
                    "icons/open.png",
                    "icons/paste.png",
                    "icons/save.png",
                    "icons/separator.png"
                    ]
                   ),
                  ('.', ['short_icon.ico'])
                ]
)
