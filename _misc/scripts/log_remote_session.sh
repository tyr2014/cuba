#!/bin/bash
LogDir=/usr/local/lib/remote-session
LogFile="$LogDir/$(id -u)/access.log"
LogDir="$LogDir/$(id -u)/$(date +%Y%m%d)"
LogDate="$(date +%H%M%S.%N)"
ScriptFile="$LogDir/$LogDate.script"
TimingFile="$LogDir/$LogDate.timing"

SFTP=/usr/lib/openssh/sftp-server

mkdir -p "$LogDir"

echo -e "\n### $(date) --- $SSH_CLIENT ###\n" >> "$LogFile"

CMD=${SSH_ORIGINAL_COMMAND:-}

echo "executing $CMD" >> "$LogFile"

if [[ "$CMD" == "internal-sftp" ]]; then
	exec $SFTP
elif [[ "$CMD" == sftp* || "$CMD" == scp* || "$CMD" == rsync* ]]; then
	exec $CMD
elif [ -n "$CMD" ]; then
	exec script -c "$SSH_ORIGINAL_COMMAND" -e -f -q -t"$TimingFile" "$ScriptFile"
        #exec $CMD
else
	echo "interactive session: $(date +%Y%m%d)/$LogDate" >> "$LogFile"
	exec script -c "bash -l" -e -f -q -t"$TimingFile" "$ScriptFile"
fi

:

