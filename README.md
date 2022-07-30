# What

Swagger API Code generator and Git Repo Management for https://swagger.io/docs/open-source-tools/swagger-codegen/

* Generates the Swagger API client files
  * Provided by Swagger Codegen project
  * Includes documentation in some cases
  * https://github.com/swagger-api/swagger-codegen/blob/master/modules/swagger-codegen-maven-plugin/README.md
  * https://www.baeldung.com/spring-boot-rest-client-swagger-codegen
* Create a Git Repository based on the parameters provided
  * [x] Gitlab Repo Creation and Updates, Gitlab Package Registry Updates
  * [ ] Github Repo Creation and Updates, Github Package Registry updates
* Creates stubs in the supported languages
  * [x] Java -> Maven
  * [ ] Nodejs / Javascript -> NPM
  * [ ] Python -> PyPi
  * [x] Git -> Flutter
  * [ ] ...

[![asciicast](https://asciinema.org/a/Efs9Dx1lPem7ezfAidJJSNGfa.svg)](https://asciinema.org/a/Efs9Dx1lPem7ezfAidJJSNGfa)

# Why

* It's faster to get started and test client implementations
* It's a well-defined process and anyone can quickly iterate over it
* All the client APIs are published to both the git repo and the component repo

# How

* Create an `input.env` file with parameters
  * Use the `template-docker-compose.env`
* Invoke `docker-compose` with it and profit

# Setup

1. Download a client swagger docs json file

```console
$ curl -o parking-plus.json https://demonstracao.parkingplus.com.br/servicos/v2/api-docs
```

2. Create the env file, say `parking-plus.env` with the properties for swagger gen to generate code

> **NOTE**: These files must be on the same dir

```properties
#####
##### Swagger Gen Language settings
#####

# The name of the file downloaded from step 1 download
SCHEMA_FILE_NAME=parking-plus.json

#####
##### Source-code specific generation
#####

# The target language to generate the code
GENERATE_CLIENT_LANG=java

# The target library to be used for the selected code
GENERATE_CLIENT_WITH_LIBRARY=feign

# The packages for the generation framework for api, invoker, model, in this case
# java package where the code lives
GENERATE_CLIENT_MODEL_PACKAGE=cash.super_.platform.client.parkingplus.model
GENERATE_CLIENT_API_PACKAGE=cash.super_.platform.client.parkingplus.api
GENERATE_CLIENT_INVOKER_PACKAGE=cash.super_.platform.client.parkingplus.invoker

#####
##### Swagger Gen Packaging settings
#####

# The group id used for the package, in this case, java 
GENERATE_CLIENT_GROUPID=cash.super_.platform.client

# The name of the artifact of the package, in this case, java
GENERATE_CLIENT_ARTIFACT=parking-plus-client

# The version of the client... Will be SNAPSHOT by default
GENERATE_CLIENT_VERSION=2.0.0

#####
##### Swagger Gen Packaging and Version control for pushing automatically
#####

# CI/CD Settings for packages like java to include pom.xml (git repo) for ssh push
GENERATE_CLIENT_URL=https://gitlab.com/supercash/clients/parking-plus-client
GENERATE_CLIENT_GIT_HOST=gitlab.com
GENERATE_CLIENT_GIT_USER_REPO=supercash/clients/parking-plus-client
GENERATE_CLIENT_GIT_BRANCH=develop
GENERATE_CLIENT_GITLAB_PROJECT_ID=22268428

# The committer information that's recorded in the commit of new changes
GENERATE_CLIENT_AUTHOR_FULLNAME=Marcello de Sales
GENERATE_CLIENT_AUTHOR_EMAIL=marcello.desales@gmail.com

#####
##### Controls to push to git repo or publish to maven directly
#####

# Push code to the git repo when generating
GENERATE_CLIENT_GIT_PUSH=true

# Publish to maven directly if not done by CI/CD
# Uncomment if you don't have CI/CD to perform the publish
#GENERATE_CLIENT_PUBLISH_TOKEN=XyV******du9r
```

# Running

> **ATTENTION**: Make sure to copy the template `template-docker-compose.env` and set your own variables.

* Use docker-compose to run a container with the generation

```console
$ docker-compose --env-file parking-plus.env up --build
```

* Before running again, remove the previous container

```console
$ docker-compose --env-file parking-plus.env rm --force
Going to remove swagger-client-pacakge-repo-gen_swagger-client-repo-gen_1
Removing swagger-client-pacakge-repo-gen_swagger-client-repo-gen_1 ... done
```

# Development

* Send a PR if there's any problem you encounter!


