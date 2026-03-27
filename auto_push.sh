#!/bin/bash

git status --porcelain | while IFS= read -r line
do
    file=$(echo "$line" | awk '{print $2}')

    echo "Processing: $file"

    # Add file
    git add "$file"

    # Check if anything staged
    if git diff --cached --quiet; then
        echo "No changes for $file"
        continue
    fi

    # Commit
    git commit -m "Update $file"

    # Push
    git push origin master

    echo "$file added, committed, and pushed"
    echo "-------------------------------"

done