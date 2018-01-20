# Personal-Python-Notes
## Getting help
* `help`. For instance, `help(len)`, or `help(tuple.index)` for known functions or methods.
* `dir`. For instance, `dir(list)` for all methods for lists.
* [函數有無返回值？](https://www.ptt.cc/bbs/Python/M.1514366821.A.326.html)
* [Re: 函數有無返回值？](https://www.ptt.cc/bbs/Python/M.1514546205.A.FEE.html)

## Assigning values
* `=`. `a = b` means that `a is b` is `True` and they share the same memory, i.e. changing a will change b. _(cf: `a = b` or `a <- b` in R copies b and assigns that to a, i.e. changing a won't change b. Read also [Use "<-" or "="](https://corytu.github.io/Coursera-R-Mentoring/use-equal-or-arrow.html).)_

## Basic functions
* `type` for getting the data type of the object in Python.
* `len` for getting the length of the object. _(cf: `length` in R)_
* `set` for getting unique values in the object. _(cf: `unique` in R; `pandas.Series.unique` in pandas library)_

## Comparison
* My Gist [comparison.py](https://gist.github.com/corytu/c4fbd7c330c8a33c45965c5cad16ab38) demonstrates the difference between `==` and `is`. Besides I mention `pd.DataFrame.equals` there for comparing DataFrames.

## Functions for programming
* `lambda`s are Python's way of creating anonymous functions. This is unlike R. "You declare a lambda function with the word `lambda` followed by a list of arguments, followed by a colon and then a single expression and this is key. There's only one expression to be evaluated in a lambda. The expression value is returned on execution of the lambda." Click [here](Defining_functions_in_R_and_Python.md) for detailed comparison of R and Python.

## Functions do loops or parallel operations
* `map` is kind of like `sapply` in R. See [defining functions in R and Python](Defining_functions_in_R_and_Python.md) for an example.

## Useful packages (ordered alphabetically)
* [fancyimpute](https://pypi.python.org/pypi/fancyimpute/0.3.0)<br>
"A variety of matrix completion and imputation algorithms implemented in Python," including MICE and k-NN.
* [NumPy](http://www.numpy.org)<br>
"NumPy is the fundamental package for scientific computing with Python."
* [Pandas](https://pandas.pydata.org)<br>
"pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language."

## Stack Overflow threads
### Python in general
* [Create list with numbers between 2 values](https://stackoverflow.com/questions/18265935/python-create-list-with-numbers-between-2-values)
* [Should a return statement have parentheses?](https://stackoverflow.com/questions/4978567/should-a-return-statement-have-parentheses)
* [How to use \*args and \*\*kwargs in Python](https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/)

### NumPy
* [Index multiple, non-adjacent ranges in numpy](https://stackoverflow.com/questions/34188620/index-multiple-non-adjacent-ranges-in-numpy): `np.r_`
* [Slicing multiple, non-contiguous rows and columns from a numpy array or matrix](https://www.reddit.com/r/learnpython/comments/33buya/slicing_multiple_noncontiguous_rows_and_columns/): `np.ix_`

### Pandas
* [Find element's index in Pandas Series](https://stackoverflow.com/questions/18327624/find-elements-index-in-pandas-series)
* [How to determine whether a Pandas column contains a particular value](https://stackoverflow.com/questions/21319929/how-to-determine-whether-a-pandas-column-contains-a-particular-value)
* [Renaming columns in pandas](https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas/46912050): `pd.DataFrame.rename`, `pd.DataFrame.set_axis`, or assign values to `pd.DataFrame.columns` (can't be part of method chain though)
* [Select one cell when pandas DataFrame has hierarchical index](https://stackoverflow.com/questions/35611786/select-one-cell-when-pandas-dataframe-has-hierarchical-index): Use a tuple to wrap the multiple indexes
* [Select two sets of columns by column names in Pandas](https://stackoverflow.com/questions/48356052/select-two-sets-of-columns-by-column-names-in-pandas)
