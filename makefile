ccend=$(shell echo "\033[0m")
cross=$(shell echo "\033[0;31m✗\033[0m")
check=$(shell echo "\033[0;32m✔\033[0m")
warn=$(shell echo "\033[0;33m⚠\033[0m")
line=$(shell printf '%*s\n' "$${1:-$$(tput cols)}" '' | tr ' ' -)
ccdim=$(shell echo "\033[2m")
ccgreen=$(shell echo "\033[32m")

.PHONEY: help
## Display this help message
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)";sed -ne"/^## /{h;s/.*//;:d" -e"H;n;s/^## //;td" -e"s/:.*//;G;s/\\n## /---/;s/\\n/ /g;p;}" ${MAKEFILE_LIST}|LC_ALL='C' sort -f|awk -F --- -v n=$$(tput cols) -v i=19 -v a="$$(tput setaf 6)" -v z="$$(tput sgr0)" '{printf"%s%*s%s ",a,-i,$$1,z;m=split($$2,w," ");l=n-i;for(j=1;j<=m;j++){l-=length(w[j])+1;if(l<= 0){l=n-i-length(w[j])-1;printf"\n%*s ",-i," ";}printf"%s ",w[j];}printf"\n";}'

.PHONY: all
all: help

.PHONY: shell
## "pipenv shell"
shell:
	pipenv shell

.PHONY: dev
## "pipenv sync --dev" Install dev deps
dev:
	pipenv sync
	pipenv sync --dev

.PHONEY: test
## Run pytest
test:
	pipenv run pytest

.PHONEY: run-notest
## Run the app without tests
run:
	pipenv run python main.py

.PHONEY: run
## Run the app 
run: test
	pipenv run python main.py