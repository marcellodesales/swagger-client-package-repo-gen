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

# Running

> **ATTENTION**: Make sure to copy the template `template-docker-compose.env` and set your own variables.

* Use docker-compose to run a container with the generation

```console
$ curl -o parking-plus.json https://demonstracao.parkingplus.com.br/servicos/v2/api-docs
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


