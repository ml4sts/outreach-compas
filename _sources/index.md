# ML4STS Lab COMPAS Activity

This is the home page for our lab's outreach activity.  

<!-- Choose the page below for your specific event's detailed instructions -->

1. Go to the [URI Jupyter Notebook Server](https://jupyter.uri.edu/)
1. Open a new notebook,
1. Download and install helper code:

  ```
  pip install git+git://github.com/ml4sts/outreach-compas.git
  ```

1. create a tutorial object

  <!-- ```
  import compaslab
  tut= compaslab.LiveTutorial('stem_academy_hints.ipynb')
  ```

1. if you fall behind: -->

  ```
  import compaslab
  tut= compaslab.Tutorial('stem_academy.ipynb')
  ```

1. Follow along using

  ```
  tut.next()
  ```
