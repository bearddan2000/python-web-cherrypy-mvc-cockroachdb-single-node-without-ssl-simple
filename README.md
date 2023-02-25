# python-web-cherrypy-mvc-cockroachdb-single-node-without-ssl-simple

## Description
Creates a mvc dataTable of `dog` for a cherrypy project.

A python cherrypy build, that connects to single node cluster
cockroach database without ssl.

If path is not found, will default to 404 error.

## Tech stack
- python
  - cherrypy
  - sqlalchemy
- bootstrap
- jquery
- dataTable
- cockroachdb

## Docker stack
- python:latest
- cockroachdb/cockroach:v19.2.4

## To run
`sudo ./install.sh -u`
- [web app](http://localhost)
- [node webui](http://localhost:8000)

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- [Cockroach setup](https://github.com/s0rg/cockroach-compose)
