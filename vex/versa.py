#!/usr/local/bin/python3
import sys
sys.path.insert(1, "docker-adds")

import docker_helper
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
parser.add_argument("-status", action="store_true", help="Displays the status of all registered containers")
parser.add_argument("-containers", action="store_true", help="Lists all docker containers")

parser.add_argument("-start", type=str, nargs="+", help="list of docker containers to start")
parser.add_argument("-stop", type=str, nargs="+", help="list of docker containers to stop")
parser.add_argument("-restart", type=str, nargs="+", help="list of docker containers to restart")

args = parser.parse_args()

print()

if args.verbose:
    print("Python version {}".format(sys.version))
    print()

if args.containers:
    docker_helper.list()

if args.status:
    print("printing the status...")

if args.start:
    for container_name in args.start:
        docker_helper.start("mongo", container_name, "C8H10N4O2")

if args.stop:
    for container_name in args.stop:
        docker_helper.stop(container_name)

if args.restart:
    for container_name in args.restart:
        docker_helper.restart(container_name)

print()
print()