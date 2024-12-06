#!/bin/sh -e

set -x

time uv run python -X gil=1 -m free_threading_examples.example1
time uv run python -X gil=0 -m free_threading_examples.example1
time uv run python -X gil=1 -m free_threading_examples.example2
time uv run python -X gil=0 -m free_threading_examples.example2
time uv run python -X gil=1 -m free_threading_examples.example3
time uv run python -X gil=0 -m free_threading_examples.example3

rm -f tmp/*.txt
