Remove-Item -Force -Recurse git_clone/*
git clone $args[0] git_clone
cd git_clone
git submodule update --init --recursive -j 4
cd ..
docker build --no-cache -t docker-django:dev_$(Get-Date -format "yyMMdd") .
Remove-Item -Force -Recurse git_clone/*; echo "" > git_clone/.gitkeep