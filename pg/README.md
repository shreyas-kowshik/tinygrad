Getting basic stuff to run

`CLANG=1 python pg/hw.py`

### Put in OneNote later on

`mean()` is simply a sum across axes `one at a time`
So in case multiple ReduceOps.SUM come in when doing a `mean` then notice that it happens per axis in terms of reduction of tensor

`toCPU()` brings data from a device to CPU or numpy that can be printed now

0 UOps.DEFINE_GLOBAL  : ptr.dtypes.float          []                               data0
   1 UOps.DEFINE_GLOBAL  : ptr.dtypes.float          []                               data1
   2 UOps.DEFINE_GLOBAL  : ptr.dtypes.float          []                               data2
   3 UOps.CONST          : dtypes.int                []                               0
   4 UOps.CONST          : dtypes.int                []                               262144
   5 UOps.CONST          : dtypes.int                []                               4
   6 UOps.CONST          : dtypes.int                []                               1
   7 UOps.CONST          : dtypes.int                []                               2
   8 UOps.CONST          : dtypes.int                []                               3
   9 UOps.LOOP           : dtypes.int                [3, 4]                           None
  10 UOps.ALU            : dtypes.int                [9, 5]                           BinaryOps.MUL
  11 UOps.LOAD           : dtypes.float              [1, 10]                          None
  12 UOps.ALU            : dtypes.int                [10, 6]                          BinaryOps.ADD
  13 UOps.LOAD           : dtypes.float              [1, 12]                          None

Above first column is the Uop, second is the data type (ptr.dtype.float specifies float*), third column is the UOps IDs that the current UOp references (for example UOps.LOOP has one variable ranging from 0 to 262144 which are the IDs 3,4 which is in [3,4])

Currently it looks like only one reduce is allowed per kernel and as soon as two reductions are introduced, a `realize()` is placed in the graph as a kernel needs to be compiled and output needs to be saved as a consequence

Next steps
Understand the kernels and the code for the readme_example.py modified file and see what all operations have been grouped into one kernel