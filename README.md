Implementation of the IRIS-HEP ADL benchmarks https://github.com/iris-hep/adl-benchmarks-index
using the bamboo framework https://gitlab.cern.ch/cp3-cms/bamboo

After installing bamboo (see the [documentation](https://cp3.irmp.ucl.ac.be/~pdavid/bamboo/install.html), plotIt is not required) these can be run with
```bash
bambooRun -m exN.py:ADLBencharkN adl_benchmarks.yml -o out_N
```
(replacing N by the numer of the benchmark).
The resulting histograms will be stored in `out_N/results/SingleMuon_test.root`.

Since some of the benchmarks go through a lot of combinatorics, implicit multithreading
(which can be enabled by passing `--threads N`, with N=3 or so) is useful to speed them up.
