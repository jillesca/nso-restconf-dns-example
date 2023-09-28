# nso-restconf-dns-example

Simple DNS example showing how to interact with NSO using Restconf APIs.

### Setup the example

Set environment variables required

```bash
export NCS_RUN_DIR=~/nso-lab-rundir
export REPO_DIR=~/src/nso-restconf-dns-example
```

Source `ncsrc`

```bash
source $NCS_DIR/ncsrc
```

Build the environment

```bash
make build
```

Install python dependencies

```bash
pip install -r $REPO_DIR/requirements.txt
```

### Run the example

```bash
python main.py
```

### Remove the example

```bash
make clean
```

<!-- ncs_cmd -dd -c 'maction "/packages/reload"' -->
