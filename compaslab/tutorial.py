
import nbconvert
import nbformat
import jupytext
from IPython.display import display, Markdown
from IPython import get_ipython
import os
import pkg_resources as pkgrs
import importlib
from datetime import datetime


tutorial_readers = {'ipynb': lambda fn : nbformat.read(fn, as_version =4).cells,
                    'md': lambda fn: jupytext.read(fn).cells}


builtin_activities = ['stem_academy']
# builtin_path = pkgrs.resource_listdir(__name__,'')

TMP_DIR = 'tutorial_tmp'

class Tutorial:
    '''
    '''

    def __init__(self,filename):
        '''
        instantiate the object by reading in a notebook file

        Parameters
        ----------

        '''
        fmt = filename.split('.')[-1]

        # # if it's a builtin activity, update the filename to be the full path
        if pkgrs.resource_exists(__name__,os.path.join('activities',filename)):
            filename = pkgrs.resource_stream(__name__,
                                os.path.join('activities',filename))


        self.tutorial = tutorial_readers[fmt](filename)

        self.current = 0

        ## prep for tmp files
        self.tmp_dir = TMP_DIR + datetime.now().strftime('%Y%m%d%H%M%S%f')
        os.mkdir(self.tmp_dir)
        self.tmp_file_list = []


    def next(self):
        '''
        show the next cell
        '''
        self.show(self.current)
        self.current += 1

    def start(self):
        '''
        start the tutorial
        '''
        self.show(0)
        self.current = 1

    def show(self,n):
        '''
        display the nth cell
        '''
        cell = self.tutorial[n]
        if cell.cell_type == 'markdown':
            display(Markdown(cell.source))
        if cell.cell_type =='code':
            cell_fname = os.path.join(self.tmp_dir,'cell' +str(n) +'.py')
            with open (cell_fname,'w') as f:
                f.write(cell.source)
            # load_cmd = 'cell' + str(n)
            get_ipython().run_line_magic('load',cell_fname)
            self.tmp_file_list.append(cell_fname)

    def close(self):
        '''
        remove temporary files that were generated
        '''

        for tmpfile in self.tmp_file_list:
            os.remove(tmpfile)

        os.removedirs(self.tmp_dir)
