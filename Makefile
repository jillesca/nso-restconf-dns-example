all:
    mkdir ${WORKING_DIR}
    ncs-setup --dest ${WORKING_DIR}
    cp pkg/Makefile ${WORKING_DIR}/Makefile
    cp pkg/ncs_init.xml ${WORKING_DIR}/ncs-cdb/ncs_init.xml
    # cp -r init/router.in nso-lab-rundir/packages/router

clean:
    # echo ${WORKING_DIR}
    -rm -rf ${WORKING_DIR}

stop:
    -ncs-netsim --dir ${WORKING_DIR}/netsim -a stop
    -ncs --stop
