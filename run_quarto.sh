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

docker run --rm -v "$WORKSPACE":/home/rstudio -w /home/rstudio/presentation $dockerrepo:$tag quarto render index.qmd