#!/bin/bash

. ./.myconfig.sh

case $USER in
  codespace)
  WORKSPACE=/workspaces
  ;;
  *)
  WORKSPACE=$PWD
  ;;
esac

script="quarto render short.qmd --output-dir _html" 
# Check if the container is running. If yes, re-use it, if not, run it.

docker ps | grep $space/$repo:$tag
if [[ $? -eq 0 ]]
then
  echo "Container is running, reusing it"
  docker exec  -w /home/rstudio/project/presentation rstudio $script
else
  echo "Container is not running, starting it"
  docker run --rm -v "$WORKSPACE":/home/rstudio/project -w /home/rstudio/project/presentation $dockerrepo:$tag $script
fi  