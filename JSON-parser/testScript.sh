#! /bin/bash

# Define the directory (change as needed)
DIR="./test"

# Loop through all files in the directory
for file in "$DIR"/*; do
    # Ensure it's a file
    if [ -f "$file" ]; then
        # Pipe the content into script.py
        echo "$file"
        cat "$file" | ./script.py
    fi
done

