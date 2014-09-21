
CODE=$HOME/z/bin/py/TDD-with-Python/superlists

PYTHON=python3

# On Windows machine, use Anaconda Python (which is Python3):
[ `hostname` = "MJBRIGHT7" ] && PYTHON=python # python3/Anaconda

########################################
# Utility functions:

die() {
    echo "$0: die - $*" >&2
    exit 1
}

press() {
    echo $*
    echo "Press <return> to continue"
    read _DUMMY
    [ "$_DUMMY" = "q" ] && exit 0
    [ "$_DUMMY" = "Q" ] && exit 0
}

########################################
# Functions:

sshtunnel() {
    echo
    echo "First start ssh tunnel to staging server using command:"
    echo "    ssh -Nv -L 80:127.0.0.1:80 b10cpq"
    echo
    read _dummy
}

runserver() {
    cd $CODE
    $PYTHON manage.py runserver
}

tests() {
    cd $CODE
    $PYTHON manage.py test
}

utests() {
    cd $CODE
    $PYTHON manage.py test lists
}

ftests() {
    cd $CODE
    $PYTHON manage.py test functional_tests
}


########################################
# args:

ACTION=NONE

while [ ! -z "$1" ];do
    case $1 in
        -r) ACTION=RUN_SERVER;;
        -t) ACTION=RUN_TESTS;;
        -u) ACTION=RUN_UNITTESTS;;
        -f) ACTION=RUN_FUNCTESTS;;
        *)  die "Bad option: '$1'";;
    esac
    shift
done

########################################
# main:


[ $ACTION = "RUN_SERVER" ]	&& runserver
[ $ACTION = "RUN_TESTS" ]	&& tests
[ $ACTION = "RUN_UNITTESTS" ]	&& utests
[ $ACTION = "RUN_FUNCTESTS" ]	&& ftests


