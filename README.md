# Estimate One Tennis Tournament Scorer Coding Test

This is my submission for the Estimate One coding challenge.

## Dependencies

Python 3.8 and the [Venv](https://docs.python.org/3/library/venv.html) module.

For Ubuntu 20.04 this should be satisfied with:

```
sudo apt-get update
sudo apt-get install python3 python3-venv
```

There is an included Dockerfile should you want to use a containerised environment instead.

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

And you will have the following output:

```
Person C defeated Person A
2 sets to 1

23 17
```

There is a debug option which will print out the results and statistics for each match and player like this:

```
$ scorer tests/data/full_tournament.txt --debug
Person A defeated Person B
2 sets to 0
Person C defeated Person A
2 sets to 1

Person A stats: 23 17
Person B stats: 0 12
Person C stats: 17 11
```

Note: if you do not want to install developer and test dependencies, running `pip install .` will skip these.

## `full-tournament.txt`

As noted above, this file has been moved into test data directory because it is used as a fixture.

I found the results of processing the sample file to differ from sample output in the instructions. You can view the results of my manual review of the input data here:

`doc/manual full_tournament.txt reconciliation.pdf`.

## Docker

You can use the included Dockerfile to build an image with the processor preinstalled. `test-docker` does this for you then runs the tests in the new container.

## CI

This code is hosted in a [Github repository](https://github.com/cgspeck/estimateOne) and there is a Github Actions-based CI workflow setup that runs on every push.

You can view the workflow definition [here](.github/workflows/main.yml).
