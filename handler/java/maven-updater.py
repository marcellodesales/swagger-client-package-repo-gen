# -*- coding: utf-8 -*-
from xml.etree import ElementTree as et
import os
import shutil

# pom file location
pomFileName = "{}/pom.xml".format(os.environ["CLIENT_API_LOCATION"])
pomFile = None
try:
  pomFile = open(pomFileName, 'r')
except IOError:
  print "The file {} couldn't be found! Please check the build!".format(pomFileName)
  sys.exit(2)

# https://stackabuse.com/reading-and-writing-xml-files-in-python/
tree = et.parse(pomFileName)
pomRoot = tree.getroot()
et.register_namespace("", "http://maven.apache.org/POM/4.0.0")

for element in pomRoot:
  if "groupId" in element.tag:
    element.text = os.environ["GENERATE_CLIENT_GROUPID"]
    print "Set {} = {}".format(element.tag, element.text)

  if "artifactId" in element.tag or "name" in element.tag:
    element.text = os.environ["GENERATE_CLIENT_ARTIFACT"]
    print "Set {} = {}".format(element.tag, element.text)

  if "version" in element.tag:
    element.text = os.environ["GENERATE_CLIENT_VERSION"]
    if "RELEASE" in element.text and "master" != os.environ["GENERATE_CLIENT_GIT_BRANCH"]:
      element.text = element.text.replace("RELEASE", "SNAPSHOT")
    print "Set {} = {}".format(element.tag, element.text)

  if "url" in element.tag:
    element.text = os.environ["GENERATE_CLIENT_URL"]
    element.text = "{}-{}".format(element.text, os.environ["GENERATE_CLIENT_WITH_LIBRARY"])
    print "Set {} = {}".format(element.tag, element.text)

  if "description" in element.tag:
    element.text = "Swagger {} Client stubs".format(os.environ["GENERATE_CLIENT_WITH_LIBRARY"])
    print "Set {} = {}".format(element.tag, element.text)

  if "scm" in element.tag:
    for scmElement in element:
      if "connection" in scmElement.tag or "developerConnection" in scmElement.tag:
        scmElement.text = scmElement.text.replace("github.com", os.environ["GENERATE_CLIENT_GIT_HOST"])
        scmElement.text = scmElement.text.replace("swagger-api/swagger-codegen", os.environ["GENERATE_CLIENT_GIT_USER_REPO"])
        scmElement.text = scmElement.text.replace(".git", "-{}.git".format(os.environ["GENERATE_CLIENT_WITH_LIBRARY"]))
        print "Set {} = {}".format(scmElement.tag, scmElement.text)

      if "url" in scmElement.tag:
        scmElement.text = os.environ["GENERATE_CLIENT_URL"]
        scmElement.text = "{}-{}".format(scmElement.text, os.environ["GENERATE_CLIENT_WITH_LIBRARY"])
        print "Set {} = {}".format(scmElement.tag, scmElement.text)

  if "developers" in element.tag:
    for developersElement in element:
      if "developer" in developersElement.tag:
        for developerElement in developersElement:
          if "name" in developerElement.tag:
            developerElement.text = os.environ["GENERATE_CLIENT_AUTHOR_FULLNAME"]
            print "Set {} = {}".format(developerElement.tag, developerElement.text)

          if "email" in developerElement.tag:
            developerElement.text = os.environ["GENERATE_CLIENT_AUTHOR_EMAIL"]
            print "Set {} = {}".format(developerElement.tag, developerElement.text)

          if "organization" in developerElement.tag and not "organizationUrl" in developerElement.tag:
            # This is the Organization of the git repo for now
            developerElement.text = os.environ["GENERATE_CLIENT_GIT_USER_REPO"].split("/")[0]
            print "Set {} = {}".format(developerElement.tag, developerElement.text)

          if "organizationUrl" in developerElement.tag:
            org = os.environ["GENERATE_CLIENT_GIT_USER_REPO"].split("/")[0]
            developerElement.text = "https://{}/{}".format(os.environ["GENERATE_CLIENT_GIT_HOST"], org)
            print "Set {} = {}".format(developerElement.tag, developerElement.text)

clientDir = "client-api/"
if "gitlab" in os.environ["GENERATE_CLIENT_GIT_HOST"]:
  print ""
  print "🚧 Generating CI/CD artifacts for Gitlab Project {}".format(os.environ["GENERATE_CLIENT_GITLAB_PROJECT_ID"])

  print "- Adding ci_settings.xml"
  shutil.copy2("/generator/cicd/gitlab/maven/ci_settings.xml", clientDir)

  print "- Adding personal_settings.xml"
  shutil.copy2("/generator/cicd/gitlab/maven/personal_settings.xml", clientDir)

  print "- Adding .gitlab-ci.yml"
  shutil.copy2("/generator/cicd/gitlab/maven/.gitlab-ci.yml", clientDir)

  print "- Generating the maven repos in Maven for Gitlab"
  templateFile = "/generator/cicd/gitlab/maven/repos.xml"
  cicdFile = clientDir + "cicd-maven.xml"

  # DO NOT UPDATE IF THE FILE ALREADY CONTAINS THE PROJECT_ID DURING UPDATES
  found = False
  #print "Looking for the projectId = {} on the pom.xml".format(os.environ["GENERATE_CLIENT_GITLAB_PROJECT_ID"])
  for line in pomFile:
    #print "pom.xml: {}".format(line)
    if os.environ["GENERATE_CLIENT_GITLAB_PROJECT_ID"] in line:
      #print "pom.xml: Found {} in Line: {}".format(os.environ["GENERATE_CLIENT_GITLAB_PROJECT_ID"], line)
      found = True
      break

  # The project ID is in the file, so the repos are already setup
  if not found:
    print "- The current pom.xml does NOT contain projectId {}".format(os.environ["GENERATE_CLIENT_GITLAB_PROJECT_ID"])
  
    # Go through the file and copy it to the client's dir
    # https://stackoverflow.com/questions/62441317/best-way-to-replace-a-list-of-tokens-in-a-text-file/62452776#62452776
    with open(templateFile, 'rb') as fi, open(cicdFile, 'wb') as fo:
      for line in fi:
        if "PROJECT_ID" in line:
          line = line.replace("PROJECT_ID", os.environ["GENERATE_CLIENT_GITLAB_PROJECT_ID"])
        fo.write(line)

    # Just making sure the file was created and it's not empty
    try:
      file = open(cicdFile, 'r')
      if os.stat(cicdFile).st_size == 0:
        raise IOError("The CI/CD was supposed to be generated, but it is empty!")

    except IOError:
      print "The cicdFile '{}' couldn't be generated for Gitlab!".format(cicdFile)
      sys.exit(3)

    # Merge the generated cicd file with repo info with the pom.xml
    cicdTree = et.parse(cicdFile)
    cicdRoot = cicdTree.getroot()
    # Go through the repos elements (2) and append to the root of pom.xml
    for cicdElement in cicdRoot:
      pomRoot.append(cicdElement)

    # Just delete the repos file
    os.remove(cicdFile)

# Write the final pom.xml file
tree.write(pomFileName)
