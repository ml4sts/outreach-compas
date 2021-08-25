# Tutorial Logistics

This activity uses a custom library called compaslab that helps advance through
the activity.

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
```

If you get an error, check that all of the cells with code have a number to the left.

## Fill in the Black tutorial_tmp
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
```



## Adding a new tutorial

Add a notebook file to `compaslab/activities` directory in the [repository](https://github.com/ml4sts/outreach-compas)
