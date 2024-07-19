#!/bin/bash

# Directory containing WAV files
dir=~/alphabet_fixed

# Check if directory exists
if [ ! -d "$dir" ]; then
    echo "Directory $dir does not exist."
    exit 1
fi

# Loop through all WAV files in the directory
for file in "$dir"/*.wav; do
    echo "Playing $file ..."
    sudo aplay "$file"
    sleep 1
done

