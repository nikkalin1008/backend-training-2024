#!/bin/bash

# Check if there is a parent commit (to prevent errors on the first commit)
if git rev-parse --verify HEAD^ >/dev/null 2>&1; then
  # If there is a parent commit, perform a diff
  MODIFIED_FILES=$(git diff --name-only HEAD^ HEAD)
else
  # If this is the first commit, list the files in the current commit
  MODIFIED_FILES=$(git ls-tree --name-only -r HEAD)
fi

echo "Modified files:"
echo "$MODIFIED_FILES"

# Check if there are files outside the 'members/' directory that were modified
NON_MEMBER_FILES=$(echo "$MODIFIED_FILES" | grep -v '^members/')

if [ -n "$NON_MEMBER_FILES" ]; then
  echo "Error: The following non-members/ files were modified:"
  echo "$NON_MEMBER_FILES"
  exit 1
else
  echo "Only members/ directory was modified. Proceeding..."
fi
