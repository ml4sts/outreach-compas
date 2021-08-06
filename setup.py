from setuptools import setup

setup(name='tutorial',
      version='0.1',
      description='helper code for COMPAS tutorial activity',
      url='https://github.com/ml4sts/outreach-compas',
      author='Sarah M Brown',
      author_email='brownsarahm@uri.edu',
      license='MIT',
      packages=['tutorial'],
      zip_safe=False,
      install_requires=['Numpy', 'Pandas', 'Seaborn'])
