#!/bin/bash

# Run pytest benchmark. Results are saved in .benchmarks
pytest tests/test_matching_engine.py::TestMatchingEngine::test_matching_with_benchmark \
  --dist no \
  --benchmark-enable \
  --benchmark-autosave

# Compare saved results
pytest-benchmark compare
