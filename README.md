# NSO Restconf - DNS Example

This example shows how you can interact with NSO through Restconf APIs using the `requests` python library.

This example is based on: `$NCS_DIR/examples.ncs/development-guide/basic-automation/showcase_rc.py`

### Setup environment variables

Set environment variables required.

> if you run this example outside of the playground, make sure `$NCS_DIR` points to the NSO directory. Adjust `NCS_RUN_DIR` and `$REPO_DIR` to your environment.

```bash
export NCS_RUN_DIR=~/nso-lab-rundir
export REPO_DIR=~/src/nso-restconf-dns-example
```

The [Makefile](Makefile) checks all the environment variables are set, any env var missing will cause the Makefile to fail.

Source the `ncsrc` file.

```bash
source $NCS_DIR/ncsrc
```

### Install dependencies

```bash
pip install -r $REPO_DIR/requirements.txt
```

### Build the environment

Build the environment.

```bash
make -C $REPO_DIR build
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

### Bonus

To find more restconf examples that come with NSO do:

```bash
find $NCS_DIR/examples.ncs/ -type f -name "showcase_rc.py"
```
