#!/bin/bash

# Initialize variables
ip_address=""
# Run adb devices and parse the output line by line
counter=0
while IFS= read -r line; do
    counter=$((counter + 1))
    if [ $counter -eq 2 ]; then
        ip_address=$(echo $line | awk '{print $1}')
        break
    fi
done < <(adb devices)

# Check if an IP address was found
if [ -z "$ip_address" ]; then
    echo "No device found."
    exit 1
fi


# Run the Python script with the IP address, width, and height
python3 /usr/lib/android-sdk/platform-tools/aatest.py $ip_address


