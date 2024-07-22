#!/bin/bash

# Directory containing the WAV files
input_dir=~/audio-alphabet

# Create an output directory if it doesn't exist
output_dir=~/alphabet_fixed
mkdir -p "$output_dir"

# Loop through all WAV files in the input directory
for input_file in "$input_dir"/*.wav; do
    # Get the base name of the file (without path and extension)
    base_name=$(basename "$input_file" .wav)
    
    # Define the output file path
    output_file="$output_dir/${base_name}_fixed.wav"
    
    # Convert the file
    ffmpeg -i "$input_file" -c:a pcm_s16le "$output_file"
    
    # Print the conversion status
    if [ $? -eq 0 ]; then
        echo "Converted $input_file to $output_file successfully."
    else
        echo "Failed to convert $input_file."
    fi
done

