# Note: Don't do FROM base <- will pull an old version of ubuntu
#       or if you do follow this advice for accessing old repos:
#       https://smyl.es/how-to-fix-ubuntudebian-apt-get-404-not-found-package-repository-errors-saucy-raring-quantal-oneiric-natty/

FROM ubuntu:14.04
MAINTAINER Michael Bright <dockerfiles@mjbright.net>

RUN apt-get update
RUN cat /etc/apt/sources.list
RUN sed -i.bak 's/^deb-src/# deb-src/' /etc/apt/sources.list
#RUN cat /etc/resolv.conf

#RUN grep -v "^#" /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive apt-get -y upgrade

# Install packages
RUN mkdir -p /var/run/sshd 
RUN chmod 7555 /var/run/sshd 
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server
# Fix for ssh login issue: (Exit 254 immediately after successful authenticn)
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config

# Misc:
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tar build-essential curl git-core vim sudo

#ADD root.bashrc /root/.bashrc
# Default command
CMD bash

RUN adduser --gecos "" --disabled-password user
#RUN adduser --gecos "" --ingroup rvm --disabled-password user
ADD user.bashrc /home/user/.bashrc
RUN echo 'user:user' |chpasswd

RUN chmod 755 /home/user/.bashrc

RUN adduser user sudo

# Expose default ports for ssh/nginx/django:
EXPOSE 22
EXPOSE 80
EXPOSE 8080

# Restart ssh server and loop - login via ssh
ENTRYPOINT /etc/init.d/ssh start; while true; do sleep 60; done


