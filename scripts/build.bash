export tag="latest"
export game="tankman"

docker build \
-t ${game}:${tag} \
-f ./Dockerfile .
