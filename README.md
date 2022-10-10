# assignment2-docker
1. Demonstration of basic docker commands.
2. Import Hello World docker image from docker hub and run locally.
3. Create a hello world fastapi application. Create a Dockerfile for your fastapi hello world application. Build Docker image using Docker file. Run docker image built in previous step. Push your Docker image to Docker Hub.
4. Automate docker build and push to hub.

# Task 1 - Basic docker commands
## Import community docker image
Downloading docker image from remote docker hub using the pull command. For example, we'll use "getting-started" docker image.
In order to pull a specific version of that image, we can specify using "docker_image:version_name"
```
docker pull docker/getting-started
```
This command is available at the docker [repository]: https://hub.docker.com/r/docker/getting-started
![](snips/pull.jpg)

## View downloaded images
In order to check which images have been downloaded into the localmachine, we can do this.
```
docker images
```
![](snips/images.jpg)

## Run docker image
For a community shared docker image, there usually is a docker run command available at the repository page.
In the following command, -d represents detached mode that means the image will run in the background and not inside the terminal.
-p represents port assignment, which we can assign to the host and the container for communication.
80:80 represents the two port mentioned above, first one is for the host and second one is for the container.
```
docker run -d -p 80:80 docker/getting-started
```
As we specified -d, we don't get any interesting output because the container is running in the background.
![](snips/run.jpg)

## View running containers
In order to see which containers are actually runnning, we can do this.
A local host can have multiple images downloaded and multiple containers running at the same time. Each image corresponds to one container.
```
docker ps
```
Here we can see various container details such as container ID, docker image that created the container, status, ports etc.
![](snips/ps.jpg)

## View content inside container 
To see what is actually happening inside the container, we must open a URL with the specific ports mentioned during run command.
In the previous step, we can see that the docker is running on the IP address that matches the local host IP address. 0.0.0.0 signifies that whatever IP is mapped to the local host will be given to the container as well. Therefore, we can use the following URL in a web browser to see inside the container.
```
127.0.0.1:80
```
Here, 80 represents the host port set during the run command.
![](snips/getting-started.jpg)

## Stop container
To stop a running container, the following command can be used
```
docker stop eb4204d346c7
```
Here, the container ID specific to the local host machine is used. Each time the container is run, a different ID is issued to the container and that must be used to stop the container. The ID can be found using the "docker ps" command used previously.
The output simply shows the container ID when the container is stopped successfully.
![](snips/stop.jpg)

## Delete image
To delete a downloaded image from the local machine, its referenced container must be removed first. Although the container was stopped before but still it creates a conflict. Therefore a normal deletion of the image will result in an error.
```
docker rmi docker/getting-started
```
![](snips/delete-error.jpg)
To force this deletion, use the -f argument.
```
docker rmi -f docker/getting-started
```
![](snips/force-delete.jpg)

To delete the stopped container, we use "rm" to remove the container ID from our list of unused containers.
```
docker ps --filter status=exited -q
```
![](snips/filter.jpg)
```
docker rm 6eded07edad8
```
![](snips/delete-container.jpg)

Once this is done, we can simply delete the image.
![](snips/delete.jpg)

