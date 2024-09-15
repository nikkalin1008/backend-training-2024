#!/bin/bash

DIVIDER="---"

# Copy test files into project
echo "Copy test files into project"
echo "$DIVIDER"
cp -r ./.github/scripts/* ./app/
echo "$DIVIDER"

# Execute check_files.sh
echo "$DIVIDER"
echo "Check Files Change"
echo "$DIVIDER"
./.github/scripts/check_files.sh
echo "$DIVIDER"

# Run pytest tests
echo "$DIVIDER"
echo "Pytest"
echo "$DIVIDER"
docker exec -it fastapi_app pytest --tb=long
echo "$DIVIDER"

echo "$DIVIDER"
echo "All tests passed successfully."
echo "$DIVIDER"