FROM maven:3.6.3-jdk-8-slim

# Depedencies
RUN apt-get update && apt-get install -y python git

WORKDIR /generator

# Get dependencies for the current
COPY pom.xml .
RUN mvn dependency:resolve-plugins dependency:go-offline

COPY entrypoint.sh .
COPY update-generated-project.py .
COPY cicd/ cicd/

VOLUME /schemas
VOLUME /client-api

CMD ["/generator/entrypoint.sh"]
