#!/bin/bash

function rpafutcf()
{
    for filename in `ls $1`
    do
        if test -d "$1/${filename}"
        then
            echo $1/$filename
            rpafutcf "$1/${filename}"
        else
			tsotlf=`ls -l $1/$filename | awk '{ print $5 }'`
			tmpfs=$((1024*10))
			if test $tsotlf -lt $tmpfs
			then
				echo $1/$filename
				printf '*%.0s' {1..100}
				echo "This file start(rpafutcf.sh)"
				echo "$(cat "$1/$filename")"
				printf '*%.0s' {1..90}
				echo "This file end(rpafutcf.sh)"
			else
			echo $1/$filename" file are larger than the limit maximum of "$tmpfs
			fi
        fi
    done
}
if [ $# -lt 1 ];
then
    tdd=$(pwd)
else
    tdd=$1
fi
rpafutcf ${tdd}