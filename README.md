# Example StarterProject
A **starter project** to show how to set up and use automated testing in Python

![Tests](https://github.com/tobibias/starter-project/actions/workflows/tests.yml/badge.svg)
![PyPi_Version](https://img.shields.io/pypi/v/lckr-jupyterlab-variableinspector)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---
## Background

- Use Black auto-formatter to avoid arguing over formatting.
- Run pylint over your code using included [pylintrc](pylintrc).
- Use [Poetry](https://python-poetry.org/) as your tool for **dependency management** and **packaging** in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.

## Example
<p align="center">
<img src="https://user-images.githubusercontent.com/8370623/180626875-fe958128-6102-4f01-9ca4-e3a30c3148f9.png" width=100% height=100% 
class="center">
</p>

## Catalog
- [x] Code ... check
- [ ] TODO


## Results
### Example Table

|    name    | resolution | acc@1 | #params | FLOPs |     model     |
| :--------: | :--------: | :---: | :-----: | :---: | :-----------: |
| ConvNeXt-T |  224x224   | 82.1  |   28M   | 4.5G  | [model](TODO) |
| ConvNeXt-S |  224x224   | 83.1  |   50M   | 8.7G  | [model](TODO) |


## Installation

Install with poetry
```
poetry install
```


Install with development packages
```
poetry install --with dev
```
## Basic Poetry commands

Using poetry run
```
poetry run python run.py
```

### Development
```
poetry run pytest
```

```
poetry run pylint src
```

```
poetry run mypy src
```

Activate interactive shell inside virtual env
```
poetry shell
```

## License
This project is released under the MIT license. Please see the [LICENSE](LICENSE)
file for more information.

## Citation
If you find this repository helpful, please consider citing:
```
@Article{todo,
  author  = ...
}
```