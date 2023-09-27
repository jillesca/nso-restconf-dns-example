build:
	$(MAKE) check-repo-env
	$(MAKE) check-ncs-run-env
	$(MAKE) check-ncs-env
	mkdir ${NCS_RUN_DIR}
	$(MAKE) netsim
	$(MAKE) setup
	$(MAKE) start

netsim:
	ncs-netsim --dir ${NCS_RUN_DIR}/netsim create-network ${NCS_DIR}/packages/neds/cisco-ios-cli-3.8 3 ex

setup:
	ncs-setup --dest ${NCS_RUN_DIR} --netsim-dir ${NCS_RUN_DIR}/netsim
	ncs-make-package --service-skeleton python dns-config --dest ${NCS_RUN_DIR}/packages/dns-config
	cp ${REPO_DIR}/dns-config.yang ${NCS_RUN_DIR}/packages/dns-config/src/yang/
	$(MAKE) -C ${NCS_RUN_DIR}/packages/dns-config/src all 

start:
	ncs-netsim -a start --dir ${NCS_RUN_DIR}/netsim
	cd ${NCS_RUN_DIR} && ncs --with-package-reload && cd -

clean:
	$(MAKE) stop
	-rm -rf ${NCS_RUN_DIR}

stop:
	$(MAKE) check-repo-env
	$(MAKE) check-ncs-run-env
	$(MAKE) check-ncs-env
	-ncs-netsim --dir ${NCS_RUN_DIR}/netsim -a stop
	-ncs --stop

check-repo-env:
ifndef REPO_DIR
	$(Error environment variable REPO_DIR is undefined. Source it. See example in README)
endif

check-ncs-run-env:
ifndef NCS_RUN_DIR
	$(Error environment variable NCS_RUN_DIR is undefined. Source it. See example in README)
endif

check-ncs-env:
ifndef NCS_DIR
	$(Error environment variable NCS_DIR is undefined. Source it. See example in README)
endif