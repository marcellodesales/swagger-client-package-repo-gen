# What

* Generates the Swagger API client files
  * Provided by Swagger Codegen project
  * Includes documentation in some cases
  * https://github.com/swagger-api/swagger-codegen/blob/master/modules/swagger-codegen-maven-plugin/README.md
  * https://www.baeldung.com/spring-boot-rest-client-swagger-codegen
* Commits code and Publishes the Git repo to a Git repository
* Publishes the packaging to a Package repository
  * [x] Java -> Maven
  * [ ] Nodejs / Javascript -> NPM
  * [ ] Python -> PyPi
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
$ docker-compose --env-file parking-plus.env up --build
```

* Before running again, remove the previous container

```console
$ docker-compose --env-file parking-plus.env rm --force
Going to remove swagger-client-pacakge-repo-gen_swagger-client-repo-gen_1
Removing swagger-client-pacakge-repo-gen_swagger-client-repo-gen_1 ... done
```

# Examples

## New Repo

* When creating a new Client API

```console
$ docker-compose --env-file parking-plus.env up
Using marcellodesales/swagger-client-package-repo-gen:latest
Attaching to swagger-code-and-repo-gen_swagger-client-generator_1
swagger-client-generator_1  | 👽 Generate the sources from parking-plus-schema.json in java using library feign
swagger-client-generator_1  |
swagger-client-generator_1  | [INFO] Scanning for projects...
swagger-client-generator_1  | [INFO]
swagger-client-generator_1  | [INFO] ---------------------< io.swagger:sample-project >----------------------
swagger-client-generator_1  | [INFO] Building sample-project 1.0-SNAPSHOT
swagger-client-generator_1  | [INFO] --------------------------------[ jar ]---------------------------------
swagger-client-generator_1  | [INFO]
swagger-client-generator_1  | [INFO] --- swagger-codegen-maven-plugin:2.4.17:generate (default) @ sample-project ---
swagger-client-generator_1  | [INFO] reading from /schemas/parking-plus-schema.json
swagger-client-generator_1  | [WARNING] Output directory does not exist, or is inaccessible. No file (.swagger-codegen-ignore) will be evaluated.
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/AutenticacaoResponse.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCnpj.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCpf.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/DadosEndereco.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/NotaInfo.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoAutorizadoRequest.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCartaoDebitoRequest.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCredenciadoRequest.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoEfetuado.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoRequest.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/Promocao.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoConsulta.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoCreditarCartao.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoErro.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoPagamento.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/TicketRequest.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2Api.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/test/java/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2ApiTest.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2Api.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/test/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2ApiTest.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/test/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2ApiTest.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/pom.xml
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/README.md
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/build.gradle
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/build.sbt
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/settings.gradle
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/gradle.properties
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/AndroidManifest.xml
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/.travis.yml
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/StringUtil.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/HttpBasicAuth.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/ApiKeyAuth.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/OAuth.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/OAuthFlow.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/gradlew
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/gradlew.bat
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/gradle/wrapper/gradle-wrapper.properties
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/gradle/wrapper/gradle-wrapper.jar
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/git_push.sh
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/.gitignore
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ParamExpander.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/EncodingUtils.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/RFC3339DateFormat.java
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/.swagger-codegen-ignore
swagger-client-generator_1  | [INFO] writing file /generator/springboot-client-api/.swagger-codegen/VERSION
swagger-client-generator_1  | [INFO] ------------------------------------------------------------------------
swagger-client-generator_1  | [INFO] BUILD SUCCESS
swagger-client-generator_1  | [INFO] ------------------------------------------------------------------------
swagger-client-generator_1  | [INFO] Total time:  2.163 s
swagger-client-generator_1  | [INFO] Finished at: 2020-11-06T03:48:42Z
swagger-client-generator_1  | [INFO] ------------------------------------------------------------------------
swagger-client-generator_1  |
swagger-client-generator_1  | 🏗  Updating client metadata and files for CI/CD for java
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}groupId = cash.super_.platform.client
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}artifactId = parking-plus-client-feign
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}name = parking-plus-client-feign
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}version = 1.0.0-SNAPSHOT
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}url = https://gitlab.com/supercash/clients/parking-plus-client-feign
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}description = Swagger feign Client stubs
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}connection = scm:git:git@gitlab.com:supercash/clients/parking-plus-client-feign.git
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}developerConnection = scm:git:git@gitlab.com:supercash/clients/parking-plus-client-feign.git
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}url = https://gitlab.com/supercash/clients/parking-plus-client-feign
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}name = Marcello de Sales
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}email = marcello.desales@gmail.com
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}organization = supercash
swagger-client-generator_1  | Set {http://maven.apache.org/POM/4.0.0}organizationUrl = https://gitlab.com/supercash
swagger-client-generator_1  |
swagger-client-generator_1  | 🚧 Generating CI/CD artifacts for Gitlab Project 22268428
swagger-client-generator_1  | - Adding ci_settings.xml
swagger-client-generator_1  | - Adding personal_settings.xml
swagger-client-generator_1  | - Adding .gitlab-ci.yml
swagger-client-generator_1  | - Generating the maven repos in Maven for Gitlab
swagger-client-generator_1  |
swagger-client-generator_1  | 🏺 Generating client jars from stubs
swagger-client-generator_1  | [INFO] Scanning for projects...
swagger-client-generator_1  | [INFO]
swagger-client-generator_1  | [INFO] -------< cash.super_.platform.client:parking-plus-client-feign >--------
swagger-client-generator_1  | [INFO] Building parking-plus-client-feign 1.0.0-SNAPSHOT
swagger-client-generator_1  | [INFO] --------------------------------[ jar ]---------------------------------
swagger-client-generator_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-compress/1.11/commons-compress-1.11.jar
swagger-client-generator_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpclient/4.2.3/httpclient-4.2.3.jar (433 kB at 843 kB/s)
swagger-client-generator_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/tukaani/xz/1.5/xz-1.5.jar
swagger-client-generator_1  | Downloaded from central: https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/1.12.1/qdox-1.12.1.jar (180 kB at 348 kB/s)
swagger-client-generator_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/3.3/plexus-archiver-3.3.jar (185 kB at 359 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.jar (86 kB at 129 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/tukaani/xz/1.5/xz-1.5.jar (100 kB at 135 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-compress/1.11/commons-compress-1.11.jar (426 kB at 422 kB/s)
swagger-client-generator_1  | [INFO]
swagger-client-generator_1  | Loading source files for package cash.super_.platform.client.parkingplus.invoker...
swagger-client-generator_1  | Loading source files for package cash.super_.platform.client.parkingplus.invoker.auth...
swagger-client-generator_1  | Loading source files for package cash.super_.platform.client.parkingplus.api...
swagger-client-generator_1  | Loading source files for package cash.super_.platform.client.parkingplus.model...
swagger-client-generator_1  | Constructing Javadoc information...
swagger-client-generator_1  | Standard Doclet version 1.8.0_272
swagger-client-generator_1  | Building tree for all the packages and classes...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/ApiClient.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/ApiClient.Api.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/EncodingUtils.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/ParamExpander.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/RFC3339DateFormat.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/StringUtil.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/ApiKeyAuth.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/HttpBasicAuth.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/OAuth.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/OAuth.AccessTokenListener.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/OAuth.OAuthFeignClient.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/OAuthFlow.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2Api.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2Api.CarregarCredenciadoUsingPOSTQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2Api.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2Api.CreditarCartaoUsingPOSTQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.GetPromocoesUsingGETQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.GetTicketUsingGETQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.GetTicketUsingPOSTQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.PagamentosEfetuadosUsingGETQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.PagarTicketAutorizadoUsingPOSTQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.PagarTicketUsingPOSTQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/AutenticacaoResponse.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/DadosCnpj.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/DadosCpf.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/DadosEndereco.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/DadosEndereco.UfEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/NotaInfo.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/PagamentoAutorizadoRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/PagamentoCartaoDebitoRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/PagamentoCredenciadoRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/PagamentoEfetuado.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/PagamentoEfetuado.TipoEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/PagamentoRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/Promocao.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/Promocao.BandeiraEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/Promocao.DiasSemanaEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/Promocao.TipoDescontoEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/Promocao.TipoPromocaoEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/RetornoConsulta.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/RetornoCreditarCartao.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/RetornoErro.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/RetornoPagamento.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/TicketRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/overview-frame.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/package-frame.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/package-summary.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/package-tree.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/package-frame.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/package-summary.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/package-tree.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/package-frame.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/package-summary.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/package-tree.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/package-frame.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/package-summary.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/package-tree.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/constant-values.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/serialized-form.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/class-use/ApiClient.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/class-use/ApiClient.Api.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/class-use/EncodingUtils.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/class-use/StringUtil.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/class-use/RFC3339DateFormat.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/class-use/ParamExpander.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/class-use/ApiKeyAuth.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/class-use/OAuth.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/class-use/OAuth.AccessTokenListener.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/class-use/OAuth.OAuthFeignClient.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/class-use/OAuthFlow.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/class-use/HttpBasicAuth.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/class-use/ServicoCargaCreditoCredenciado2Api.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/class-use/ServicoCargaCreditoCredenciado2Api.CarregarCredenciadoUsingPOSTQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/class-use/ServicoPagamentoCartaoDebito2Api.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/class-use/ServicoPagamentoCartaoDebito2Api.CreditarCartaoUsingPOSTQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/class-use/ServicoPagamentoTicket2Api.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/class-use/ServicoPagamentoTicket2Api.GetPromocoesUsingGETQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/class-use/ServicoPagamentoTicket2Api.GetTicketUsingGETQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/class-use/ServicoPagamentoTicket2Api.GetTicketUsingPOSTQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/class-use/ServicoPagamentoTicket2Api.PagamentosEfetuadosUsingGETQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/class-use/ServicoPagamentoTicket2Api.PagarTicketAutorizadoUsingPOSTQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/class-use/ServicoPagamentoTicket2Api.PagarTicketUsingPOSTQueryParams.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/DadosEndereco.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/DadosEndereco.UfEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/PagamentoEfetuado.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/PagamentoEfetuado.TipoEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/PagamentoRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/NotaInfo.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/AutenticacaoResponse.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/RetornoPagamento.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/RetornoCreditarCartao.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/CriptografarCartaoRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/DadosCpf.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/PagamentoAutorizadoRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/RetornoConsulta.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/PagamentoCartaoDebitoRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/Promocao.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/Promocao.BandeiraEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/Promocao.DiasSemanaEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/Promocao.TipoDescontoEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/Promocao.TipoPromocaoEnum.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/PagamentoCredenciadoRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/DadosCnpj.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/TicketRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/class-use/RetornoErro.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/package-use.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/package-use.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/package-use.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/package-use.html...
swagger-client-generator_1  | Building index for all the packages and classes...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/overview-tree.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/index-all.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/deprecated-list.html...
swagger-client-generator_1  | Building index for all classes...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/allclasses-frame.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/allclasses-noframe.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/index.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/overview-summary.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/help-doc.html...
swagger-client-generator_1  | 11 warnings
swagger-client-generator_1  | [WARNING] Javadoc Warnings
swagger-client-generator_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:83: warning: no description for @param
swagger-client-generator_1  | [WARNING] * @param password
swagger-client-generator_1  | [WARNING] ^
swagger-client-generator_1  | [INFO] Building jar: /generator/springboot-client-api/target/parking-plus-client-feign-1.0.0-SNAPSHOT-javadoc.jar
swagger-client-generator_1  | [INFO]
swagger-client-generator_1  | [INFO] --- maven-source-plugin:2.2.1:jar-no-fork (attach-sources) @ parking-plus-client-feign ---
swagger-client-generator_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.jar (185 kB at 511 kB/s)
swagger-client-generator_1  | [INFO] Building jar: /generator/springboot-client-api/target/parking-plus-client-feign-1.0.0-SNAPSHOT-sources.jar
swagger-client-generator_1  | [INFO] ------------------------------------------------------------------------
swagger-client-generator_1  | [INFO] BUILD SUCCESS
swagger-client-generator_1  | [INFO] ------------------------------------------------------------------------
swagger-client-generator_1  | [INFO] Total time:  01:20 min
swagger-client-generator_1  | [INFO] Finished at: 2020-11-06T03:50:05Z
swagger-client-generator_1  | [INFO] ------------------------------------------------------------------------
swagger-client-generator_1  |
swagger-client-generator_1  | 🎨 Copying originating schema '/schemas/parking-plus-schema.json'
swagger-client-generator_1  | '/schemas/parking-plus-schema.json' -> 'src/main/resources/parking-plus-schema.json'
swagger-client-generator_1  |
swagger-client-generator_1  | 🐙 Setting up initial git repo with remote 'git@gitlab.com:supercash/clients/parking-plus-client-feign.git'
swagger-client-generator_1  | - Setting user as Marcello de Sales
swagger-client-generator_1  | - Setting email as marcello.desales@gmail.com
swagger-client-generator_1  | - Adding remote as git@gitlab.com:supercash/clients/parking-plus-client-feign.git
swagger-client-generator_1  |
swagger-client-generator_1  | Initialized empty Git repository in /generator/springboot-client-api/.git/
swagger-client-generator_1  | - Initial commit...
swagger-client-generator_1  | [master (root-commit) 860bb72] :tada:  Initial commit for client API
swagger-client-generator_1  |  52 files changed, 8258 insertions(+)
swagger-client-generator_1  |  create mode 100644 .gitignore
swagger-client-generator_1  |  create mode 100644 .gitlab-ci.yml
swagger-client-generator_1  |  create mode 100644 .swagger-codegen-ignore
swagger-client-generator_1  |  create mode 100644 .swagger-codegen/VERSION
swagger-client-generator_1  |  create mode 100644 .travis.yml
swagger-client-generator_1  |  create mode 100644 README.md
swagger-client-generator_1  |  create mode 100644 build.gradle
swagger-client-generator_1  |  create mode 100644 build.sbt
swagger-client-generator_1  |  create mode 100644 ci_settings.xml
swagger-client-generator_1  |  create mode 100644 git_push.sh
swagger-client-generator_1  |  create mode 100644 gradle.properties
swagger-client-generator_1  |  create mode 100644 gradle/wrapper/gradle-wrapper.jar
swagger-client-generator_1  |  create mode 100644 gradle/wrapper/gradle-wrapper.properties
swagger-client-generator_1  |  create mode 100644 gradlew
swagger-client-generator_1  |  create mode 100644 gradlew.bat
swagger-client-generator_1  |  create mode 100644 personal_settings.xml
swagger-client-generator_1  |  create mode 100644 pom.xml
swagger-client-generator_1  |  create mode 100644 settings.gradle
swagger-client-generator_1  |  create mode 100644 src/main/AndroidManifest.xml
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2Api.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2Api.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/invoker/EncodingUtils.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/invoker/ParamExpander.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/invoker/RFC3339DateFormat.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/invoker/StringUtil.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/ApiKeyAuth.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/HttpBasicAuth.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/OAuth.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/OAuthFlow.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/AutenticacaoResponse.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/DadosCnpj.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/DadosCpf.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/DadosEndereco.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/NotaInfo.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoAutorizadoRequest.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCartaoDebitoRequest.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCredenciadoRequest.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoEfetuado.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoRequest.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/Promocao.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/RetornoConsulta.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/RetornoCreditarCartao.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/RetornoErro.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/RetornoPagamento.java
swagger-client-generator_1  |  create mode 100644 src/main/java/cash/super_/platform/client/parkingplus/model/TicketRequest.java
swagger-client-generator_1  |  create mode 100644 src/main/resources/parking-plus-schema.json
swagger-client-generator_1  |  create mode 100644 src/test/java/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2ApiTest.java
swagger-client-generator_1  |  create mode 100644 src/test/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2ApiTest.java
swagger-client-generator_1  |  create mode 100644 src/test/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2ApiTest.java
swagger-client-generator_1  | Switched to a new branch 'develop'
swagger-client-generator_1  |
swagger-client-generator_1  | 📦 Publishing stubs to Gitlab Maven Repository
swagger-client-generator_1  | [INFO] Scanning for projects...
swagger-client-generator_1  | [INFO]
swagger-client-generator_1  | [INFO] -------< cash.super_.platform.client:parking-plus-client-feign >--------
swagger-client-generator_1  | [INFO] Building parking-plus-client-feign 1.0.0-SNAPSHOT
swagger-client-generator_1  | [INFO] --------------------------------[ jar ]---------------------------------
swagger-client-generator_1  | [INFO]
swagger-client-generator_1  | [INFO] --- maven-enforcer-plugin:3.0.0-M1:enforce (enforce-maven) @ parking-plus-client-feign ---
swagger-client-generator_1  | Loading source files for package cash.super_.platform.client.parkingplus.invoker.auth...
swagger-client-generator_1  | Loading source files for package cash.super_.platform.client.parkingplus.api...
swagger-client-generator_1  | Loading source files for package cash.super_.platform.client.parkingplus.model...
swagger-client-generator_1  | Constructing Javadoc information...
swagger-client-generator_1  | Standard Doclet version 1.8.0_272
swagger-client-generator_1  | Building tree for all the packages and classes...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/ApiClient.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/ApiClient.Api.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/TicketRequest.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/overview-frame.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/package-frame.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/package-summary.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/package-use.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/package-use.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/package-use.html...
swagger-client-generator_1  | Building index for all the packages and classes...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/overview-tree.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/index-all.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/deprecated-list.html...
swagger-client-generator_1  | Building index for all classes...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/allclasses-frame.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/allclasses-noframe.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/index.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/overview-summary.html...
swagger-client-generator_1  | Generating /generator/springboot-client-api/target/apidocs/help-doc.html...
swagger-client-generator_1  | [WARNING] * @param username
swagger-client-generator_1  | [WARNING] ^
swagger-client-generator_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:83: warning: no description for @param
swagger-client-generator_1  | [WARNING] * @param password
swagger-client-generator_1  | [WARNING] ^
swagger-client-generator_1  | [INFO] Building jar: /generator/springboot-client-api/target/parking-plus-client-feign-1.0.0-SNAPSHOT-javadoc.jar
swagger-client-generator_1  | [INFO]
swagger-client-generator_1  | [INFO] --- maven-source-plugin:2.2.1:jar-no-fork (attach-sources) @ parking-plus-client-feign ---
swagger-client-generator_1  | [INFO]
swagger-client-generator_1  | [INFO] --- maven-install-plugin:2.4:install (default-install) @ parking-plus-client-feign ---
swagger-client-generator_1  | [INFO] Installing /generator/springboot-client-api/target/parking-plus-client-feign-1.0.0-SNAPSHOT.jar to /root/.m2/repository/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/parking-plus-client-feign-1.0.0-SNAPSHOT.jar
swagger-client-generator_1  | [INFO] Installing /generator/springboot-client-api/pom.xml to /root/.m2/repository/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/parking-plus-client-feign-1.0.0-SNAPSHOT.pom
swagger-client-generator_1  | [INFO] Installing /generator/springboot-client-api/target/parking-plus-client-feign-1.0.0-SNAPSHOT-javadoc.jar to /root/.m2/repository/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/parking-plus-client-feign-1.0.0-SNAPSHOT-javadoc.jar
swagger-client-generator_1  | [INFO] Installing /generator/springboot-client-api/target/parking-plus-client-feign-1.0.0-SNAPSHOT-sources.jar to /root/.m2/repository/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/parking-plus-client-feign-1.0.0-SNAPSHOT-sources.jar
swagger-client-generator_1  | [INFO]
swagger-client-generator_1  | [INFO] --- maven-deploy-plugin:2.7:deploy (default-deploy) @ parking-plus-client-feign ---
swagger-client-generator_1  | Downloading from gitlab-maven: https://gitlab.com/api/v4/projects/22268428/packages/maven/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/maven-metadata.xml
swagger-client-generator_1  | Uploading to gitlab-maven: https://gitlab.com/api/v4/projects/22268428/packages/maven/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/parking-plus-client-feign-1.0.0-20201106.035016-1.jar
Uploaded to gitlab-maven: https://gitlab.com/api/v4/projects/22268428/packages/maven/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/parking-plus-client-feign-1.0.0-20201106.035016-1.jar (94 kB at 26 kB/s)
swagger-client-generator_1  | Uploading to gitlab-maven: https://gitlab.com/api/v4/projects/22268428/packages/maven/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/parking-plus-client-feign-1.0.0-20201106.035016-1.pom
Uploaded to gitlab-maven: https://gitlab.com/api/v4/projects/22268428/packages/maven/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/parking-plus-client-feign-1.0.0-20201106.035016-1.pom (11 kB at 4.6 kB/s)
swagger-client-generator_1  | Downloading from gitlab-maven: https://gitlab.com/api/v4/projects/22268428/packages/maven/cash/super_/platform/client/parking-plus-client-feign/maven-metadata.xml
swagger-client-generator_1  | Uploading to gitlab-maven: https://gitlab.com/api/v4/projects/22268428/packages/maven/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/maven-metadata.xml
Uploaded to gitlab-maven: https://gitlab.com/api/v4/projects/22268428/packages/maven/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/maven-metadata.xml (802 B at 354 B/s)
swagger-client-generator_1  | Uploading to gitlab-maven: https://gitlab.com/api/v4/projects/22268428/packages/maven/cash/super_/platform/client/parking-plus-client-feign/maven-metadata.xml
Uploaded to gitlab-maven: https://gitlab.com/api/v4/projects/22268428/packages/maven/cash/super_/platform/client/parking-plus-client-feign/maven-metadata.xml (312 B at 127 B/s)
Uploaded to gitlab-maven: https://gitlab.com/api/v4/projects/22268428/packages/maven/cash/super_/platform/client/parking-plus-client-feign/1.0.0-SNAPSHOT/maven-metadata.xml (1.2 kB at 499 B/s)
swagger-client-generator_1  | [INFO] ------------------------------------------------------------------------
swagger-client-generator_1  | [INFO] BUILD SUCCESS
swagger-client-generator_1  | [INFO] ------------------------------------------------------------------------
swagger-client-generator_1  | [INFO] Total time:  31.906 s
swagger-client-generator_1  | [INFO] Finished at: 2020-11-06T03:50:39Z
swagger-client-generator_1  | [INFO] ------------------------------------------------------------------------
swagger-client-generator_1  |
swagger-client-generator_1  | 🚚 Pushing the code to the git host. Make sure to have the ssh keys mounted!
swagger-client-generator_1  | remote:
swagger-client-generator_1  | remote: To create a merge request for develop, visit:
swagger-client-generator_1  | remote:   https://gitlab.com/supercash/clients/parking-plus-client-feign/-/merge_requests/new?merge_request%5Bsource_branch%5D=develop
swagger-client-generator_1  | remote:
swagger-client-generator_1  | To gitlab.com:supercash/clients/parking-plus-client-feign.git
swagger-client-generator_1  |  * [new branch]      master -> master
swagger-client-generator_1  |  * [new branch]      develop -> develop
swagger-client-generator_1  |
swagger-client-generator_1  | 🍻 Local deploy to /client-api/parking-plus-client-feign
swagger-client-generator_1  |
swagger-client-generator_1  | 💥 Deleting previous build from directory '/client-api/parking-plus-client-feign'
swagger-client-generator_1  |
swagger-client-generator_1  | 'parking-plus-client-feign/' -> '/client-api/parking-plus-client-feign'
swagger-client-generator_1  | 'parking-plus-client-feign/src' -> '/client-api/parking-plus-client-feign/src'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main' -> '/client-api/parking-plus-client-feign/src/main'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java' -> '/client-api/parking-plus-client-feign/src/main/java'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash' -> '/client-api/parking-plus-client-feign/src/main/java/cash'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash/super_' -> '/client-api/parking-plus-client-feign/src/main/java/cash/super_'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash/super_/platform' -> '/client-api/parking-plus-client-feign/src/main/java/cash/super_/platform'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash/super_/platform/client' -> '/client-api/parking-plus-client-feign/src/main/java/cash/super_/platform/client'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus' -> '/client-api/parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model' -> '/client-api/parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/AutenticacaoResponse.java' -> '/client-api/parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/AutenticacaoResponse.java'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.java' -> '/client-api/parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.java'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCnpj.java' -> '/client-api/parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCnpj.java'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCpf.java' -> '/client-api/parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCpf.java'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/DadosEndereco.java' -> '/client-api/parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/DadosEndereco.java'
swagger-client-generator_1  | 'parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/NotaInfo.java' -> '/client-api/parking-plus-client-feign/src/main/java/cash/super_/platform/client/parkingplus/model/NotaInfo.java'
swagger-client-generator_1  | 'parking-plus-client-feign/pom.xml' -> '/client-api/parking-plus-client-feign/pom.xml'
swagger-client-generator_1  | 'parking-plus-client-feign/README.md' -> '/client-api/parking-plus-client-feign/README.md'
swagger-client-generator_1  | 'parking-plus-client-feign/build.gradle' -> '/client-api/parking-plus-client-feign/build.gradle'
swagger-client-generator_1  | 'parking-plus-client-feign/build.sbt' -> '/client-api/parking-plus-client-feign/build.sbt'
swagger-client-generator_1  | 'parking-plus-client-feign/settings.gradle' -> '/client-api/parking-plus-client-feign/settings.gradle'
swagger-client-generator_1  | 'parking-plus-client-feign/gradle.properties' -> '/client-api/parking-plus-client-feign/gradle.properties'
swagger-client-generator_1  | 'parking-plus-client-feign/.travis.yml' -> '/client-api/parking-plus-client-feign/.travis.yml'
swagger-client-generator_1  | 'parking-plus-client-feign/gradlew' -> '/client-api/parking-plus-client-feign/gradlew'
swagger-client-generator_1  | 'parking-plus-client-feign/gradlew.bat' -> '/client-api/parking-plus-client-feign/gradlew.bat'
swagger-client-generator_1  | 'parking-plus-client-feign/gradle' -> '/client-api/parking-plus-client-feign/gradle'
swagger-client-generator_1  | 'parking-plus-client-feign/gradle/wrapper' -> '/client-api/parking-plus-client-feign/gradle/wrapper'
swagger-client-generator_1  | 'parking-plus-client-feign/gradle/wrapper/gradle-wrapper.properties' -> '/client-api/parking-plus-client-feign/gradle/wrapper/gradle-wrapper.properties'
swagger-client-generator_1  | 'parking-plus-client-feign/gradle/wrapper/gradle-wrapper.jar' -> '/client-api/parking-plus-client-feign/gradle/wrapper/gradle-wrapper.jar'
swagger-client-generator_1  | 'parking-plus-client-feign/git_push.sh' -> '/client-api/parking-plus-client-feign/git_push.sh'
swagger-client-generator_1  | 'parking-plus-client-feign/.git/HEAD' -> '/client-api/parking-plus-client-feign/.git/HEAD'
swagger-code-and-repo-gen_swagger-client-generator_1 exited with code 0
```

## Existing Client API Repo

* When the API already exists
* API is updated and a new commit is done with the update
* The API Schema is copied to the resources.

```console
$ docker-compose --env-file parking-plus.env up --build
WARNING: The GENERATE_CLIENT_PUBLISH_TOKEN variable is not set. Defaulting to a blank string.
Building swagger-client-repo-gen
Step 1/11 : FROM maven:3.6.3-jdk-8-slim
 ---> ebf1fc5205e8
Step 2/11 : RUN apt-get update && apt-get install -y python git
 ---> Using cache
 ---> a22bc0819db3
Step 3/11 : WORKDIR /generator
 ---> Using cache
 ---> 17dda3f580b6
Step 4/11 : COPY pom.xml .
 ---> Using cache
 ---> f0b8afdb0468
Step 5/11 : RUN mvn dependency:resolve-plugins dependency:go-offline
 ---> Using cache
 ---> 0d10c51bc4a9
Step 6/11 : COPY entrypoint.sh .
 ---> Using cache
 ---> af784081af8b
Step 7/11 : COPY update-generated-project.py .
 ---> Using cache
 ---> 1b51f9d2b2ae
Step 8/11 : COPY cicd/ cicd/
 ---> Using cache
 ---> 2a43f20cbc04
Step 9/11 : VOLUME /schemas
 ---> Using cache
 ---> c87015e58bfd
Step 10/11 : VOLUME /client-api
 ---> Using cache
 ---> c2e60e6e31e9
Step 11/11 : CMD ["/generator/entrypoint.sh"]
 ---> Using cache
 ---> 7c95f38dba14

Successfully built 7c95f38dba14
Successfully tagged marcellodesales/swagger-client-package-repo-gen:latest
Creating swagger-client-pacakge-repo-gen_swagger-client-repo-gen_1 ... done
Attaching to swagger-client-pacakge-repo-gen_swagger-client-repo-gen_1
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | 🐙 Setting up initial git repo at 'git@gitlab.com:supercash/clients/parking-plus-client-feign.git'
swagger-client-repo-gen_1  | - Setting user as Marcello de Sales
swagger-client-repo-gen_1  | - Setting email as marcello.desales@gmail.com
swagger-client-repo-gen_1  | - Pulling existing Git Repo origin git@gitlab.com:supercash/clients/parking-plus-client-feign.git...
swagger-client-repo-gen_1  | Cloning into 'springboot-client-api'...
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | 👽 Generate the sources from parking-plus-update.json in java using library feign
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | [INFO] Scanning for projects...
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] ---------------------< io.swagger:sample-project >----------------------
swagger-client-repo-gen_1  | [INFO] Building sample-project 1.0-SNAPSHOT
swagger-client-repo-gen_1  | [INFO] --------------------------------[ jar ]---------------------------------
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- swagger-codegen-maven-plugin:2.4.17:generate (default) @ sample-project ---
swagger-client-repo-gen_1  | [INFO] reading from /schemas/parking-plus-update.json
swagger-client-repo-gen_1  | [INFO] Skipped overwriting pom.xml as the file already exists in /generator/springboot-client-api//pom.xml
swagger-client-repo-gen_1  | [INFO] Skipped overwriting README.md as the file already exists in /generator/springboot-client-api//README.md
swagger-client-repo-gen_1  | [INFO] Skipped overwriting build.gradle as the file already exists in /generator/springboot-client-api//build.gradle
swagger-client-repo-gen_1  | [INFO] Skipped overwriting build.sbt as the file already exists in /generator/springboot-client-api//build.sbt
swagger-client-repo-gen_1  | [INFO] Skipped overwriting settings.gradle as the file already exists in /generator/springboot-client-api//settings.gradle
swagger-client-repo-gen_1  | [INFO] Skipped overwriting gradle.properties as the file already exists in /generator/springboot-client-api//gradle.properties
swagger-client-repo-gen_1  | [INFO] Skipped overwriting AndroidManifest.xml as the file already exists in /generator/springboot-client-api/src/main/AndroidManifest.xml
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/AutenticacaoResponse.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCnpj.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCpf.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/DadosEndereco.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/NotaInfo.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoAutorizadoRequest.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCartaoDebitoRequest.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCredenciadoRequest.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoEfetuado.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoRequest.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/Promocao.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoConsulta.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoCreditarCartao.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoErro.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoPagamento.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/model/TicketRequest.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2Api.java
swagger-client-repo-gen_1  | [INFO] File exists. Skipped overwriting /generator/springboot-client-api/src/test/java/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2ApiTest.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2Api.java
swagger-client-repo-gen_1  | [INFO] File exists. Skipped overwriting /generator/springboot-client-api/src/test/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2ApiTest.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.java
swagger-client-repo-gen_1  | [INFO] File exists. Skipped overwriting /generator/springboot-client-api/src/test/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2ApiTest.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/.travis.yml
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/StringUtil.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/HttpBasicAuth.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/ApiKeyAuth.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/OAuth.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/auth/OAuthFlow.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/gradlew
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/gradlew.bat
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/gradle/wrapper/gradle-wrapper.properties
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/gradle/wrapper/gradle-wrapper.jar
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/git_push.sh
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/.gitignore
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ParamExpander.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/EncodingUtils.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/RFC3339DateFormat.java
swagger-client-repo-gen_1  | [INFO] writing file /generator/springboot-client-api/.swagger-codegen/VERSION
swagger-client-repo-gen_1  | [INFO] ------------------------------------------------------------------------
swagger-client-repo-gen_1  | [INFO] BUILD SUCCESS
swagger-client-repo-gen_1  | [INFO] ------------------------------------------------------------------------
swagger-client-repo-gen_1  | [INFO] Total time:  1.275 s
swagger-client-repo-gen_1  | [INFO] Finished at: 2020-11-10T17:02:09Z
swagger-client-repo-gen_1  | [INFO] ------------------------------------------------------------------------
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | 🏗  Updating client metadata already setup and in the repo!
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | 🏺 Generating client jars from stubs
swagger-client-repo-gen_1  | [INFO] Scanning for projects...
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] -------< cash.super_.platform.client:parking-plus-client-feign >--------
swagger-client-repo-gen_1  | [INFO] Building parking-plus-client-feign 1.0.0-SNAPSHOT
swagger-client-repo-gen_1  | [INFO] --------------------------------[ jar ]---------------------------------
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-enforcer-plugin/3.0.0-M1/maven-enforcer-plugin-3.0.0-M1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-enforcer-plugin/3.0.0-M1/maven-enforcer-plugin-3.0.0-M1.pom (7.2 kB at 5.4 kB/s)
...
...
...
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-monitor/2.2.1/maven-monitor-2.2.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/2.2.1/maven-repository-metadata-2.2.1.jar (26 kB at 22 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-api/2.2.1/maven-plugin-api-2.2.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-logging-api/1.1/doxia-logging-api-1.1.jar (11 kB at 9.5 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-descriptor/2.2.1/maven-plugin-descriptor-2.2.1.jar (39 kB at 30 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.0.22/plexus-utils-3.0.22.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-monitor/2.2.1/maven-monitor-2.2.1.jar (10 kB at 7.6 kB/s)
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-api/2.2.1/maven-plugin-api-2.2.1.jar (12 kB at 8.8 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.jar (80 kB at 54 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-error-diagnostics/2.2.1/maven-error-diagnostics-2.2.1.jar (13 kB at 8.7 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.0.22/plexus-utils-3.0.22.jar (245 kB at 148 kB/s)
swagger-client-repo-gen_1  | [INFO] Source directory: /generator/springboot-client-api/src/main/java added.
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- maven-resources-plugin:2.6:resources (default-resources) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | [INFO] Using 'UTF-8' encoding to copy filtered resources.
swagger-client-repo-gen_1  | [INFO] Copying 1 resource
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- maven-compiler-plugin:3.1:compile (default-compile) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | [INFO] Changes detected - recompiling the module!
swagger-client-repo-gen_1  | [INFO] Compiling 29 source files to /generator/springboot-client-api/target/classes
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/RFC3339DateFormat.java: /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/RFC3339DateFormat.java uses or overrides a deprecated API.
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/RFC3339DateFormat.java: Recompile with -Xlint:deprecation for details.
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- build-helper-maven-plugin:1.10:add-test-source (add_test_sources) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | [INFO] Test Source directory: /generator/springboot-client-api/src/test/java added.
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- maven-resources-plugin:2.6:testResources (default-testResources) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | [INFO] Not copying test resources
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- maven-compiler-plugin:3.1:testCompile (default-testCompile) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | [INFO] Not compiling test sources
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- maven-surefire-plugin:2.12:test (default-test) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/2.12/surefire-booter-2.12.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/2.12/surefire-booter-2.12.pom (3.0 kB at 11 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/2.12/surefire-api-2.12.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/2.12/surefire-api-2.12.pom (2.5 kB at 8.9 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/2.12/maven-surefire-common-2.12.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/2.12/maven-surefire-common-2.12.pom (5.1 kB at 18 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/2.12/surefire-api-2.12.jar
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/2.12/maven-surefire-common-2.12.jar
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/2.12/surefire-booter-2.12.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/2.12/surefire-booter-2.12.jar (33 kB at 119 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/2.12/surefire-api-2.12.jar (124 kB at 410 kB/s)
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/2.12/maven-surefire-common-2.12.jar (224 kB at 536 kB/s)
swagger-client-repo-gen_1  | [INFO] Tests are skipped.
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- maven-jar-plugin:2.2:jar (default-jar) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-project/2.0.7/maven-project-2.0.7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-project/2.0.7/maven-project-2.0.7.pom (2.6 kB at 9.6 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/2.0.7/maven-2.0.7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/2.0.7/maven-2.0.7.pom (11 kB at 38 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings/2.0.7/maven-settings-2.0.7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings/2.0.7/maven-settings-2.0.7.pom (2.0 kB at 7.1 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-model/2.0.7/maven-model-2.0.7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-model/2.0.7/maven-model-2.0.7.pom (3.0 kB at 11 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-profile/2.0.7/maven-profile-2.0.7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-profile/2.0.7/maven-profile-2.0.7.pom (2.0 kB at 7.2 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact-manager/2.0.7/maven-artifact-manager-2.0.7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact-manager/2.0.7/maven-artifact-manager-2.0.7.pom (2.6 kB at 9.4 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/2.0.7/maven-repository-metadata-2.0.7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/2.0.7/maven-repository-metadata-2.0.7.pom (1.9 kB at 6.5 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.0.7/maven-artifact-2.0.7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.0.7/maven-artifact-2.0.7.pom (1.6 kB at 6.4 kB/s)
...
...
...
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-registry/2.0.7/maven-plugin-registry-2.0.7.jar (29 kB at 48 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/1.0-alpha-1/plexus-io-1.0-alpha-1.jar
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/1.0-alpha-9/plexus-archiver-1.0-alpha-9.jar (157 kB at 238 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/1.0-alpha-1/plexus-io-1.0-alpha-1.jar (12 kB at 14 kB/s)
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/1.4.9/plexus-utils-1.4.9.jar (204 kB at 221 kB/s)
swagger-client-repo-gen_1  | [INFO] Building jar: /generator/springboot-client-api/target/parking-plus-client-feign-1.0.0-SNAPSHOT.jar
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- maven-dependency-plugin:2.8:copy-dependencies (default) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/1.0-alpha-10/doxia-sink-api-1.0-alpha-10.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/1.0-alpha-10/doxia-sink-api-1.0-alpha-10.pom (1.3 kB at 4.6 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia/1.0-alpha-10/doxia-1.0-alpha-10.pom
...
...
...
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-invoker/2.0.11/maven-invoker-2.0.11.jar
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/asm/asm/3.3.1/asm-3.3.1.jar (44 kB at 38 kB/s)
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-tree/2.1/maven-dependency-tree-2.1.jar (60 kB at 52 kB/s)
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.4/maven-dependency-analyzer-1.4.jar (27 kB at 24 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4.jar (32 kB at 23 kB/s)
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-invoker/2.0.11/maven-invoker-2.0.11.jar (29 kB at 20 kB/s)
swagger-client-repo-gen_1  | [INFO] Copying animal-sniffer-annotation-1.0.jar to /generator/springboot-client-api/target/lib/animal-sniffer-annotation-1.0.jar
swagger-client-repo-gen_1  | [INFO] Copying bcprov-jdk15on-1.50.jar to /generator/springboot-client-api/target/lib/bcprov-jdk15on-1.50.jar
swagger-client-repo-gen_1  | [INFO] Copying feign-jackson-9.4.0.jar to /generator/springboot-client-api/target/lib/feign-jackson-9.4.0.jar
swagger-client-repo-gen_1  | [INFO] Copying swagger-annotations-1.5.18.jar to /generator/springboot-client-api/target/lib/swagger-annotations-1.5.18.jar
swagger-client-repo-gen_1  | [INFO] Copying joda-time-2.9.9.jar to /generator/springboot-client-api/target/lib/joda-time-2.9.9.jar
swagger-client-repo-gen_1  | [INFO] Copying org.apache.oltu.oauth2.common-1.0.1.jar to /generator/springboot-client-api/target/lib/org.apache.oltu.oauth2.common-1.0.1.jar
swagger-client-repo-gen_1  | [INFO] Copying okio-1.11.0.jar to /generator/springboot-client-api/target/lib/okio-1.11.0.jar
swagger-client-repo-gen_1  | [INFO] Copying hamcrest-core-1.3.jar to /generator/springboot-client-api/target/lib/hamcrest-core-1.3.jar
swagger-client-repo-gen_1  | [INFO] Copying jackson-databind-2.10.1.jar to /generator/springboot-client-api/target/lib/jackson-databind-2.10.1.jar
swagger-client-repo-gen_1  | [INFO] Copying json-20140107.jar to /generator/springboot-client-api/target/lib/json-20140107.jar
swagger-client-repo-gen_1  | [INFO] Copying commons-codec-1.9.jar to /generator/springboot-client-api/target/lib/commons-codec-1.9.jar
swagger-client-repo-gen_1  | [INFO] Copying slf4j-api-1.7.13.jar to /generator/springboot-client-api/target/lib/slf4j-api-1.7.13.jar
swagger-client-repo-gen_1  | [INFO] Copying feign-slf4j-9.4.0.jar to /generator/springboot-client-api/target/lib/feign-slf4j-9.4.0.jar
swagger-client-repo-gen_1  | [INFO] Copying junit-4.13.1.jar to /generator/springboot-client-api/target/lib/junit-4.13.1.jar
swagger-client-repo-gen_1  | [INFO] Copying mockwebserver-3.6.0.jar to /generator/springboot-client-api/target/lib/mockwebserver-3.6.0.jar
swagger-client-repo-gen_1  | [INFO] Copying feign-core-9.4.0.jar to /generator/springboot-client-api/target/lib/feign-core-9.4.0.jar
swagger-client-repo-gen_1  | [INFO] Copying jackson-core-2.10.1.jar to /generator/springboot-client-api/target/lib/jackson-core-2.10.1.jar
swagger-client-repo-gen_1  | [INFO] Copying jackson-annotations-2.10.1.jar to /generator/springboot-client-api/target/lib/jackson-annotations-2.10.1.jar
swagger-client-repo-gen_1  | [INFO] Copying okhttp-3.6.0.jar to /generator/springboot-client-api/target/lib/okhttp-3.6.0.jar
swagger-client-repo-gen_1  | [INFO] Copying jackson-datatype-joda-2.10.1.jar to /generator/springboot-client-api/target/lib/jackson-datatype-joda-2.10.1.jar
swagger-client-repo-gen_1  | [INFO] Copying org.apache.oltu.oauth2.client-1.0.1.jar to /generator/springboot-client-api/target/lib/org.apache.oltu.oauth2.client-1.0.1.jar
swagger-client-repo-gen_1  | [INFO] Copying feign-form-2.1.0.jar to /generator/springboot-client-api/target/lib/feign-form-2.1.0.jar
swagger-client-repo-gen_1  | [INFO] Copying lombok-1.16.12.jar to /generator/springboot-client-api/target/lib/lombok-1.16.12.jar
swagger-client-repo-gen_1  | [INFO] Copying assertj-core-1.7.1.jar to /generator/springboot-client-api/target/lib/assertj-core-1.7.1.jar
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- maven-jar-plugin:2.2:jar (default) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- maven-jar-plugin:2.2:test-jar (default) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | [INFO] Skipping packaging of the test-jar
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- maven-javadoc-plugin:2.10.4:jar (attach-javadocs) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-toolchain/2.2.1/maven-toolchain-2.2.1.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-toolchain/2.2.1/maven-toolchain-2.2.1.pom (3.3 kB at 12 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-invoker/2.2/maven-invoker-2.2.pom
...
...
...
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/3.3/plexus-archiver-3.3.jar (185 kB at 267 kB/s)
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/2.7.1/plexus-io-2.7.1.jar (86 kB at 113 kB/s)
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/log4j/log4j/1.2.14/log4j-1.2.14.jar (367 kB at 483 kB/s)
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-compress/1.11/commons-compress-1.11.jar (426 kB at 559 kB/s)
Downloaded from central: https://repo.maven.apache.org/maven2/org/tukaani/xz/1.5/xz-1.5.jar (100 kB at 106 kB/s)
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | Loading source files for package cash.super_.platform.client.parkingplus.invoker...
swagger-client-repo-gen_1  | Loading source files for package cash.super_.platform.client.parkingplus.invoker.auth...
swagger-client-repo-gen_1  | Loading source files for package cash.super_.platform.client.parkingplus.api...
swagger-client-repo-gen_1  | Loading source files for package cash.super_.platform.client.parkingplus.model...
swagger-client-repo-gen_1  | Constructing Javadoc information...
swagger-client-repo-gen_1  | Standard Doclet version 1.8.0_272
swagger-client-repo-gen_1  | Building tree for all the packages and classes...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/ApiClient.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/ApiClient.Api.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/EncodingUtils.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/ParamExpander.html...
...
...
...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/api/package-use.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/package-use.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/invoker/auth/package-use.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/cash/super_/platform/client/parkingplus/model/package-use.html...
swagger-client-repo-gen_1  | Building index for all the packages and classes...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/overview-tree.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/index-all.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/deprecated-list.html...
swagger-client-repo-gen_1  | Building index for all classes...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/allclasses-frame.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/allclasses-noframe.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/index.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/overview-summary.html...
swagger-client-repo-gen_1  | Generating /generator/springboot-client-api/target/apidocs/help-doc.html...
swagger-client-repo-gen_1  | 11 warnings
swagger-client-repo-gen_1  | [WARNING] Javadoc Warnings
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:50: warning: no description for @param
swagger-client-repo-gen_1  | [WARNING] * @param authName
swagger-client-repo-gen_1  | [WARNING] ^
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:58: warning: no description for @param
swagger-client-repo-gen_1  | [WARNING] * @param authName
swagger-client-repo-gen_1  | [WARNING] ^
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:59: warning: no description for @param
swagger-client-repo-gen_1  | [WARNING] * @param apiKey
swagger-client-repo-gen_1  | [WARNING] ^
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:68: warning: no description for @param
swagger-client-repo-gen_1  | [WARNING] * @param authName
swagger-client-repo-gen_1  | [WARNING] ^
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:69: warning: no description for @param
swagger-client-repo-gen_1  | [WARNING] * @param username
swagger-client-repo-gen_1  | [WARNING] ^
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:70: warning: no description for @param
swagger-client-repo-gen_1  | [WARNING] * @param password
swagger-client-repo-gen_1  | [WARNING] ^
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:79: warning: no description for @param
swagger-client-repo-gen_1  | [WARNING] * @param authName
swagger-client-repo-gen_1  | [WARNING] ^
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:80: warning: no description for @param
swagger-client-repo-gen_1  | [WARNING] * @param clientId
swagger-client-repo-gen_1  | [WARNING] ^
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:81: warning: no description for @param
swagger-client-repo-gen_1  | [WARNING] * @param secret
swagger-client-repo-gen_1  | [WARNING] ^
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:82: warning: no description for @param
swagger-client-repo-gen_1  | [WARNING] * @param username
swagger-client-repo-gen_1  | [WARNING] ^
swagger-client-repo-gen_1  | [WARNING] /generator/springboot-client-api/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java:83: warning: no description for @param
swagger-client-repo-gen_1  | [WARNING] * @param password
swagger-client-repo-gen_1  | [WARNING] ^
swagger-client-repo-gen_1  | [INFO] Building jar: /generator/springboot-client-api/target/parking-plus-client-feign-1.0.0-SNAPSHOT-javadoc.jar
swagger-client-repo-gen_1  | [INFO]
swagger-client-repo-gen_1  | [INFO] --- maven-source-plugin:2.2.1:jar-no-fork (attach-sources) @ parking-plus-client-feign ---
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.pom (3.2 kB at 12 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/1.1.20/plexus-components-1.1.20.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/1.1.20/plexus-components-1.1.20.pom (3.0 kB at 11 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.0.7/plexus-utils-3.0.7.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.0.7/plexus-utils-3.0.7.pom (2.5 kB at 9.1 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.pom (1.7 kB at 6.7 kB/s)
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.jar
swagger-client-repo-gen_1  | Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/2.0.4/plexus-io-2.0.4.jar (58 kB at 218 kB/s)
swagger-client-repo-gen_1  | Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.jar (185 kB at 627 kB/s)
swagger-client-repo-gen_1  | [INFO] Building jar: /generator/springboot-client-api/target/parking-plus-client-feign-1.0.0-SNAPSHOT-sources.jar
swagger-client-repo-gen_1  | [INFO] ------------------------------------------------------------------------
swagger-client-repo-gen_1  | [INFO] BUILD SUCCESS
swagger-client-repo-gen_1  | [INFO] ------------------------------------------------------------------------
swagger-client-repo-gen_1  | [INFO] Total time:  01:36 min
swagger-client-repo-gen_1  | [INFO] Finished at: 2020-11-10T17:03:47Z
swagger-client-repo-gen_1  | [INFO] ------------------------------------------------------------------------
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | 🎨 Copying originating schema '/schemas/parking-plus-update.json'
swagger-client-repo-gen_1  | '/schemas/parking-plus-update.json' -> 'src/main/resources/parking-plus-update.json'
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | - Seeing the differences
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2Api.java b/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2Api.java
swagger-client-repo-gen_1  | index e40467a..6fc74e6 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2Api.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoCargaCreditoCredenciado2Api.java
swagger-client-repo-gen_1  | @@ -12,7 +12,7 @@ import java.util.List;
swagger-client-repo-gen_1  |  import java.util.Map;
swagger-client-repo-gen_1  |  import feign.*;
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |  public interface ServicoCargaCreditoCredenciado2Api extends ApiClient.Api {
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2Api.java b/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2Api.java
swagger-client-repo-gen_1  | index 22f6581..fb9c584 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2Api.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoCartaoDebito2Api.java
swagger-client-repo-gen_1  | @@ -13,7 +13,7 @@ import java.util.List;
swagger-client-repo-gen_1  |  import java.util.Map;
swagger-client-repo-gen_1  |  import feign.*;
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |  public interface ServicoPagamentoCartaoDebito2Api extends ApiClient.Api {
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.java b/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.java
swagger-client-repo-gen_1  | index a3cc1cf..136be87 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/api/ServicoPagamentoTicket2Api.java
swagger-client-repo-gen_1  | @@ -18,7 +18,7 @@ import java.util.List;
swagger-client-repo-gen_1  |  import java.util.Map;
swagger-client-repo-gen_1  |  import feign.*;
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |  public interface ServicoPagamentoTicket2Api extends ApiClient.Api {
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java b/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java
swagger-client-repo-gen_1  | index 8fd7680..0d2f6f0 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/invoker/ApiClient.java
swagger-client-repo-gen_1  | @@ -20,7 +20,7 @@ import feign.slf4j.Slf4jLogger;
swagger-client-repo-gen_1  |  import cash.super_.platform.client.parkingplus.invoker.auth.*;
swagger-client-repo-gen_1  |  import cash.super_.platform.client.parkingplus.invoker.auth.OAuth.AccessTokenListener;
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |  public class ApiClient {
swagger-client-repo-gen_1  |    public interface Api {}
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/invoker/StringUtil.java b/src/main/java/cash/super_/platform/client/parkingplus/invoker/StringUtil.java
swagger-client-repo-gen_1  | index e140852..5fa8e52 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/invoker/StringUtil.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/invoker/StringUtil.java
swagger-client-repo-gen_1  | @@ -13,7 +13,7 @@
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |  package cash.super_.platform.client.parkingplus.invoker;
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |  public class StringUtil {
swagger-client-repo-gen_1  |    /**
swagger-client-repo-gen_1  |     * Check if the given array contains the given value (with case-insensitive comparison).
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/AutenticacaoResponse.java b/src/main/java/cash/super_/platform/client/parkingplus/model/AutenticacaoResponse.java
swagger-client-repo-gen_1  | index 3d5f681..91a151b 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/AutenticacaoResponse.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/AutenticacaoResponse.java
swagger-client-repo-gen_1  | @@ -24,7 +24,7 @@ import io.swagger.annotations.ApiModelProperty;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * AutenticacaoResponse
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.java b/src/main/java/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.java
swagger-client-repo-gen_1  | index ebfbe97..e9fc7a1 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.java
swagger-client-repo-gen_1  | @@ -24,7 +24,7 @@ import io.swagger.annotations.ApiModelProperty;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * CriptografarCartaoRequest
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCnpj.java b/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCnpj.java
swagger-client-repo-gen_1  | index c555ca7..14affe2 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCnpj.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCnpj.java
swagger-client-repo-gen_1  | @@ -25,7 +25,7 @@ import io.swagger.annotations.ApiModelProperty;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * DadosCnpj
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCpf.java b/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCpf.java
swagger-client-repo-gen_1  | index abf97da..6d6965c 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCpf.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/DadosCpf.java
swagger-client-repo-gen_1  | @@ -24,7 +24,7 @@ import io.swagger.annotations.ApiModelProperty;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * DadosCpf
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/DadosEndereco.java b/src/main/java/cash/super_/platform/client/parkingplus/model/DadosEndereco.java
swagger-client-repo-gen_1  | index dca541d..326bac6 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/DadosEndereco.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/DadosEndereco.java
swagger-client-repo-gen_1  | @@ -24,7 +24,7 @@ import io.swagger.annotations.ApiModelProperty;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * DadosEndereco
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/NotaInfo.java b/src/main/java/cash/super_/platform/client/parkingplus/model/NotaInfo.java
swagger-client-repo-gen_1  | index d1756d9..407668c 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/NotaInfo.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/NotaInfo.java
swagger-client-repo-gen_1  | @@ -25,7 +25,7 @@ import org.joda.time.DateTime;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * NotaInfo
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoAutorizadoRequest.java b/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoAutorizadoRequest.java
swagger-client-repo-gen_1  | index 2a4d62e..3eda806 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoAutorizadoRequest.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoAutorizadoRequest.java
swagger-client-repo-gen_1  | @@ -28,7 +28,7 @@ import java.util.List;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * PagamentoAutorizadoRequest
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCartaoDebitoRequest.java b/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCartaoDebitoRequest.java
swagger-client-repo-gen_1  | index 48afc10..b6071b5 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCartaoDebitoRequest.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCartaoDebitoRequest.java
swagger-client-repo-gen_1  | @@ -26,7 +26,7 @@ import io.swagger.annotations.ApiModelProperty;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * PagamentoCartaoDebitoRequest
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCredenciadoRequest.java b/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCredenciadoRequest.java
swagger-client-repo-gen_1  | index b6bc2fd..8470c3f 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCredenciadoRequest.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoCredenciadoRequest.java
swagger-client-repo-gen_1  | @@ -26,7 +26,7 @@ import io.swagger.annotations.ApiModelProperty;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * PagamentoCredenciadoRequest
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoEfetuado.java b/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoEfetuado.java
swagger-client-repo-gen_1  | index 28ef56b..523a94a 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoEfetuado.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoEfetuado.java
swagger-client-repo-gen_1  | @@ -24,7 +24,7 @@ import io.swagger.annotations.ApiModelProperty;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * PagamentoEfetuado
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | @@ -59,12 +59,24 @@ public class PagamentoEfetuado {
swagger-client-repo-gen_1  |    @JsonProperty("nsu")
swagger-client-repo-gen_1  |    private String nsu = null;
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | +  @JsonProperty("permanencia")
swagger-client-repo-gen_1  | +  private Long permanencia = null;
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +  @JsonProperty("permanenciaFim")
swagger-client-repo-gen_1  | +  private Long permanenciaFim = null;
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +  @JsonProperty("prepago")
swagger-client-repo-gen_1  | +  private Boolean prepago = null;
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  |    @JsonProperty("rps")
swagger-client-repo-gen_1  |    private String rps = null;
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |    @JsonProperty("serieRps")
swagger-client-repo-gen_1  |    private String serieRps = null;
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | +  @JsonProperty("ticket")
swagger-client-repo-gen_1  | +  private String ticket = null;
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  |    /**
swagger-client-repo-gen_1  |     * O tipo do serviço pago.
swagger-client-repo-gen_1  |     */
swagger-client-repo-gen_1  | @@ -108,6 +120,9 @@ public class PagamentoEfetuado {
swagger-client-repo-gen_1  |    @JsonProperty("valorPago")
swagger-client-repo-gen_1  |    private Long valorPago = null;
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | +  @JsonProperty("valorDesconto")
swagger-client-repo-gen_1  | +  private Integer valorDesconto = null;
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  |    public PagamentoEfetuado cnpjGaragem(String cnpjGaragem) {
swagger-client-repo-gen_1  |      this.cnpjGaragem = cnpjGaragem;
swagger-client-repo-gen_1  |      return this;
swagger-client-repo-gen_1  | @@ -288,6 +303,60 @@ public class PagamentoEfetuado {
swagger-client-repo-gen_1  |      this.nsu = nsu;
swagger-client-repo-gen_1  |    }
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | +  public PagamentoEfetuado permanencia(Long permanencia) {
swagger-client-repo-gen_1  | +    this.permanencia = permanencia;
swagger-client-repo-gen_1  | +    return this;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +   /**
swagger-client-repo-gen_1  | +   * Data de entrada(Unix Epoch em milissegundos)
swagger-client-repo-gen_1  | +   * @return permanencia
swagger-client-repo-gen_1  | +  **/
swagger-client-repo-gen_1  | +  @ApiModelProperty(value = "Data de entrada(Unix Epoch em milissegundos)")
swagger-client-repo-gen_1  | +  public Long getPermanencia() {
swagger-client-repo-gen_1  | +    return permanencia;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +  public void setPermanencia(Long permanencia) {
swagger-client-repo-gen_1  | +    this.permanencia = permanencia;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +  public PagamentoEfetuado permanenciaFim(Long permanenciaFim) {
swagger-client-repo-gen_1  | +    this.permanenciaFim = permanenciaFim;
swagger-client-repo-gen_1  | +    return this;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +   /**
swagger-client-repo-gen_1  | +   * Uma previsão da data permitida para saída se o ticket for pago com o valor atual (Unix Epoch em milissegundos)
swagger-client-repo-gen_1  | +   * @return permanenciaFim
swagger-client-repo-gen_1  | +  **/
swagger-client-repo-gen_1  | +  @ApiModelProperty(value = "Uma previsão da data permitida para saída se o ticket for pago com o valor atual (Unix Epoch em milissegundos)")
swagger-client-repo-gen_1  | +  public Long getPermanenciaFim() {
swagger-client-repo-gen_1  | +    return permanenciaFim;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +  public void setPermanenciaFim(Long permanenciaFim) {
swagger-client-repo-gen_1  | +    this.permanenciaFim = permanenciaFim;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +  public PagamentoEfetuado prepago(Boolean prepago) {
swagger-client-repo-gen_1  | +    this.prepago = prepago;
swagger-client-repo-gen_1  | +    return this;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +   /**
swagger-client-repo-gen_1  | +   * Se o pagamento foi prepago
swagger-client-repo-gen_1  | +   * @return prepago
swagger-client-repo-gen_1  | +  **/
swagger-client-repo-gen_1  | +  @ApiModelProperty(value = "Se o pagamento foi prepago")
swagger-client-repo-gen_1  | +  public Boolean isPrepago() {
swagger-client-repo-gen_1  | +    return prepago;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +  public void setPrepago(Boolean prepago) {
swagger-client-repo-gen_1  | +    this.prepago = prepago;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  |    public PagamentoEfetuado rps(String rps) {
swagger-client-repo-gen_1  |      this.rps = rps;
swagger-client-repo-gen_1  |      return this;
swagger-client-repo-gen_1  | @@ -324,6 +393,24 @@ public class PagamentoEfetuado {
swagger-client-repo-gen_1  |      this.serieRps = serieRps;
swagger-client-repo-gen_1  |    }
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | +  public PagamentoEfetuado ticket(String ticket) {
swagger-client-repo-gen_1  | +    this.ticket = ticket;
swagger-client-repo-gen_1  | +    return this;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +   /**
swagger-client-repo-gen_1  | +   * O número do ticket
swagger-client-repo-gen_1  | +   * @return ticket
swagger-client-repo-gen_1  | +  **/
swagger-client-repo-gen_1  | +  @ApiModelProperty(value = "O número do ticket")
swagger-client-repo-gen_1  | +  public String getTicket() {
swagger-client-repo-gen_1  | +    return ticket;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +  public void setTicket(String ticket) {
swagger-client-repo-gen_1  | +    this.ticket = ticket;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  |    public PagamentoEfetuado tipo(TipoEnum tipo) {
swagger-client-repo-gen_1  |      this.tipo = tipo;
swagger-client-repo-gen_1  |      return this;
swagger-client-repo-gen_1  | @@ -360,6 +447,24 @@ public class PagamentoEfetuado {
swagger-client-repo-gen_1  |      this.valorPago = valorPago;
swagger-client-repo-gen_1  |    }
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | +  public PagamentoEfetuado valorDesconto(Integer valorDesconto) {
swagger-client-repo-gen_1  | +    this.valorDesconto = valorDesconto;
swagger-client-repo-gen_1  | +    return this;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +   /**
swagger-client-repo-gen_1  | +   * Valor do desconto aplicado na tarifa em centavos(R$1,50 &#x3D; 150)
swagger-client-repo-gen_1  | +   * @return valorDesconto
swagger-client-repo-gen_1  | +  **/
swagger-client-repo-gen_1  | +  @ApiModelProperty(value = "Valor do desconto aplicado na tarifa em centavos(R$1,50 = 150)")
swagger-client-repo-gen_1  | +  public Integer getValorDesconto() {
swagger-client-repo-gen_1  | +    return valorDesconto;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  | +  public void setValorDesconto(Integer valorDesconto) {
swagger-client-repo-gen_1  | +    this.valorDesconto = valorDesconto;
swagger-client-repo-gen_1  | +  }
swagger-client-repo-gen_1  | +
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |    @Override
swagger-client-repo-gen_1  |    public boolean equals(java.lang.Object o) {
swagger-client-repo-gen_1  | @@ -380,15 +485,20 @@ public class PagamentoEfetuado {
swagger-client-repo-gen_1  |          Objects.equals(this.nfseNumero, pagamentoEfetuado.nfseNumero) &&
swagger-client-repo-gen_1  |          Objects.equals(this.nfseQrCode, pagamentoEfetuado.nfseQrCode) &&
swagger-client-repo-gen_1  |          Objects.equals(this.nsu, pagamentoEfetuado.nsu) &&
swagger-client-repo-gen_1  | +        Objects.equals(this.permanencia, pagamentoEfetuado.permanencia) &&
swagger-client-repo-gen_1  | +        Objects.equals(this.permanenciaFim, pagamentoEfetuado.permanenciaFim) &&
swagger-client-repo-gen_1  | +        Objects.equals(this.prepago, pagamentoEfetuado.prepago) &&
swagger-client-repo-gen_1  |          Objects.equals(this.rps, pagamentoEfetuado.rps) &&
swagger-client-repo-gen_1  |          Objects.equals(this.serieRps, pagamentoEfetuado.serieRps) &&
swagger-client-repo-gen_1  | +        Objects.equals(this.ticket, pagamentoEfetuado.ticket) &&
swagger-client-repo-gen_1  |          Objects.equals(this.tipo, pagamentoEfetuado.tipo) &&
swagger-client-repo-gen_1  | -        Objects.equals(this.valorPago, pagamentoEfetuado.valorPago);
swagger-client-repo-gen_1  | +        Objects.equals(this.valorPago, pagamentoEfetuado.valorPago) &&
swagger-client-repo-gen_1  | +        Objects.equals(this.valorDesconto, pagamentoEfetuado.valorDesconto);
swagger-client-repo-gen_1  |    }
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |    @Override
swagger-client-repo-gen_1  |    public int hashCode() {
swagger-client-repo-gen_1  | -    return Objects.hash(cnpjGaragem, codigoAutorizacao, cpfCnpj, data, estaticonamento, linkLogoGaragem, nfseCodigoVerificacao, nfseNumero, nfseQrCode, nsu, rps, serieRps, tipo, valorPago);
swagger-client-repo-gen_1  | +    return Objects.hash(cnpjGaragem, codigoAutorizacao, cpfCnpj, data, estaticonamento, linkLogoGaragem, nfseCodigoVerificacao, nfseNumero, nfseQrCode, nsu, permanencia, permanenciaFim, prepago, rps, serieRps, ticket, tipo, valorPago, valorDesconto);
swagger-client-repo-gen_1  |    }
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | @@ -407,10 +517,15 @@ public class PagamentoEfetuado {
swagger-client-repo-gen_1  |      sb.append("    nfseNumero: ").append(toIndentedString(nfseNumero)).append("\n");
swagger-client-repo-gen_1  |      sb.append("    nfseQrCode: ").append(toIndentedString(nfseQrCode)).append("\n");
swagger-client-repo-gen_1  |      sb.append("    nsu: ").append(toIndentedString(nsu)).append("\n");
swagger-client-repo-gen_1  | +    sb.append("    permanencia: ").append(toIndentedString(permanencia)).append("\n");
swagger-client-repo-gen_1  | +    sb.append("    permanenciaFim: ").append(toIndentedString(permanenciaFim)).append("\n");
swagger-client-repo-gen_1  | +    sb.append("    prepago: ").append(toIndentedString(prepago)).append("\n");
swagger-client-repo-gen_1  |      sb.append("    rps: ").append(toIndentedString(rps)).append("\n");
swagger-client-repo-gen_1  |      sb.append("    serieRps: ").append(toIndentedString(serieRps)).append("\n");
swagger-client-repo-gen_1  | +    sb.append("    ticket: ").append(toIndentedString(ticket)).append("\n");
swagger-client-repo-gen_1  |      sb.append("    tipo: ").append(toIndentedString(tipo)).append("\n");
swagger-client-repo-gen_1  |      sb.append("    valorPago: ").append(toIndentedString(valorPago)).append("\n");
swagger-client-repo-gen_1  | +    sb.append("    valorDesconto: ").append(toIndentedString(valorDesconto)).append("\n");
swagger-client-repo-gen_1  |      sb.append("}");
swagger-client-repo-gen_1  |      return sb.toString();
swagger-client-repo-gen_1  |    }
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoRequest.java b/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoRequest.java
swagger-client-repo-gen_1  | index 6ab27eb..accc01c 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoRequest.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/PagamentoRequest.java
swagger-client-repo-gen_1  | @@ -28,7 +28,7 @@ import java.util.List;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * PagamentoRequest
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/Promocao.java b/src/main/java/cash/super_/platform/client/parkingplus/model/Promocao.java
swagger-client-repo-gen_1  | index 33618ce..3e097fa 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/Promocao.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/Promocao.java
swagger-client-repo-gen_1  | @@ -27,7 +27,7 @@ import org.joda.time.DateTime;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * Promocao
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoConsulta.java b/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoConsulta.java
swagger-client-repo-gen_1  | index f93131b..f27b337 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoConsulta.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoConsulta.java
swagger-client-repo-gen_1  | @@ -27,7 +27,7 @@ import java.util.List;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * RetornoConsulta
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoCreditarCartao.java b/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoCreditarCartao.java
swagger-client-repo-gen_1  | index 4bef1bd..843ba7d 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoCreditarCartao.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoCreditarCartao.java
swagger-client-repo-gen_1  | @@ -24,7 +24,7 @@ import io.swagger.annotations.ApiModelProperty;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * RetornoCreditarCartao
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoErro.java b/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoErro.java
swagger-client-repo-gen_1  | index 2c495b1..afe0c1a 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoErro.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoErro.java
swagger-client-repo-gen_1  | @@ -24,7 +24,7 @@ import io.swagger.annotations.ApiModelProperty;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * RetornoErro
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoPagamento.java b/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoPagamento.java
swagger-client-repo-gen_1  | index 1ad62a8..8e68793 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoPagamento.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/RetornoPagamento.java
swagger-client-repo-gen_1  | @@ -24,7 +24,7 @@ import io.swagger.annotations.ApiModelProperty;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * RetornoPagamento
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | diff --git a/src/main/java/cash/super_/platform/client/parkingplus/model/TicketRequest.java b/src/main/java/cash/super_/platform/client/parkingplus/model/TicketRequest.java
swagger-client-repo-gen_1  | index 62d8ae2..28198f4 100644
swagger-client-repo-gen_1  | --- a/src/main/java/cash/super_/platform/client/parkingplus/model/TicketRequest.java
swagger-client-repo-gen_1  | +++ b/src/main/java/cash/super_/platform/client/parkingplus/model/TicketRequest.java
swagger-client-repo-gen_1  | @@ -26,7 +26,7 @@ import java.util.List;
swagger-client-repo-gen_1  |  /**
swagger-client-repo-gen_1  |   * TicketRequest
swagger-client-repo-gen_1  |   */
swagger-client-repo-gen_1  | -@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-06T03:48:42.172Z")
swagger-client-repo-gen_1  | +@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-10T17:02:09.002Z")
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | - Update commit...
swagger-client-repo-gen_1  | [develop 6e4d854] :new:  Updating client API
swagger-client-repo-gen_1  |  23 files changed, 1903 insertions(+), 24 deletions(-)
swagger-client-repo-gen_1  |  create mode 100644 src/main/resources/parking-plus-update.json
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | 📦 Skip publishing stubs to Maven repo. Set GENERATE_CLIENT_PUBLISH_TOKEN=token if needed!
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | 🚚 Pushing the code to the git host. Make sure to have the ssh keys mounted!
swagger-client-repo-gen_1  | remote:
swagger-client-repo-gen_1  | remote: To create a merge request for develop, visit:
swagger-client-repo-gen_1  | remote:   https://gitlab.com/supercash/clients/parking-plus-client-feign/-/merge_requests/new?merge_request%5Bsource_branch%5D=develop
swagger-client-repo-gen_1  | remote:
swagger-client-repo-gen_1  | To gitlab.com:supercash/clients/parking-plus-client-feign.git
swagger-client-repo-gen_1  |    860bb72..6e4d854  develop -> develop
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | 💥 Deleting previous build from directory '/client-api/parking-plus-client-feign'
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | 🍻 Local deploy to /client-api/parking-plus-client-feign
swagger-client-repo-gen_1  | 'parking-plus-client-feign/' -> '/client-api/parking-plus-client-feign'
swagger-client-repo-gen_1  | 'parking-plus-client-feign/.git' -> '/client-api/parking-plus-client-feign/.git'
swagger-client-repo-gen_1  | 'parking-plus-client-feign/.git/branches' -> '/client-api/parking-plus-client-feign/.git/branches'
swagger-client-repo-gen_1  | 'parking-plus-client-feign/.git/info' -> '/client-api/parking-plus-client-feign/.git/info'
swagger-client-repo-gen_1  | 'parking-plus-client-feign/.git/info/exclude' -> '/client-api/parking-plus-client-feign/.git/info/exclude'
swagger-client-repo-gen_1  | 'parking-plus-client-feign/.git/hooks' -> '/client-api/parking-plus-client-feign/.git/hooks'
swagger-client-repo-gen_1  | 'parking-plus-client-feign/.git/hooks/pre-receive.sample' -> '/client-api/parking-plus-client-feign/.git/hooks/pre-receive.sample'
...
...
...
swagger-client-repo-gen_1  | 'parking-plus-client-feign/target/classes/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.class' -> '/client-api/parking-plus-client-feign/target/classes/cash/super_/platform/client/parkingplus/model/CriptografarCartaoRequest.class'
swagger-client-repo-gen_1  | 'parking-plus-client-feign/target/apidocs/help-doc.html' -> '/client-api/parking-plus-client-feign/target/apidocs/help-doc.html'
...
...
...
swagger-client-repo-gen_1  | 'parking-plus-client-feign/target/apidocs/stylesheet.css' -> '/client-api/parking-plus-client-feign/target/apidocs/stylesheet.css'
swagger-client-repo-gen_1  | 'parking-plus-client-feign/target/apidocs/script.js' -> '/client-api/parking-plus-client-feign/target/apidocs/script.js'
swagger-client-repo-gen_1  |
swagger-client-repo-gen_1  | ✨ Done!
swagger-client-pacakge-repo-gen_swagger-client-repo-gen_1 exited with code 0
```
