# Estimate One Tennis Tournament Scorer Coding Test

This is my submission for the Estimate One coding challenge.

## Dependencies

Python 3.8 and Virtualenv.

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

If you run this without any queries then it will print out the results and statistics for each match and player.

Note: if you do not want to install developer and test dependencies, running `pip install .` will skip these.

## Docker

You can use the included Dockerfile to build an image with the processor preinstalled. `test-docker` does this for you then runs the tests in the new container.
