# Estimate One Tennis Tournament Scorer Coding Test

This is my submission for the Estimate One coding challenge.

## Dependencies

Python3 and Virtualenv.

## Local Development

Create a virtualenv and run install the requirements:

```
python3 -m venv venv
source ./venv/bin/activate
pip install -e .[dev]
```

Run the tests:

```
./test
```

## Using the Processor

Run the tournament scorer like so:

```
scorer tests/data/full_tournament.txt << EOF
Score Match 02
Games Player Person A
EOF
```

Note: if you do not want to install developer and test dependencies, running `pip install .` will skip these.
