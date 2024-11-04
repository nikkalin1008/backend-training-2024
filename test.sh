# #!/bin/bash

# # Define a function to print a separator that matches the terminal width
# print_separator() {
#     local message=" $1 " # Get the function argument as the message
#     local term_width=$(tput cols) # Get the terminal width
#     local equals_width=$(( (term_width - ${#message}) / 2 )) # Calculate the number of equal signs

#     # Output the separator line
#     printf '%*s' "$equals_width" | tr ' ' '='
#     printf '%s' "$message"
#     printf '%*s\n' "$equals_width" | tr ' ' '='
# }

# print_separator "Check files change"
# sh ./.github/scripts/check_files.sh

# print_separator "Install requirements"
# cd "/mnt/app"
# pip install --quiet --no-cache-dir -r requirements.txt

print_separator "Run pytest"
cd /mnt
rm -rf test
mkdir test
cp -fr .github/scripts/* ./test/
cp -fr app/* ./test/
cd /mnt/test
#pytest




pytest test_homework4.py

rm -rf /mnt/test