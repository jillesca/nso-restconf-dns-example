# nso-restconf-dns-example

Simple DNS example showign how to interact with NSO using Restconf APIs.

<!-- export NCS_DIR=~/nso/nso-6.1.2.1 -->

source $NCS_DIR/ncsrc

export NCS_RUN_DIR=~/nso/nso-lab-rundir
export REPO_DIR=~/nso/nso-restconf-dns-example

make clean all

<!-- ncs_cmd -dd -c 'maction "/packages/reload"' -->

<!-- export NCS_RUN_DIR=~/nso-lab-rundir -->
<!-- export REPO_DIR=~/src/nso-restconf-dns-example -->
