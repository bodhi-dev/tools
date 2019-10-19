#!/usr/local/bin/python3
import docker

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

def list():
    containers = client.containers.list()
    for container in containers:
        print("Container: {}".format(container.name))

def stop(name):
    print("Stopping container {}...".format(name))
    container = client.containers.get(name)
    container.stop()

def start(image, name, network):
    print("Staring container {}...".format(name))
    client.containers.run(
        image,
        detach=True,
        name=name,
        network=network)

def restart(name):
    print("Restarting container {}...".format(name))

