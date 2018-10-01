set -e

if [ -z "$PREFIX" ]; then
    echo 'PREFIX variable is not set'
    exit 1
fi

if [ -z "$IMAGE" ]; then
    echo 'IMAGE variable is not set'
    exit 1
fi

if [ -z "$DC_USER" ]; then
    echo 'DC_USER variable is not set'
    exit 1
fi

if [ -z "$DC_PASS" ]; then
    echo 'DC_PASS variable is not set'
    exit 1
fi

version=`cat VERSION`
echo "version: $version"

if [ -z "$version" ]; then
    echo 'version variable is not set'
    exit 1
fi

docker build -t $PREFIX/$IMAGE:latest -f production.Dockerfile .

# tag it
docker tag $PREFIX/$IMAGE:latest $PREFIX/$IMAGE:$version

# login docker hub
docker login -u $DC_USER -p $DC_PASS

# push it
echo "publishing latest: ${PREFIX}/${IMAGE}:latest"
docker push ${PREFIX}/${IMAGE}:latest
echo "publishing version: ${PREFIX}/${IMAGE}:${version}"
docker push ${PREFIX}/${IMAGE}:${version}
