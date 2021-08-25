
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


builtin_activities = ['stem_academy','stem_academy_hints']
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

        self.next_cell= 0

        ## prep for tmp files
        self.tmp_dir = TMP_DIR + datetime.now().strftime('%Y%m%d%H%M%S%f')
        os.mkdir(self.tmp_dir)
        self.tmp_file_list = []


    def next(self):
        '''
        show the next cell
        '''
        self.display(self.tutorial[self.next_cell])
        self.next_cell+= 1

    def start(self):
        '''
        start the tutorial
        '''
        self.display(self.tutorial[0])
        self.next_cell= 1

    def display(self,cell):
        '''
        display a cell
        '''

        if cell.cell_type == 'markdown':
            display(Markdown(cell.source))
        if cell.cell_type =='code':
            cell_fname = os.path.join(self.tmp_dir,'cell'+str(self.next_cell) +'.py')
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

class LiveTutorial(Tutorial):

    def __init__(self,filename):
        super().__init__(filename)
        blocks = {}
        for i,c in enumerate(self.tutorial):
            cur_blk = get_attr(c,'block')
            cur_type = get_attr(c,'type')
            # create or append to the dictionary for this block
            if cur_blk in blocks.keys():

                blocks[cur_blk][cur_type] =c

            else:
                blocks[cur_blk] = {cur_type:c}

            # always enumerate the cell for advancing linearly
            blocks[cur_blk][cur_type]['num'] =i

        self.blocks = blocks
        self.block_list = list(blocks.keys())
        self.current_block = self.block_list[0]

    def start(self):
        '''
        start the tutorial
        '''
        self.current_block = self.block_list[0]
        self.display(self.tutorial[0])
        self.next_cell= 1

    def next(self):
        '''
        show the next cell and advance in order
        '''
        self.display(self.tutorial[self.next_cell])
        self.next_cell += 1

    def jump(self):
        '''
        show first cell in the next block
        '''
        cur_block_num = self.block_list.index(self.current_block)
        next_blockname = self.block_list[cur_block_num+2]
        self.show(next_blockname)


    def show(self,blockname):
        '''
        show first cell in a block
        '''
        if blockname in self.block_list:

            first_type = list(self.blocks[blockname].keys())[0]
            cell = self.blocks[blockname][first_type]
            self.display(cell)
            self.current_block = blockname
            self.next_cell = cell['num'] +1
        else:
            self.missingblock(blockname)

    def intro(self,blockname= None):
        '''
        show intro text of the given block and advance
        '''
        if not(blockname):
            blockname = self.current_block
        self.showpart(blockname,'narrative')

    def template(self, blockname = None):
        '''

        '''
        if not(blockname):
            blockname = self.current_block
        self.showpart(blockname,'template')

    def hint(self, blockname = None):
        '''
        '''
        if not(blockname):
            blockname = self.current_block
        self.showpart(blockname,'hint')

    def solution(self, blockname = None):
        '''
        show the solution of a specific or the current block
        '''
        if not(blockname): # ev
            blockname = self.current_block
        self.showpart(blockname,'solution')

    def explain(self, blockname = None):
        '''
        show the solution of a specific or the current block
        '''
        if not(blockname): # ev
            blockname = self.current_block
        self.showpart(blockname,'interpretation')


    def showpart(self, blockname,partname):
        '''
        show partname cell of  blockname section
        '''
        # check if the block exists
        if blockname in self.blocks.keys():
            # check if the part exists
            if partname in self.blocks[blockname].keys():
                cell = self.blocks[blockname][partname]
                self.display(cell)
                self.current_block = blockname
                self.next_cell = cell['num'] +1
            else:
                self.missingpart(blockname,partname)
        else:
            self.missingblock(blockname)

    def missingpart(self,blockname,partname):
        '''
        note tha there's no such part
        '''

        msg = ("The " + blockname + " section does'nt have a " +
                    partname + "try `.next()`" )
        display(Markdown(msg))

    def missingblock(self,blockname):
        '''
        note tha there's no such part
        '''
        msg = "There is no " + blockname
                    # " section, the options are :" + str(self.block_list))
        display(Markdown(msg))



    # def parse(self):
    #     '''
    #     parse the loaded notebook into instructions, hints, templates
    #     '''
