---
id: deploy-from-dockerhub
title: Deploy your service
---

The DSRI is an [OpenShift OKD](https://www.okd.io/) cluster, based on [Kubernetes](https://kubernetes.io/). It uses [Docker containers](https://www.docker.com) to deploy services and applications in **pods**.

## Find an image for your service

The easiest way to deploy a service on the DSRI is to use a Docker image from [DockerHub 🐳](https://hub.docker.com/).

Search for an image for your service published on [DockerHub](https://hub.docker.com/)

* [Google "dockerhub my_service_name"](https://www.google.com/search?q=dockerhub+python)
* Sometime different users deployed a different image for your service. Take the most relevant one for your use-case.

> If no suitable image can be found on [DockerHub](https://hub.docker.com/), it can be built from a Dockerfile.

## Build and push a new image

To build and push a Docker image you will need to have [Docker installed](https://docs.docker.com/get-docker/).

> See the [official Docker documentation](https://docs.docker.com/get-docker/).

> See [this documentation for details about Docker installation on Linux, MacOS and Windows](https://d2s.semanticscience.org/docs/d2s-installation#install-docker) without the need for a DockerHub account (required to use Docker Desktop on MacOS and Windows)

### Define a Dockerfile

If no images are available on DockerHub, it is still possible that the developers created the [Dockerfile to build the image](https://docs.docker.com/engine/reference/builder/) without pushing it to DockerHub. Go to the GitHub/GitLab source code repository and search for a `Dockerfile`, it can usually be found in

* the source code repository root folder
* a `docker` subfolder
* as instructions in the `README.md`

If no `Dockerfile` are available we will need to define one. 

> Feel free to [contact us](/help) to get help with this, especially if you are unfamiliar with [Docker](https://docs.docker.com/get-started/).

### Build the image

Once a Dockerfile has been defined for the service you can build it by running the following command from the source code root folder, where the Dockerfile is:

```shell
docker build -t username/my-service .
```

Arguments can be provided when starting the build, they need to be defined in the Dockerfile to be used.

```shell
docker build -t username/my-service --build-args MY_ARG=my_value .
```

### Push to DockerHub

Before pushing it to DockerHub you will need to create a repository. To do so, click on **[Create Repository](https://hub.docker.com/repository/create)**.

* DockerHub is free for public repositories
* Images can be published under your DockerHub user or an organization you belong to

Login to DockerHub, if not already done:

```shell
docker login
```

Push the image previously built to DockerHub:

```shell
docker push username/my-service
```

You can link DockerHub to your source code repository and ask it to build the Docker image automatically (from the Dockerfile in the root folder). It should take between 10 and 30min for DockerHub to build your image

> You can also deploy a service on the DSRI directly from the Dockerfile, to avoid using DockerHub. See [this page to deploy a service from a local Dockerfile](/dsri-documentation/docs/guide-dockerfile-to-openshift) for more instructions