# Copyright (c) 1991-2016 Kawahara Lab., Kyoto University
# Copyright (c) 2000-2005 Shikano Lab., Nara Institute of Science and Technology
# Copyright (c) 2005-2016 Julius project team, Nagoya Institute of Technology
# All rights reserved

SHELL=/bin/sh
RM=/bin/rm -f
prefix=/usr/local
exec_prefix=${prefix}
INSTALL=/usr/bin/install -c

TARGET=jclient.pl

all:
	chmod +x $(TARGET)

install: install.bin

install.bin:
	${INSTALL} -d ${exec_prefix}/bin
	${INSTALL} $(TARGET) ${exec_prefix}/bin

clean:
	echo nothing to do

distclean:
	chmod -x $(TARGET)
	$(RM) Makefile
