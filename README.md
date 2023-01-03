# Django to Docker Builder


### how to use?
You need to change the **<git_repo>** into your url of your git repository.
> ! If you want to include your own enviroment variables add a '.env' file in the current folder.
\
\
To build your docker container run **build_docker.ps1** in your PowerShell Terminal.
> Run your container with `docker run -d -p 8080:8000 --name django docker-django:dev_230103`
> **230103** needs to be replaced with the current datestamp.