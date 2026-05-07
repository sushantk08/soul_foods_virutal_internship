#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run pytest
pytest test_app.py

# Check pytest exit status
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed!"
    exit 1
fi