# wid_hackathon
Women in Data Hackathon

==============================

Women in Data Hackathon

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │ ├── external       <- Data from third party sources.
    │ ├── interim        <- Intermediate data that has been transformed.
    │ ├── processed      <- The final, canonical data sets for modeling.
    │ └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default mkdocs project; see https://www.mkdocs.org/ for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

## Installation

Create a virtual environments
```bash
python -m venv /c/dev/virtual/wid-hack
```

Similar to pip, pip-tools must be installed in each of your project's virtual environments:
```bash
source /c/dev/virtual/wid-hack/Scripts/activate
python -m pip install pip-tools
pip-compile -o requirements.txt pyproject.toml
```

Simple instructions to action pre-commit hooks in this repo. See docs on  
pre-commit: https://github.com/pre-commit/pre-commit

```bash
source /c/dev/virtual/wid-hack/activate
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
