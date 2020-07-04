# MKFILE_PATH has a trailing slash
MKFILE_PATH := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
STATIC_PATH = $(MKFILE_PATH)../static/brimo

MAIN_CSS = $(STATIC_PATH)/style.css

.PHONY: all clean

all: $(MAIN_CSS)

clean:
	rm -rf $(MAIN_CSS)

$(MAIN_CSS): style.scss
	sass $< $@
