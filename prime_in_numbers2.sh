#!/usr/bin/env bash
#https://www.codewars.com/kata/54d512e62a5e54c96200019e
set -eu

primeFactors() {
    arg=$(($1))
    res="$(factor "$arg" | cut -d ' ' -f 2- | tr ' ' '\n' | uniq -c)"
    IFS=$'\n'; s=''
    power=( $(echo "$res" | awk '{print $1}') )
    base=( $(echo "$res" | awk '{print $2}') )
    for i in ${!power[*]}
    do
        if [[ ${power[$i]} -gt 1 ]]; then
            s+="(${base[$i]}**${power[$i]})"
        else
            s+="(${base[$i]})"
        fi
    done
    echo $s
}


primeFactors 7775460
primeFactors 7919
primeFactors 17*17*93*677
