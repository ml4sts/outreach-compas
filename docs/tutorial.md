# Tutorial Logistics

This activity uses a custom library called compaslab that helps advance through
the activity.

## Installation

The library is packaged, but not deployed in PiPy, so we install it directly from
GitHub.

```
pip install git+git://github.com/ml4sts/outreach-compas.git
```

## Usage
After installing, import the package
```
import compaslab
```


## Basic Tutorial navigation



load the activity
```
tut = compaslab.Tutorial('filename')
```

Then proceeed using these controls

```{list-table}
:header-rows: 1

* - Action
  - How to
* - execute a cell (block in the notebook)
  - shift + enter (windows/linux) or shift + return (mac)
* - go to the next step
  - `tut.next()`
* - get back to the right place if out of sync and lost track, by resetting
  - `tut.start()`
* - clean up the temporary files
  - `tut.close()`
* - repeat a step
  - `tut.repeat()`
* - go back N steps
  - `tut.previous(N)`
```

If you get an error, check that all of the cells with code have a number to the left.

## Fill in the Blank Tutorial Navigation
A more advanced version with fill in the blanks can be started with

```
tut = compaslab.LiveTutorial('filename')
```

That provides the additional controls:
```{list-table}
:header-rows: 1
* - go to the next section
  - `tut.jump()`
* - get a hint
  - `tut.hint()`
* - get the intro for a section
  - `tut.intro()`
* - get the template
  - `tut.template()`
* - get the solution
  - `tut.solution()`
* - get an explanation or interpretation of a cell
  - `tut.explain()`
* - go to a specific section
  - `tut.show('sectionname')`
```
All of the basic commands work as well


## Adding a new tutorial

Add a notebook file to `compaslab/activities` directory in the [repository](https://github.com/ml4sts/outreach-compas)

You can read the ones in there (especially the .md versions) to see an example.

When writing the notebook file, this can be done in a regular notebook or a Myst
markdown notebook.  If using Myst (which is good for version control) sync it with
a notebook file using `jupytext` by including the following in the header.

```
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
```

You can then use
```
jupytext --sync filename.md
```
to get the `.ipynb` file up to date, this is important because the `jupytext`
read function in the library doesn't currently work.

To make a tutorial that has hints put meta data in each cell.  

- For markdown cells:

     ```
     +++ {"lecture_tools": {"block": "<name of step>", "type": "<type of cell>"}}
     ```
- For code cells:

    ```
    ---
    lecture_tools:
      block: <name of step>
      type: <type of cell>
    ---
    ```

The `---` marks the start and end of the metadata in a code cell.
The name can be whatever, but should be descriptive and typically a few
consecutive cells will have the same name but be different types.
The type can be one of the following:
- narrative
- template
- hint
- solution
- interpretation

For `hint` and `template` cells, also include the following  in the metadata so
that the recap will work correctly.

```
tags: [raises-exception]
```

You can set metadata in the [notebook interface](https://jupyterbook.org/content/metadata.html#adding-tags-using-notebook-interfaces) too.
