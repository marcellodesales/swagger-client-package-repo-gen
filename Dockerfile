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
# Labels are added dynamicall by the pipeline for the proper mapping
# docker build --label org.opencontainers.image.created="$(date)" 
#              --label org.opencontainers.image.source=https://value 
#              --label org.opencontainers.image.revision=fos939dsi -t my-image .

CMD ["/bin/bash", "/generator/entrypoint.sh"]
