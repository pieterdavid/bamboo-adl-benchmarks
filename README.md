# Implementation of the [IRIS-HEP ADL benchmarks](https://github.com/iris-hep/adl-benchmarks-index) using the [bamboo](https://gitlab.cern.ch/cp3-cms/bamboo) framework

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pieterdavid/bamboo-docker/master?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fpieterdavid%252Fbamboo-adl-benchmarks%26urlpath%3Dlab%252Ftree%252Fbamboo-adl-benchmarks%252Fex1.py%26branch%3Dmaster)

These can be run on Binder through the badge above, or installed locally (see the [documentation](https://cp3.irmp.ucl.ac.be/~pdavid/bamboo/install.html); [plotIt](https://github.com/cp3-llbb/plotIt) is not required) with:
```bash
cd bamboo-adl-benchmarks
export PYTHONPATH=$PYTHONPATH:$(pwd) # to allow importing shared code from adl_benchmarks.py
bambooRun -m exN.py:BenchmarkN adl_benchmarks.yml -o out_N
```
(replacing N by the numer of the benchmark).
The resulting histograms will be stored in `out_N/results/SingleMuon_test.root`.

Since some of the benchmarks go through a lot of combinatorics, [implicit multithreading](https://doi.org/10.1088/1742-6596/898/7/072022) in [RDataFrame](https://root.cern/doc/master/classROOT_1_1RDataFrame.html)
(which can be enabled by passing `--threads N`, with N=3 or so) is useful to speed them up.
