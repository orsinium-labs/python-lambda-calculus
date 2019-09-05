<h1 align="center">λ</h1>

## Lambda Calculus functions implemented on Python

[Lambda Calculus](https://en.wikipedia.org/wiki/Lambda_calculus) is a kind of mathematical game when you're implementing programming language with only functions that accept exactly one argument and returns exactly one value. Such function named "lambda". Thing is lambda can return another lambda, and it allows you to build everything, even [numbers](https://en.wikipedia.org/wiki/Church_encoding).

This repository contains [lambdas](./lambdas/) with implemented lambdas and [tests](./tests/) with pytest-based tests for it. To run tests execute `pytest`.

Implemented:

1. Boolean operations: [code](./lambdas/_bool.py), [tests](./tests/test_bool.py).
1. Natural numbers: [code](./lambdas/_natural.py), [tests](./tests/test_natural.py).
1. Pair: [code](./lambdas/_pair.py), [tests](./tests/test_pair.py).
1. Combinators: [code](./lambdas/_bool.py), [tests](./tests/test_bool.py).
1. Recursive functions: [code](./lambdas/_recursive.py), [tests](./tests/test_recursive.py).
1. Signed numbers: [code](./lambdas/_signed.py), [tests](./tests/test_signed.py).
1. Lists: [code](./lambdas/_list.py), [tests](./tests/test_list.py).

The list below is in order of the recommend implementation. It's recommend to try to do it by yourself, and use this repository as a cheatsheet.

## Read more

* [Lambda Calculus on Wikipedia](https://en.wikipedia.org/wiki/Lambda_calculus)
* [Church Encoding on Wikipedia](https://en.wikipedia.org/wiki/Church_encoding)
* [Lambda Calculus David Beazley's screencast](https://youtu.be/5C6sv7-eTKg)
* [JS implementation of some lambdas](https://github.com/gtramontina/lambda)
* Computerphile videos:
    * [Lambda Calculus](https://youtu.be/eis11j_iGMs)
    * [What is a Monad?](https://youtu.be/t1e8gqXLbsU)
    * [Functional Programming's Y Combinator](https://youtu.be/9T8A89jgeTI)
