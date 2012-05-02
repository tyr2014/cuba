## this file should be filtered through "fabric_tasks.sh install_bashrc"
## which replace LIST_FILE with the real path to the list file

## return if not sourced by bash
[ -z $BASH_VERSION ] && return

## workon and ve helper function for fast virtualenv and working directory switching
_workon() {
	local cur
	COMPREPLY=()
	cur=${COMP_WORDS[COMP_CWORD]}

	if [ $COMP_CWORD -eq 1 ] ; then
		COMPREPLY=( $( compgen -W "$( command cat LIST_FILE | awk '{print $1}' )" -- $cur ) )
	fi
}

workon() {
	test -z $1 && return 2
	local dir env
	dir=$( egrep "^$1 " LIST_FILE | awk '{print $2}' )
	env=$( egrep "^$1 " LIST_FILE | awk '{print $3}' )
    test -r "$env/bin/activate" || return 2
    test -d "$dir" || return 2
	source "$env/bin/activate"
	cd $dir
}

## ve() is an alias to workon()
ve() {
	workon $*
}

complete -F _workon workon
complete -F _workon ve


## bash_completion for manage.py and django-admin.py
_django_completion()
{
    COMPREPLY=( $( COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
	               DJANGO_AUTO_COMPLETE=1 $1 ) )
}
complete -F _django_completion -o default django-admin.py manage.py django-admin

_python_django_completion()
{
    if [[ ${COMP_CWORD} -ge 2 ]]; then
        PYTHON_EXE=$( basename -- ${COMP_WORDS[0]} )
        echo $PYTHON_EXE | egrep "python([2-9]\.[0-9])?" >/dev/null 2>&1
        if [[ $? == 0 ]]; then
            PYTHON_SCRIPT=$( basename -- ${COMP_WORDS[1]} )
            echo $PYTHON_SCRIPT | egrep "manage\.py|django-admin(\.py)?" >/dev/null 2>&1
            if [[ $? == 0 ]]; then
                COMPREPLY=( $( COMP_WORDS="${COMP_WORDS[*]:1}" \
                               COMP_CWORD=$(( COMP_CWORD-1 )) \
                               DJANGO_AUTO_COMPLETE=1 ${COMP_WORDS[*]} ) )
            fi
        fi
    fi
}

# Support for multiple interpreters.
unset pythons
if command -v whereis &>/dev/null; then
    python_interpreters=$(whereis python | cut -d " " -f 2-)
    for python in $python_interpreters; do
        pythons="${pythons} $(basename -- $python)"
    done
    pythons=$(echo $pythons | tr " " "\n" | sort -u | tr "\n" " ")
else
    pythons=python
fi

complete -F _python_django_completion -o default $pythons


## helper function to output a daily summary of recent commits in a git repository
git_daily_sum() {
	NEXT=$(date +%F)
	expr match "$1" '^[0-9]\+$' > /dev/null && len="$1" || len="7"
	echo "CHANGELOG"
	echo ----------------------
	git log --all --no-merges --format="%cd" --date=short | sort -u -r | head -n $len | while read DATE ; do
		[ $DATE == $NEXT ] && continue
		echo
		echo "[$DATE] - [$NEXT]"
		GIT_PAGER=cat git log --all --no-merges --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --since=$DATE --until=$NEXT
		NEXT=$DATE
		echo
	done
}

