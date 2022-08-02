# Tax Calculator

[![Python Version][python-image]][python-url]


Design of a tax calculator based on stock market investment operations.

## Installation

### Environment Local

Using your dependency manager, create a python environment, follow a [link](https://ahmed-nafies.medium.com/pip-pipenv-poetry-or-conda-7d2398adbac9) talking about the managers!

Access the project folder and using the **pip** manager, inside the python env, apply the command below:

Upgrade pip version and install requirements and install:

```sh
pip install --upgrade pip && pip install --require-hashes -r requirements/dev.txt
```

After installing all dependencies,compile this project with command:

```sh
python manage.py calculate '[{"operation":"buy", "unit-cost":10.00, "quantity": 100},{"operation":"sell", "unit-cost":15.00, "quantity": 50},{"operation":"sell", "unit-cost":15.00, "quantity": 50}]'
```

### Docker Build

You will need to have docker-compose, and finally apply the command:

```sh
docker-compose up --build
```

After build project, in another terminal, apply the command:

```sh
docker exec -it tax-calculator python manage.py calculate '[{"operation":"buy", "unit-cost":10.00, "quantity": 100},{"operation":"sell", "unit-cost":15.00, "quantity": 50},{"operation":"sell", "unit-cost":15.00, "quantity": 50}]'
```

**Obs:**

* For practical use of the application it is necessary to add single quotes, making it a valid argument.
* For two arguments or more, follow the formatting premise of the input arguments above.
* Don't forget to create the environment variables file, as per the "env.example" file


## Dependencies

This project uses hashed dependencies. To update them, edit `requirements/base.in` for project dependencies and `requirements/dev.in` for development dependencies and run:
```sh
pip-compile --generate-hashes --output-file requirements/base.txt requirements/base.in && \
pip-compile --generate-hashes --output-file requirements/dev.txt requirements/dev.in
```
It is always necessary to `pip-compile` both because dev-deps references base-deps.

## Usage

In order to be able to normalize, we add the best practices in this project, aiming to respect the principles with example **Clean Code**, **SOLID** and others. For more details, see the tip links!


### Formatters and Linters

* [Flake8](https://flake8.pycqa.org/en/latest/index.html)
* [Black](https://black.readthedocs.io/en/stable/)
* [Isort](https://isort.readthedocs.io/en/latest/)
* [Bandit](https://bandit.readthedocs.io/en/latest/)
* [MyPy](https://mypy.readthedocs.io/en/stable/)

**Obs:**

* Programming with Python, we use the `snake_case` style for variables, functions and methods, and the `PascalCase` style for classes. Configuration variables should written in `UPPERCASE`.

### Structure

We use the **microservices architecture patterns** with **DDD principle**, to create system resources. To example, see the content:

```sh
.
├── app
│   ├── core
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── __init__.py
│   ├── models.py
│   ├── repository.py
│   └── services.py
├── docker-compose.yml
├── Dockerfile
├── env.example
├── manage.py
├── pyproject.toml
├── README.md
├── requirements
│   ├── base.in
│   ├── base.txt
│   ├── dev.in
│   └── dev.txt
└── tests
    ├── __init__.py
    ├── test_models.py
    ├── test_repository.py
    └── test_service.py

```

### Tests

In this application, we used this dependencies to perform, scan and cover tests in the application:

* [Interrogate](https://interrogate.readthedocs.io/en/latest/)
* [Coverage](https://coverage.readthedocs.io/en/6.3.2/)
* [Pytest](https://docs.pytest.org/en/6.2.x/)

In this application, unit tests were created, using **pytest**. Follow the instructions to run the tests:

* To see tests list

```sh
docker-compose run monopoly-challenge python manage.py runtest --list
```

* To run all test

```sh
docker-compose run monopoly-challenge python manage.py runtest
```

* To run only test module

```sh
docker-compose run monopoly-challenge python manage.py runtest -n <module_name>.py
```

* To run only function test module

```sh
docker-compose run monopoly-challenge python manage.py runtest -n <module_name>.py::<function_teste_name>
```
**Obs:**

* If you're not used to the docker-compose tool, you can change the prefix using ``docker exec -it project python manage.py runtest --help``
* Any doubts about the use or how pytest works, in the resources section we provide a direct link to the tool's documentation.



## Resources and Documentations

* [Pip (Package Installer Python)](https://pip.pypa.io/en/stable/)
* [Pre-commits](https://pre-commit.com/index.html)
* [Editor Config](https://editorconfig.org/)
* [Pip Tools](https://github.com/jazzband/pip-tools)
* [Click](https://click.palletsprojects.com/en/8.1.x/)
* [Docker](https://docs.docker.com/get-started/)
* [Docker Compose](https://docs.docker.com/compose/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

[python-url]: https://www.python.org/dev/peps/pep-0596/
[python-image]: https://img.shields.io/badge/python-v3.10-blue
