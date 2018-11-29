
usedb () {
    export MYMYSQLDB=$@
}
showtable() {
        if [ $# -ne 1 ]; then
                mysql -e "use $MYMYSQLDB; show tables;"
                echo "To show one table, use:"
                echo "  ${FUNCNAME[0]} <table>"
        else
            mysql -e "use $MYMYSQLDB; describe $@;"
        fi
}

listtable() {
        if [ $# -ne 1 ]; then
                mysql -e "use $MYMYSQLDB; show tables;"
                echo "To dump one table, use:"
                echo "  ${FUNCNAME[0]} <table>"
        else
                mysql -e "use $MYMYSQLDB; select * from $@;"
        fi
}

counttable () {
    if [ $# -ne 1 ]; then
        echo "Usage:    ${FUNCNAME[0]} <table>"
        echo "To see table list: listtables"
    else
        mysql -e "use $MYMYSQLDB; SELECT COUNT(*) FROM $@";
    fi
}
counttable_silent () {
    mysql -s -N -e "use $MYMYSQLDB; SELECT COUNT(*) FROM $@";
}
count_online_device () {
    mysql -e "use $MYMYSQLDB; select count(mac), \
                              sum(if(connected = 1, 1, 0)) as 'connected(1)', \
                              sum(if(connected = 0, 1, 0)) as 'connected(0)', \
                              sum(if(connected = -1, 1, 0)) as 'connected(-1)' \
                              from device_info"
}
count_online_client () {
    mysql -e "use $MYMYSQLDB; select count(client_mac), \
                              sum(if(online = 1, 1, 0)) as 'online', \
                              sum(if(online = 0, 1, 0)) as 'offline' \
                              from client_session"
}


##
# friendly for human reading
#
alias listtables='mysql -e "use $MYMYSQLDB; show tables;"'
alias describe_table='showtable'
alias dump_table='listtable'
alias count_table='counttable'

##
# friendly for scripting
#
alias listtables_silent='mysql -s -N -e "use $MYMYSQLDB; show tables;"'
alias count_table_silent='counttable_silent'


##
# handy script use function above
#
alias count_all_table='for i in $(listtables_silent); do cnt=$(count_table_silent $i); echo "$i $cnt";done'
