#!/bin/bash
rm -rf git_clone/*
git clone $1 git_clone
cd git_clone
git submodule update --init --recursive -j 4
cd ..
docker build --no-cache -t docker-django:dev_$(Get-Date -format "yyMMdd") .
rm -rf git_clone/*; echo "" > git_clone/.gitkeep