## Docker image for Selenium Hub

* [selenium](http://docs.seleniumhq.org/)
* Forked from https://github.com/lzhang/docker-selenium

## Install

Either git pull and build this docker image yourself, or pull down the version you need from the docker index.

```sh
$ sudo docker pull momer/docker-selenium-hub:1.0.0
```
(note: Replace 1.0.0 with up-to-date version if any, check [DockerHub page](https://registry.hub.docker.com/u/momer/docker-selenium-hub/tags/manage/) for more info about this image)

## Start

This was designed to work with [MaestroNG](https://github.com/signalfuse/maestro-ng). You can either set your container to use that, or, start this container by passing the necessary environment variables:

```sh
$ SELENIUM_CONTAINER=$(sudo docker run -e "SELENIUM_HUB_PORT=4444" -e "SELENIUM_HUB_TIMEOUT=300000" -e "SELENIUM_HUB_MAX_SESSION=15" -p 4444:4444 -d momer/selenium:`version`)
```

Selenium hub is now available on port 4444 at the host and container.
