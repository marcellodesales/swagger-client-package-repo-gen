# -*- coding: utf-8 -*-
from xml.etree import ElementTree as et
import os
import shutil

pomFile = "springboot-client-api/pom.xml"
try:
  file = open(pomFile, 'r')
except IOError:
  print "The file {} couldn't be found! Please check the build!".format(pomFile)
  sys.exit(2)

# https://stackabuse.com/reading-and-writing-xml-files-in-python/
tree = et.parse(pomFile)
pomRoot = tree.getroot()
et.register_namespace("", "http://maven.apache.org/POM/4.0.0")

for element in pomRoot:
  if "groupId" in element.tag:
    element.text = os.environ["GENERATE_CLIENT_GROUPID"]
    print "Set {} = {}".format(element.tag, element.text)

  if "artifactId" in element.tag or "name" in element.tag:
    element.text = "{}-{}".format(os.environ["GENERATE_CLIENT_ARTIFACT"], os.environ["GENERATE_CLIENT_WITH_LIBRARY"])
    print "Set {} = {}".format(element.tag, element.text)

  if "version" in element.tag:
    element.text = os.environ["GENERATE_CLIENT_VERSION"]
    if "SNAPSHOT" not in element.text:
      element.text = "{}-SNAPSHOT".format(element.text)
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

        cloneUrl = "git@{}:{}-{}.git".format(os.environ["GENERATE_CLIENT_GIT_HOST"], os.environ["GENERATE_CLIENT_GIT_USER_REPO"], os.environ["GENERATE_CLIENT_WITH_LIBRARY"])
        cloneFile = open("git-remote.txt","w")
        cloneFile.writelines(cloneUrl)
        cloneFile.close()

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

if "gitlab" in os.environ["GENERATE_CLIENT_GIT_HOST"]:
  print ""
  print "🚧 Generating CI/CD artifacts for Gitlab Project {}".format(os.environ["GENERATE_CLIENT_GITLAB_PROJECT_ID"])

  print "- Adding ci_settings.xml"
  shutil.copy2("/generator/cicd/gitlab/maven/ci_settings.xml", "springboot-client-api/")

  print "- Adding personal_settings.xml"
  shutil.copy2("/generator/cicd/gitlab/maven/personal_settings.xml", "springboot-client-api/")

  print "- Adding .gitlab-ci.yml"
  shutil.copy2("/generator/cicd/gitlab/maven/.gitlab-ci.yml", "springboot-client-api/")

  print "- Generating the maven repos in Maven for Gitlab"
  templateFile = "/generator/cicd/gitlab/maven/repos.xml"
  cicdFile = "springboot-client-api/cicd-maven.xml"

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

  # Merge the generated cicd file with the pom.xml
  cicdTree = et.parse(cicdFile)
  cicdRoot = cicdTree.getroot()
  # Go through the repos elements (2) and append to the root of pom.xml
  for cicdElement in cicdRoot:
    pomRoot.append(cicdElement)

  # Just delete the repos file
  os.remove(cicdFile)

# Write the final pom.xml file
tree.write(pomFile)
