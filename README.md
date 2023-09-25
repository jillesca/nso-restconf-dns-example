# nso-restconf-dns-example

Simple DNS example showing how to interact with NSO using Restconf APIs.

export NCS_RUN_DIR=~/nso-lab-rundir
export REPO_DIR=~/src/nso-restconf-dns-example

source $NCS_DIR/ncsrc

make clean all

pip install -r $REPO_DIR/requirements.txt

<!-- ncs_cmd -dd -c 'maction "/packages/reload"' -->
