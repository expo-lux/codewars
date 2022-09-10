#!/usr/bin/env bash
#https://www.codewars.com/kata/54d512e62a5e54c96200019e
set -eu

primeFactors() {
    cols="$(factor $(($1)) | cut -d' ' -f2-  | tr ' ' '\n' | uniq -c )"
    echo "$cols" | awk '{ if ($1 == 1 ) { printf "("$2")" } else { printf "("$2"**"$1")"} } END { printf "\n" }'
}

primeFactors 7775460
primeFactors 7919
primeFactors 17*17*93*677