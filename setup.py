from setuptools import setup

setup(name='compaslab',
      version='0.1',
      description='helper code for COMPAS tutorial activity',
      url='https://github.com/ml4sts/outreach-compas',
      author='Sarah M Brown',
      author_email='brownsarahm@uri.edu',
      license='MIT',
      packages=['compaslab'],
      zip_safe=False,
      install_requires=['Numpy', 'Pandas', 'Seaborn', 'Jupytext'])
