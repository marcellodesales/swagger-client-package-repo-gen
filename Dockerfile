ARG GITHUB_REPO
ARG GITHUB_SHA
ARG DATE

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

# https://github.com/opencontainers/image-spec/blob/main/annotations.md
LABEL org.opencontainers.image.source ${GITHUB_REPO}
LABEL org.opencontainers.image.revision ${GITHUB_SHA}
LABEL org.opencontainers.image.created ${DATE}


CMD ["/bin/bash", "/generator/entrypoint.sh"]
