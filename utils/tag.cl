#!/bin/sh
if git status --porcelain | grep "^ M"
then
    printf "found uncommitted changes!\n"
    exit 223
fi
git_tags=$(git log --tags --simplify-by-decoration --pretty="format:%d")
last_tag=$( echo $git_tags | cut -f1 -d")")
last_version=$(echo $last_tag | cut -f3 -d" " | sed -e 's/[,)]$//')
version=$(grep version setup.py | cut -f2 -d"'")
if test $last_version != $version; 
then
    git tag -a $version
fi
