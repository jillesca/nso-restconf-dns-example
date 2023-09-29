# NSO Restconf - DNS Example

This example shows how you can interact with NSO through Restconf APIs using the `requests` python library.

### What the script does

The script updates the DNS server configuration of a netsim device using the yang model and template created for this example. The outputs of the calls are printed to the terminal.

It performs the following steps:

- Creates an HTTP session to NSO.
- Lists the devices present in NSO.
- Syncs NSO with the netsim devices using `sync-from`.
- Adds the DNS server `1.1.1.1` to `ex1`.
- Dry-runs adding a DNS server `2.2.2.2` to `ex1`.
- Adds the DNS server `2.2.2.2` to `ex1`.
- Lists the rollback files present in NSO.
- Applies the latest rollback file (0).
- Dry-runs adding a DNS serve `3.3.3.3` to `ex1`.
- Adds the DNS server `3.3.3.3` to `ex1`.

During the execution the script will print the results to the terminal, and displays the existing DNS configuration.

You can edit the [main.py](main.py) on the playground to experiment with `ex0` or `ex2` or change the flow of the steps.

Take a look at [script_outpiut.log](script_output.log) to see what the script prints.

### How the example is built

This example uses NSO in local install mode, along with three `netsim` devices (but only ex1 is used) that work with the IOS example NED.

NSO and netsim are configured automatically using a [Makefile](Makefile).

A simple dns-config template is created to experiment with this example. This template is created, configured and compiled automatically by the same [Makefile](Makefile). You can find the template detais under the [dns-config directory](dns-config/)

The only thing you need to do are the steps described below, and then play with the python script.

This example is based on: `$NCS_DIR/examples.ncs/development-guide/basic-automation/showcase_rc.py`

### Setup environment variables

> if you run this example outside of the playground, make sure `$NCS_DIR` points to the NSO directory. Adjust `NCS_RUN_DIR` and `$REPO_DIR` to your environment.

The [Makefile](Makefile) checks all the environment variables are set, any env var missing will cause the Makefile to fail.

```bash
export NCS_RUN_DIR=~/nso-lab-rundir
export REPO_DIR=~/src/nso-restconf-dns-example
```

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
