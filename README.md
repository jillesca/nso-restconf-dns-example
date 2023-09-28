# NSO Restconf - DNS Example

Simple DNS example showing how to interact with NSO using Restconf APIs.

### Setup example

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
make -C $REPO_DIR build
```

Install python dependencies

```bash
pip install -r $REPO_DIR/requirements.txt
```

### Run example

```bash
python $REPO_DIR/main.py
```

### Remove example

```bash
make -C $REPO_DIR clean
```

---

### Addendum

#### Test template manually without python

```bash
devices sync-from
config
dns-config ex0 dns-server 1.1.1.1
dns-config ex0 dns-server 2.2.2.2
dns-config ex1 dns-server 1.1.1.1
dns-config ex2 dns-server 5.5.5.5
```

See what NSO will send to the devices

```bash
commit dry-run
commit and-quit
```

Verify config was applied on the devices

```bash
show running-config devices device * config ip name-server
```
