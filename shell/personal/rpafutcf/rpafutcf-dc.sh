# The purpose of this script is to recurssively prints all files under current file
# The anthor of this script is sherlongqu

#!/bin/bash

# Define function
# Define a function "rpafutcf(recursively prints all files under the current file)"
function rpafutcf()
{
    for filename in `ls $1`
    do

		# Determine if "$1/${filename}" is a directory
        if test -d "$1/${filename}"
        then
        
            # Print the directory that will be printed recursively
            echo $1/$filename

            # Call function "rpafutcf" and take "$1/${filename}" as the "$1" parameter in the called function "rpafutcf"
            rpafutcf "$1/${filename}"
        else

			# Define local variable to limit the size of the print file
			# Define local variable "tsotlf(the size of the loaded file)"
			tsotlf=`ls -l $1/$filename | awk '{ print $5 }'`

			# Define local variable "tmpfs(the maximum printable file size)"
			tmpfs=$((1024*10))

			# Determine whether "tsotlf" is greater than "tmpfs"
			if test $tsotlf -lt $tmpfs
			then
			
				# Prints the full path of the file currently being printed
				echo $1/$filename

				# The start location of the file that is currently being printed
				printf '*%.0s' {1..100}
				echo "This file start(rpafutcf.sh)"

				# Print the file
				echo "$(cat "$1/$filename")"

				# Prints the end position of the file currently being printed
				printf '*%.0s' {1..90}
				echo "This file end(rpafutcf.sh)"
			else
			
			# Print the file name and file size information
			echo $1/$filename" file are larger than the limit maximum of "$tmpfs
			fi
        fi
    done
}

# Define variable
# Define a variable "tdd(the destination directory)"
# Determine whether parameters are entered,if so,"tdd" is set as the first input parmeter,and if not,"tdd" is set to the working directory
if [ $# -lt 1 ];
then
    tdd=$(pwd)
else
    tdd=$1
fi

# The script body
# Call the function "rpafutcf"
rpafutcf ${tdd}

# The bash commands used in this script are:"ls","echo","test","printf","cat","pwd","awk"
# The loop statement used in this script are:"if..then..else..fi","for..in..do..done"
# A functionand"rpafutcf" and parameter "tdd","tsotlf","tmpfs" are defined in the script
# This script is version 0.1.1