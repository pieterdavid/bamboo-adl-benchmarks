#!/usr/bin/env bash

echo "Running ex1"
bambooRun -m ex1.py:Benchmark1 adl_benchmarks.yml --prefix=ex1_ -o out_1 &> out_1.log || return 1
echo "Running ex2"
bambooRun -m ex2.py:Benchmark2 adl_benchmarks.yml --prefix=ex2_ -o out_2 &> out_2.log || return 1
echo "Running ex3"
bambooRun -m ex3.py:Benchmark3 adl_benchmarks.yml --prefix=ex3_ -o out_3 &> out_3.log || return 1
echo "Running ex4"
bambooRun -m ex4.py:Benchmark4 adl_benchmarks.yml --prefix=ex4_ -o out_4 &> out_4.log || return 1
echo "Running ex5"
bambooRun -m ex5.py:Benchmark5 adl_benchmarks.yml --prefix=ex5_ -o out_5 &> out_5.log || return 1
echo "Running ex6"
bambooRun -m ex6.py:Benchmark6 adl_benchmarks.yml --prefix=ex6_ -o out_6 --threads=3 &> out_6.log || return 1
echo "Running ex7"
bambooRun -m ex7.py:Benchmark7 adl_benchmarks.yml --prefix=ex7_ -o out_7 &> out_7.log || return 1
echo "Running ex8"
bambooRun -m ex8.py:Benchmark8 adl_benchmarks.yml --prefix=ex8_ -o out_8 &> out_8.log || return 1
