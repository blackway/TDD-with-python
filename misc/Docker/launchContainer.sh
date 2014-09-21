
NAME=TDD
IMAGE_GREP=TDD
TAG=mine:TDD

CMD="/etc/init.d/ssh restart; while true; do sleep 10; done'"
[ ! -z "$1" ] && CMD="$1"

########################################
# functions:

die() {
    echo "$0: die - $*" >&2
    exit 1
}

UNUSEDcreateDockerDir() {
    DIR="$HOME/Docker/$NAME"
    [ ! -d $DIR ] && {
        echo "mkdir -p $DIR";
        mkdir -p $DIR;
    }
}

checkPortNotListening() {
    PORT=$1; shift

    echo "Checking that tcp port $PORT is not in use:"
    netstat -an | grep -E "tcp .*:$PORT .*LISTEN" && {
        die "Error: port $PORT is already in use"
    }
}


########################################
# main:

## MOUNT:
#MOUNT="-v $DIR:/home/user/TDD"
MOUNT=""

## SSH:
SSH_PORT=2222
#PORTS="-p $SSH_PORT:22 -p 3000:3000"
#PORTS="-p $SSH_PORT:22"
#PORTS="-p $SSH_PORT:22 -p 80:80 -p 8080:8080"
PORTS="-p $SSH_PORT:22 -p 8080:80"

echo
echo "SSH listening on port $SSH_PORT"
echo
echo "You may want to change the ssh 'user' password"
echo
#echo "docker run -i -t $PORTS $MOUNT $TAG bash -lc "$CMD""
#exit 0
#set -x
echo "MOUNT: $MOUNT"
echo "PORTS: $PORTS"
#docker run -i -t $PORTS $MOUNT $TAG bash -lc "$CMD"

checkPortNotListening 2222
#checkPortNotListening 80
checkPortNotListening 8080
docker run -d $PORTS $MOUNT $TAG bash -lc "$CMD"

#LATEST_IMAGE=$(docker images | grep $IMAGE_GREP | head -1 | awk '{print $1;}')
#docker run -d -p 2222:22 -v /home/mjb/RAILS:/tmp $LATEST_IMAGE bash -c '/etc/init.d/sshd start; while true; do sleep 10; done'

docker ps -l

