# RaspberryPi client for the Doorman project

## Requirements
* runs on Python 2.7
* `mysql-oonnector-python` to connect to the sql server
* `RPi.GPIO` usually pre-installed on python2.7 raspbian

## Configuration
This requires MySQL ssl to run, thus in `/door/db/ssl` the following files are expected:

* `ca-cert.pem`
* `client-cert.pem`
* `client-key.pem`

Also, the program expects to find a configuration file `/door/config.cfg` like this:

    [mysql]
    user = door
    pass = password
    host = 127.0.0.1
    port = 3306
    database = door
    ssl = False
