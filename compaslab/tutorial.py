
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
                    'md': lambda fn: jupytext.read(fn)['cells']}


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
        self.show(self.tutorial[self.current])
        self.current += 1

    def start(self):
        '''
        start the tutorial
        '''
        self.show(self.tutorial[0])
        self.current = 1

    def show(self,cell):
        '''
        display a cell
        '''

        if cell.cell_type == 'markdown':
            display(Markdown(cell.source))
        if cell.cell_type =='code':
            cell_fname = os.path.join(self.tmp_dir,'cell'+str(self.current) +'.py')
            with open (cell_fname,'w') as f:
                f.write(cell.source)
            get_ipython().run_line_magic('load',cell_fname)
            self.tmp_file_list.append(cell_fname)

    def close(self):
        '''
        remove temporary files that were generated
        '''

        for tmpfile in self.tmp_file_list:
            os.remove(tmpfile)

        os.removedirs(self.tmp_dir)


def get_attr(cell,attr):
    '''
    from a notebook cell object, pull a lt meta field
    '''
    return cell.metadata.lecture_tools[attr]


def check_nb(file):
    '''
    '''
    # read file
    # cell_list =
    # check that each cell hass lecture_tools, block name and type

    required_meta = ['block','type']
    meta_missing = []
    fld_missing = {f:[] for f in required_meta}

    for cell in cell_list:
        if 'lecture_tools' in cell.metadata.keys():
            for attr in required_meta:
                if not(attr in cell.metadata.lecture_tools.keys()):
                    fld_missing[attr].append(cell)
        else:
            meta_missing.append(cell)

    return True

class BlockTutorial(Tutorial):

    def __init__():
        super().__init__()
        blocks = {}
        for c in self.tutorial]:
            cur_blk = get_attr(c,'block')
            if cur_blk in blocks.keys():
                blocks[cur_blk][get_attr(c,'type')] =c
            else:
                blocks[cur_blk] = {get_attr(c,'type'):c}
        self.blocks = blocks

    def next(self):
        '''
        show the next cell
        '''
        self.show(self.tutorial[self.current])
        self.current += 1

    def start(self):
        '''
        start the tutorial
        '''
    # def parse(self):
    #     '''
    #     parse the loaded notebook into instructions, hints, templates
    #     '''
