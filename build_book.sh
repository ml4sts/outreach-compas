mkdir docs/recaps
cp compaslab/activities/*.md docs/recaps/
jupyter-book build docs/
rm -rf docs/recaps/
