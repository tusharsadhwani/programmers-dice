# Programmers' dice

Generates excuses for programmers.

Inspired by this product: https://pretendstore.co/products/pocket-developer

## Installation

```bash
pip install programmers_dice
```

## Usage

In your terminal, type `roll` to get an excuse:

```console
$ roll
Ctrl+Shift+R should fix it.
```

Or, type `roll --count N` for `N` excuses to choose from!

```console
$ roll -c 3
My wrist hurts.
It's a feature.
Clear your cache.
```

## Local Development / Testing

- Create and activate a virtual environment
- Run `pip install -r requirements-dev.txt` to do an editable install
- Run `pytest` to run tests

## Type Checking

Run `mypy .`

## Create and upload a package to PyPI

Make sure to bump the version in `setup.cfg`.

Then run the following commands:

```bash
rm -rf build dist
python setup.py sdist bdist_wheel
```

Then upload it to PyPI using [twine](https://twine.readthedocs.io/en/latest/#installation):

```bash
twine upload dist/*
```
