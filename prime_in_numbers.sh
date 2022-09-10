#!/usr/bin/env bash
#https://www.codewars.com/kata/54d512e62a5e54c96200019e
set -eu

primeFactors() {
    arg=$(($1))
    factors=$(factor "$arg")
    factors=${factors//"$arg: "}
    res="$(echo "$factors" | tr ' ' '\n' | uniq -c)"
    f=""
    while IFS= read -r line
    do 
        base="$(echo "$line" | xargs | cut -d ' ' -f 2)"
        power="$(echo "$line" | xargs | cut -d ' ' -f 1)"
        if [[ power -gt 1 ]]; then
            f+="(${base}**${power})"
        else
            f+="(${base})"
        fi
    done <<< "$res"
    echo "$f"
}

primeFactors 7775460
primeFactors 7919
primeFactors 17*17*93*677



#IFS=$' '; r=( $(factor 7775460 | cut -d ' ' -f 2-) )
#res="$(factor 7775460 | cut -d ' ' -f 2- | tr ' ' '\n' | uniq -c)"
#IFS=$'\n'; power=( $(echo "$res" | awk '{print $1}') )
