#!/bin/sh

### BEGIN INIT INFO
# Provides:          supervisord
# Required-Start:    $network $local_fs $remote_fs $syslog
# Required-Stop:     $network $local_fs $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: start supervisord in configured virtualenvs
# Description:       This script is installed by tukeq's
#                    deploy_run_once.sh. It reads configurations in
#                    /etc/default/supervisord and start supervisord
#                    for $DaemonUser.
### END INIT INFO

. /lib/lsb/init-functions

test $DEBIAN_SCRIPT_DEBUG && set -v -x

## these arg can be override by /etc/default/supervisor
GRACEKILL=15
GRACETERM=30
#GRACERESTART=5

test -e /etc/default/supervisor && . /etc/default/supervisor

DESC=supervisor
NAME=supervisord
DAEMON=/usr/bin/$NAME
PIDFILE=/var/run/$NAME.pid

if [ ! -x "$DAEMON" ] ; then
	echo "$DESC: command not found: $DAEMON"
	exit 0
fi

#
# Function that starts the daemon/service
#
do_start()
{
	# Return
	#   0 if daemon has been started
	#   1 if daemon was already running
	#   2 if daemon could not be started
	pidofproc "$DAEMON" > /dev/null && return 1
	start-stop-daemon --start --quiet --pidfile $PIDFILE --exec $DAEMON --test > /dev/null || return 1
	start-stop-daemon --start --quiet --pidfile $PIDFILE --exec $DAEMON -- $DAEMON_ARGS || return 2
	# Add code here, if necessary, that waits for the process to be ready
	# to handle requests from services started subsequently which depend
	# on this one.  As a last resort, sleep for some time.
}

#
# Function that stops the daemon/service
#
do_stop()
{
	# Return
	#   0 if daemon has been stopped
	#   1 if daemon was already stopped
	#   2 if daemon could not be stopped
	#   other if a failure occurred
	start-stop-daemon --stop --quiet --retry=TERM/$GRACETERM/KILL/$GRACEKILL --pidfile $PIDFILE --name $NAME
	RETVAL="$?"
	[ "$RETVAL" = 2 ] && return 2
	# Wait for children to finish too if this is a daemon that forks
	# and if the daemon is only ever run from this initscript.
	# If the above conditions are not satisfied then add some other code
	# that waits for the process to drop all resources that could be
	# needed by services started subsequently.  A last resort is to
	# sleep for some time.
	start-stop-daemon --stop --quiet --oknodo --retry=0/$GRACETERM/KILL/$GRACEKILL --exec $DAEMON
	[ "$?" = 2 ] && return 2
	# Many daemons don't delete their pidfiles when they exit.
	rm -f $PIDFILE
	return "$RETVAL"
}

case "$1" in
	start)
		[ "$VERBOSE" != no ] && log_daemon_msg "Starting $DESC" "$NAME"
		do_start
		case "$?" in
		0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
		2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
		esac
		;;
	stop)
		[ "$VERBOSE" != no ] && log_daemon_msg "Stopping $DESC" "$NAME"
		do_stop
		case "$?" in
		0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
		2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
		esac
		;;
	status)
		status_of_proc "$DAEMON" "$NAME" && exit 0 || exit $?
		;;
## TODO supervisor's native reload seems buggy. will check later.
#	reload)
#		;;
	restart)
		log_daemon_msg "Restarting $DESC" "$NAME"
		do_stop
		[ -n "$GRACERESTART" ] && sleep $GRACERESTART
		case "$?" in
			0|1)
				do_start
				case "$?" in
					0) log_end_msg 0 ;;
					1) log_end_msg 1 ;; # Old process is still running
					*) log_end_msg 1 ;; # Failed to start
				esac
				;;
			*) log_end_msg 1 ;;
		esac
		;;
	*)
		echo "Usage: /etc/init.d/$DESC {start|stop|status|restart}" >&2
		exit 3
		;;
esac

:

