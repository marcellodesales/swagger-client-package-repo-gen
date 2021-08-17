#!/bin/bash

if [ ! -z "${LOG}" ]; then
  echo "ACTION=${ACTION}: Will create the repo"
fi

###### INPUT REQUIRED
# Personal Token
TOKEN=${GITLAB_TOKEN:?"ERROR: Must provide the Gitlab token"}


GITLAB_HOST=${GITLAB_HOST:?"ERROR: Must provide the Gitlab host"}
# Gitlab full group name, like suborg/org
GITLAB_GROUP=${GITLAB_GROUP:?"ERROR: Must provide the Gitlab group (org/suborg)"}

# The name of the new repo 
GITLAB_REPO=${GITLAB_NEW_REPO_NAME:?"ERROR: Must provide the name of the repo"}
GITLAB_REPO_DESC=${GITLAB_NEW_REPO_DESCRIPTION:?"ERROR: Must provide the description for the app"}

#### PROCESS VVVVVVVVVVVVVVVVVVV

# https://stackoverflow.com/questions/296536/how-to-urlencode-data-for-curl-command/34407620#34407620
GROUP_ENCODED=$(printf "${GITLAB_GROUP}" 'encode this' | jq -sRr @uri)
GROUP_DESC_ENCODED=$(printf "${GITLAB_REPO_DESC}" 'encode this' | jq -sRr @uri)

# https://docs.gitlab.com/ee/api/groups.html
GROUP_PROFILE_JSON=$(curl -s --header "PRIVATE-TOKEN: $TOKEN" "https://${GITLAB_HOST}/api/v4/groups/${GROUP_ENCODED}")
GROUP_ID=$(echo ${GROUP_PROFILE_JSON} | jq -r '.id')

if [ ! -z ${LOG} ]; then
  echo "* The repository will be created under Group ID GITLAB_GROUP ${GITLAB_GROUP} => ID[${GROUP_ID}]"
fi

# try creating in the first attempt without knowing if it exists or not
NEW_REPO_JSON=$(curl -s --header "PRIVATE-TOKEN: ${TOKEN}" -X POST "https://${GITLAB_HOST}/api/v4/projects?name=${GITLAB_REPO}&default_branch=master&namespace_id=${GROUP_ID}&description=${GROUP_DESC_ENCODED}")
NEW_REPO_ID=$(echo $NEW_REPO_JSON | jq -r '.id')
NEW_REPO_NAMESPACE_PATH=$(echo $NEW_REPO_JSON | jq -r '.web_url')

# if the repo already exists
if [ "${NEW_REPO_ID}" == "null" ]; then

  # Attempt to delete the existing repo and creating it again
  if [ "${FORCE_CREATE}" == "true" ]; then
    # The project creatil failed, but we can delete the existing one
    GITLAB_PROJECT_PATH="${GITLAB_GROUP}/${GITLAB_NEW_REPO_NAME}"
 
    # https://stackoverflow.com/questions/34911622/dockerfile-set-env-to-result-of-command/68290395#68290395
    # https://stackoverflow.com/questions/40027395/passing-bash-variable-to-jq/40027637#40027637
    PROJECTS_LIST_JSON=$(curl -s --header "PRIVATE-TOKEN: ${TOKEN}" -X GET https://${GITLAB_HOST}/api/v4/projects?owned=true)
    GITLAB_PROJECT_ID=$(echo ${PROJECTS_LIST_JSON} | jq --arg PATH "$GITLAB_PROJECT_PATH" '.[] | select(.path_with_namespace == $PATH).id')

    if [ ! -z ${LOG} ]; then
      echo "INFO: Deleting project ${GITLAB_PROJECT_PATH} [ID=${GITLAB_PROJECT_ID}] before creating again..."
    fi

    # https://docs.gitlab.com/ee/api/projects.html#delete-project
    DELETE_RESULT=$(curl -s --header "PRIVATE-TOKEN: ${TOKEN}" -X DELETE https://${GITLAB_HOST}/api/v4/projects/${GITLAB_PROJECT_ID})
    DELETE_RESULT=$(echo $DELETE_RESULT | jq -r '.message')

    if [ "${DELETE_RESULT}" == "202 Accepted" ]; then
      if [ ! -z "${LOG}" ]; then
        echo "* Successfully deleted project"
      fi
    else
      if [ ! -z "${LOG}" ]; then
        echo "ERROR: Failed deleting the project: ${DELETE_RESULT}"
        exit 3
      fi
    fi

    if [ ! -z "${LOG}" ]; then
      echo "INFO: Re-creating project after deletion..."
    fi

    # Just wait for a bit before it can accept new creation
    sleep 5

    NEW_REPO_JSON=$(curl -s --header "PRIVATE-TOKEN: ${TOKEN}" -X POST "https://${GITLAB_HOST}/api/v4/projects?name=${GITLAB_REPO}&default_branch=master&namespace_id=${GROUP_ID}&description=${GROUP_DESC_ENCODED}")
    NEW_REPO_ID=$(echo $NEW_REPO_JSON | jq -r '.id')
    NEW_REPO_NAMESPACE_PATH=$(echo $NEW_REPO_JSON | jq -r '.web_url')
 
  else
   # It should fail the creation

   if [ "$FORMAT" == "json" ]; then
     echo "{ \"id\": null, \"error\": \"Could not create project. Try FORCE_CREATE=true to override\" }"

   else
     echo ""
   fi

   # Just exit
   exit 2;
  fi
fi

if [ ! -z ${LOG} ]; then
  echo "* Created repository at ${NEW_REPO_NAMESPACE_PATH} => ID[${NEW_REPO_ID}]"
fi

if [ "$FORMAT" == "json" ]; then
  echo "{ \"id\": ${NEW_REPO_ID}, \"url\": \"${NEW_REPO_NAMESPACE_PATH}\", \"error\": null }"
else
  echo "${NEW_REPO_ID}"
fi
