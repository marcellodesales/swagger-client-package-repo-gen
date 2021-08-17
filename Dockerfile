FROM maven:3.6.3-jdk-8-slim

# Depedencies
RUN apt-get update && apt-get install -y python git curl jq

WORKDIR /generator

# Get dependencies for the current
COPY pom.xml .
RUN mvn dependency:resolve-plugins dependency:go-offline

COPY entrypoint.sh .
COPY handler handler/
COPY cicd/ cicd/

VOLUME /schemas
VOLUME /client-api

CMD ["/bin/bash", "/generator/entrypoint.sh"]
