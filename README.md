# Python Notes

## General

### Naming conventions

* [Naming conventions of Python](https://www.python.org/dev/peps/pep-0008/#naming-conventions) from PEP 8

### How functions work

* [How to use \*args and \*\*kwargs in Python](https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/)
* [函數有無返回值？](https://www.ptt.cc/bbs/Python/M.1514366821.A.326.html)
* [Re: 函數有無返回值？](https://www.ptt.cc/bbs/Python/M.1514546205.A.FEE.html)

### Precedence

* [Operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
* [Boolean operations - `and`, `or`, `not`](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) for short-circuit operators.

## Getting help

* `help`. For instance, `help(len)`, or `help(tuple.index)` for known functions or methods.
* In IPython (e.g. Jupyter Notebook), `? len` also works.

## [Python standard library](https://docs.python.org/3/library/)

> While [The Python Language Reference](https://docs.python.org/3/reference/index.html) describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.

* [`venv`](https://docs.python.org/3/library/venv.html) provides a convinient way to creat "lightweight 'virtual environments'". Read [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html) for the official tutorial.

### [Built-in functions](https://docs.python.org/3/library/functions.html)

* `dir` returns all methods (attributes) of specified instance (object).
* `type` returns the data type of the object in Python.
* `import` is like `source` and `library` in R, sourcing packages or script files.
* `len` returns the length of the object. _(cf: `length` in R)_
* `set` returns unique values in the object, and that allows mathematical set operations. `list(set(a_list))` is a way to have unique values in the list `a_list`. _(cf: `unique` in R; `pandas.Series.unique` in pandas library)_
* `zip` returns a mapped iterable from multiple instances (objects).
* `enumerate` returns an enumerate object. It is useful with `itemgetter` in [`operator` module](https://docs.python.org/3/library/operator.html) when [finding maximum value and its index in a list](https://stackoverflow.com/questions/6193498/pythonic-way-to-find-maximum-value-and-its-index-in-a-list/).

## Assigning values

* `=`. `a = b` means that `a is b` is `True` and they share the same memory, i.e. changing a will change b. _(cf: `a = b` or `a <- b` in R copies b and assigns that to a, i.e. changing a won't change b. Read also [Use "<-" or "="](https://corytu.github.io/CourseraRMentoring/articles/use-equal-or-arrow.html).)_

## Comparison

* My Gist [comparison.py](https://gist.github.com/corytu/c4fbd7c330c8a33c45965c5cad16ab38) demonstrates the difference between `==` and `is`. Besides I mention `pd.DataFrame.equals` there for comparing DataFrames.

## Functions for programming

Unlike R, Python is usually __not__ a functional programming language. Still, these following functionalities provide essential help or comparison.

* `lambda` are Python's way of creating anonymous functions. This is unlike R.
  
  > You declare a lambda function with the word `lambda` followed by a list of arguments, followed by a colon and then a single expression and this is key. There's only one expression to be evaluated in a lambda. The expression value is returned on execution of the lambda.

* `map` is kind of like `sapply` in R. See [defining functions in R and Python](Defining_functions_in_R_and_Python.md) for an example.

## Useful packages (ordered alphabetically)

* [fancyimpute](https://pypi.python.org/pypi/fancyimpute/)

  > A variety of matrix completion and imputation algorithms implemented in Python including MICE and k-NN.

* [NumPy](http://www.numpy.org)

  > NumPy is the fundamental package for scientific computing with Python.

* [Pandas](https://pandas.pydata.org)

  > Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

  * See [Comparison with R / R libraries](https://pandas.pydata.org/pandas-docs/stable/comparison_with_r.html) for reference to equivalent functionality in R.
  * Check [my asked questions about `Pandas` on Stack Overflow](https://stackoverflow.com/search?q=user:6666231+[pandas]).

* [pipreqs](https://github.com/bndr/pipreqs)

  > Generate requirements.txt file for any project based on imports

* [regex](https://pypi.org/project/regex/)

  > This regex implementation is backwards-compatible with the standard 're' module, but offers additional functionality.

## Engineering tools using Python

* [docker](https://www.docker.com)
	* A scalable, VM-like solution
	* Official [getting started](https://docs.docker.com/get-started/)
	* [Python docker hub](https://hub.docker.com/_/python/) for getting Python environment in docker
	* [Personal notes of docker](docker_docs.md)