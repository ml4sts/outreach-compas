
import nbconvert
import nbformat
import jupytext
from IPython.display import display, Markdown
from IPython import get_ipython

tutorial_readers = {'ipynb': lambda fn : nbformat.read(fn, as_version =4),
                    'md': lambda fn: jupytext.read(fn)}

class Tutorial:
    '''
    '''

    def __init__(self,filename):
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
        cell = lab.cells[n]
        if cell.cell_type == 'markdown':
            display(Markdown(cell.source))
        if cell.cell_type =='code':
            with open ('cell' +str(n) +'.py','w') as f:
                f.write(cell.source)
            load_cmd = 'cell' + str(n)
            get_ipython().run_line_magic('load',load_cmd)
