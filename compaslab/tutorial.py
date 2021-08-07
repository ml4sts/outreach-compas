
import nbconvert
import nbformat
import jupytext
from IPython.display import display, Markdown
from IPython import get_ipython
import os
import pkg_resources as pkgrs
import importlib


tutorial_readers = {'ipynb': lambda fn : nbformat.read(fn, as_version =4).cells,
                    'md': lambda fn: jupytext.read(fn).cells}


builtin_activities = ['stem_academy']
# builtin_path = pkgrs.resource_listdir(__name__,'')


class Tutorial:
    '''
    '''

    def __init__(self,filename):
        # builtin_activities = importlib.resources.files()
        # print(builtin_activities)
        # if it's a builtin activity, update the filename to be the full path
        if pkgrs.resource_exists(__name__,filename):
            filename = pkgrs.resource_stream(__name__,filename)

        fmt = filename.split('.')[-1]

        self.tutorial = tutorial_readers[fmt](filename)

        self.current = 0

    def next(self):
        self.show(self.current)
        self.current += 1

    def start(self):
        self.show(0)
        self.current += 1

    def show(self,n):
        cell = self.tutorial[n]
        if cell.cell_type == 'markdown':
            display(Markdown(cell.source))
        if cell.cell_type =='code':
            with open ('cell' +str(n) +'.py','w') as f:
                f.write(cell.source)
            load_cmd = 'cell' + str(n)
            get_ipython().run_line_magic('load',load_cmd)
