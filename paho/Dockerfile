FROM python:3.6
ARG USER=user
ARG GROUP=developer
ARG PASS=your_password

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NOWARNINGS yes

# Common
RUN apt-get update && apt-get install -y \
  apt-transport-https \
  libasound2-dev \
  bash-completion \
  build-essential \
  bzip2 \
  cmake \
  curl \
  gcc \
  g++ \
  git \
  less \
  libatlas-base-dev \
  libgl1-mesa-dev \
  locales \
  locales-all \
  make \
  man \
  manpages-dev \
  mosquitto-clients \
  net-tools \
  openssh-server \
  openssh-client \
  p7zip \
  postgresql-client \
  software-properties-common \
  sudo \
  unzip \
  vim \
  wget \
  xorg-dev \
  zlib1g-dev \
  zsh
#  vim-gnome \

RUN groupadd -g 1000 $GROUP
RUN useradd -g $GROUP -G sudo -m -s /bin/bash $USER

RUN mkdir /var/run/sshd
RUN echo "${USER}:${PASS}" | chpasswd
RUN echo "root:${PASS}" | chpasswd

# SSH settings. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN sed -e 's@#Port 22@Port 22@' -e 's@#AddressFamily any@AddressFamily inet@' -i /etc/ssh/sshd_config

# Note: The latest tornado(6.0.1) caused a problem not to connect to jupyter kernel; tornado==5.1.1 is a W/A.
#RUN pip3 install numpy tensorflow opencv-python Pillow scipy matplotlib pandas keras jupyter tornado==5.1.1

# Locale
ARG LANGVAL=en_US.utf8
RUN echo "export LANG=$LANGVAL" >> /etc/profile
RUN echo "export LANGUAGE=$LANGVAL" >> /etc/profile
RUN echo "export LC_CTYPE=$LANGVAL" >> /etc/profile
RUN echo "export LC_ALL=$LANGVAL" >> /etc/profile
ENV LANG     $LANGVAL
ENV LANGUAGE $LANGVAL
ENV LC_CTYPE $LANGVAL
ENV LC_ALL   $LANGVAL
RUN echo "$LANGVAL UTF-8" > /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=$LANGVAL

RUN cp /usr/share/zoneinfo/Japan /etc/localtime

# obniz
RUN pip install obniz

# paho-mqtt
RUN pip3 install paho-mqtt

#### User ####
USER $USER
WORKDIR /home/$USER

# Settings
RUN echo 'alias ls="ls -a --color=auto --show-control-chars --time-style=long-iso -FH"' >> /home/$USER/.profile
RUN echo 'alias ll="ls -a -lA"' >> /home/$USER/.profile
RUN echo 'alias h=history' >> /home/$USER/.profile
RUN echo 'alias vi=vim' >> /home/$USER/.profile

RUN echo 'PS1="\$ "' >> /home/$USER/.bashrc
#RUN echo 'set background=dark' > /home/$USER/.vimrc
#RUN echo 'syntax on' >> /home/$USER/.vimrc
RUN touch /home/$USER/.Xauthority && chmod 600 /home/$USER/.Xauthority

USER root

#ADD .netrc /home/$USER
#ADD .gitconfig /home/$USER
#RUN mkdir -p /home/$USER/.vim/colors
#ADD hybrid.vim /home/$USER/.vim/colors/hybrid.vim
ADD .vimrc /home/$USER/.vimrc
ADD .gvimrc /home/$USER/.gvimrc
RUN chown -R $USER:$GROUP /home/$USER/.*vim*
RUN chmod -R 644 /home/$USER/.*vim*

EXPOSE 22
EXPOSE 8080
