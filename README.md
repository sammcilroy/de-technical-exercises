![.github/workflows/ci-workflow.yaml](https://github.com/pcandoalmeida/de-technical-exercises/workflows/.github/workflows/ci-workflow.yaml/badge.svg)

# Data Engineering Technical Exercises
* Loading data directly into memory is not ideal; this would need to be revised; could we get guarantees on processing?
* Want to explore multiprocessing to parallelize ingestion and computation; alternatively computing engine such as Spark
* Wanted to try OOP -- please disect, criticise, comment on!
* Simple profiling solution implemented; exploring better tools such as cProfile
* Only basic tests provided!

## How To Run

The demo.py file will profile the calculation methods. Tests file paths will need to be amended as right now they are designed to run via Githib Actions.

Piplock file(s) included so recommended to use pipenv to create a virtual environment. `pipenv install` and `pipenv run demo.py` should do the trick in the cloned repository.
