# Django to Docker Builder


### how to use?
Add your Git-Repo URL to the <i>build_docker.ps1 | build_docker.sh</i> as first parameter.
> ! If you want to include your own enviroment variables add a '.env' file in the current folder.
<br></br>
To build your docker container run **build_docker.ps1** or **build_docker.sh** in your Terminal.
> Run your container with `docker run -d -p 8080:8000 --name django docker-django:dev_230103`
> **230103** needs to be replaced with the current datestamp.
