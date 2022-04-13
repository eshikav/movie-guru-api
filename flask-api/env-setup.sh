action=$1
application=$2
tag=$3

cleanImages(){
echo "Removing all the container images for the application $application:$tag"
docker rmi $application:$tag
}

buildImages(){
echo "Building the container image"
docker build --no-cache -t $application:$tag .

}

deleteContainer(){
echo "Deleting all the containers created"
docker rm -f $application
}

runContainer(){
echo "Running the container with $application with $tag"
docker run -p 127.0.0.1:5000:5000/tcp --name $application -d  $application:$tag
}

clean(){
deleteContainer
cleanImages
}


setup(){
echo "Building the container images"
buildImages
runContainer
}

if [[ $action == "clean" ]]
then
echo 'Cleaning environment for the application'
clean
else
echo 'Setting environment for the $i application'
setup
fi
