#!/bin/bash


PWD=$(pwd)
. ${PWD}/.myconfig.sh

if [[ "$1" == "-h" ]]
then
cat << EOF
$0 (tag)

will start interactive environment for tag (TAG)
EOF
exit 0
fi

if [[ ! -z "$1" ]]
then
  tag=${1}
fi
shift

if [[ ! -z "$1" ]]
then
  echo "Passing additional arguments to docker run: $@"
  DOCKEREXTRA="$DOCKEREXTRA -it"
fi

echo "Using tag = $tag"

case $USER in
  codespace)
  WORKSPACE=/workspaces
  ;;
  *)
  WORKSPACE=$PWD
  ;;
esac
  
# pull the docker if necessary
set -v

echo $space/$repo
tag_present=$(docker images | grep $space/$repo | awk ' { print $2 } ' | grep $tag)

if [[ -z "$tag_present" ]]
then
  echo "Pulling $space/$repo:$tag"
  docker pull $space/$repo:$tag
else  
  echo "Found $space/$repo:$tag"
fi

# map cache if present

if [[ -d $WORKSPACE/.cache ]]
then
  echo "Found cache"
  # Ensure cache directory is writable
  chmod a+rwX $WORKSPACE/.cache
  DOCKEREXTRA="$DOCKEREXTRA -v $WORKSPACE/.cache:/home/rstudio/.cache"
fi

docker run $DOCKEREXTRA -e DISABLE_AUTH=true \
  --name rstudio \
  -e RENV_PATHS_CACHE=/home/rstudio/.cache -v "$WORKSPACE":/home/rstudio/project -w /home/rstudio/project --rm -p 8787:8787  -p 3456:3456 $space/$repo:$tag $@
