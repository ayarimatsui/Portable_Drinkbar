# Copyright (c) 1991-2016 Kawahara Lab., Kyoto University
# Copyright (c) 2001-2005 Shikano Lab., Nara Institute of Science and Technology
# Copyright (c) 2005-2016 Julius project team, Nagoya Institute of Technology
# All rights reserved 
#
SHELL=/bin/sh
.SUFFIXES:
.SUFFIXES: .c .o
.c.o:
	$(CC) $(CFLAGS) $(CPPFLAGS) -o $@ -c $<
guiobj/%.o: %.c
	$(CC) $(CFLAGS) $(CPPFLAGS) $(SDL_CFLAGS) -o $@ -c $<

LIBSENT=../libsent
LIBJULIUS=../libjulius
CC=gcc
CFLAGS=-g -O2
CPPFLAGS=-I. -I$(LIBJULIUS)/include -I$(LIBSENT)/include  `$(LIBSENT)/libsent-config --cflags` `$(LIBJULIUS)/libjulius-config --cflags`
LDFLAGS= -L$(LIBJULIUS) `$(LIBJULIUS)/libjulius-config --libs` -L$(LIBSENT) `$(LIBSENT)/libsent-config --libs`
RM=/bin/rm -f
prefix=/usr/local
exec_prefix=${prefix}
INSTALL=/usr/bin/install -c

SDL_CFLAGS= -DUSE_SDL
SDL_LDFLAGS=

OBJ=adintool.o options.o mainloop.o
GUIOBJ=guiobj/adintool.o guiobj/options.o guiobj/mainloop.o

EXTRA_TARGET=
ifdef EXTRA_TARGET
GUITARGET=
endif

TARGET=adintool $(GUITARGET)

all: $(TARGET)

adintool: $(OBJ) $(LIBSENT)/libsent.a $(LIBJULIUS)/libjulius.a
	$(CC) $(CFLAGS) $(CPPFLAGS) -o $@ $(OBJ) $(LDFLAGS)

adintool-gui: $(GUIOBJ) $(LIBSENT)/libsent.a $(LIBJULIUS)/libjulius.a
	$(CC) $(CFLAGS) $(CPPFLAGS) $(SDL_CFLAGS) -o $@ $(GUIOBJ) $(LDFLAGS) $(SDL_LDFLAGS)

install: install.bin

install.bin: $(TARGET)
	${INSTALL} -d ${exec_prefix}/bin
	${INSTALL} $(TARGET) ${exec_prefix}/bin

clean:
	$(RM) $(OBJ) $(GUIOBJ)
	$(RM) config.log config.cache
	$(RM) *~ core
	$(RM) adintool adintool adintool-gui adintool-gui

distclean:
	$(RM) $(OBJ) $(GUIOBJ)
	$(RM) config.log config.cache
	$(RM) *~ core
	$(RM) adintool adintool adintool-gui adintool-gui
	$(RM) config.status
	$(RM) Makefile
