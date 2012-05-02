#!/bin/bash

ScriptDir="/_misc/scripts"
RepoRoot=$(cd ${0%/$(basename $0)}; pwd)
RepoRoot=${RepoRoot%$ScriptDir}

SupportedEnvs=([dev]=1 [prod]=1 [qa]=1)

. "$RepoRoot$ScriptDir/deploy_env"

[ -f $SourcedFile ] && . $SourcedFile

check_npm_deps() {
	deps=(lessc uglifyjs)
	out=''
	for dep in ${deps[*]}; do
		executable=`which $dep 2>&1`
		ret=$?
		[[ $ret -eq 0 && -x $executable ]] || out="$out $dep"
	done
    [[ $out ]] && {
		echo "[WARN] executables not found:$out"
		echo -n "well, anyway, these are not required for development. continue? [Y/n]: "
		read ANS
		case $ANS in
			[Nn])
				exit 1
				;;
		esac
    }
}

install_bashrc() {
	Skeleton="$RepoRoot/_misc/skeleton/bash_helper_functions.sh"

	egrep -q "^\. $SourcedFile$" "$HOME/.bashrc" || echo -e "\n. $SourcedFile" >> "$HOME/.bashrc"
	egrep -q "^export PIP_DOWNLOAD_CACHE=$PipCacheDir$" "$HOME/.bashrc" || echo -e "export PIP_DOWNLOAD_CACHE=$PipCacheDir\n" >> "$HOME/.bashrc"

	# also add to ".profile" for non-interactive shell
	egrep -q "^\. $SourcedFile$" "$HOME/.profile" || echo -e "\n. $SourcedFile" >> "$HOME/.profile"
	egrep -q "^export PIP_DOWNLOAD_CACHE=$PipCacheDir$" "$HOME/.profile" || echo -e "export PIP_DOWNLOAD_CACHE=$PipCacheDir\n" >> "$HOME/.profile"

	[[ -d $VirtualEnvs ]] || mkdir $VirtualEnvs
	touch $ListFile

	cat "$Skeleton" > $SourcedFile
	sed -i -e "s#LIST_FILE#$ListFile#" "$SourcedFile"
}

mkvirtualenv() {
	VirtualEnvPath="$VirtualEnvs/$VirtualEnvName"
	echo -n "virtualenv for \"$VirtualEnvName\" is not found. use an existing one? [y/N]: "
	read ANS
	case $ANS in
		[Yy])
			echo -n "Location? [$VirtualEnvPath]: "
			read ANS
            test -z $ANS && ANS=$VirtualEnvPath
			test -r "$ANS/bin/activate" || {
				echo "\"$ANS\" is not a valid virtualenv path, aborting."
				exit 1
			}
			VirtualEnvPath="$ANS" 
			;;
        *)
            test -r "$VirtualEnvPatn/bin/activate" && {
                echo "existing virtualenv found at $VirtualEnvPath, overwrite it with a new one from scratch? [y/N]: "
                read ANS
                case $ANS in
                    [Yy])
                        echo "create new virtualenv for \"$VirtualEnvName\" in \"$VirtualEnvPath\" .. "
                        virtualenv --no-site-packages --clear "$VirtualEnvPath" || exit 1
                        ;;
                    *)
                        ;;
                esac
            } || {
                echo "create new virtualenv for \"$VirtualEnvName\" in \"$VirtualEnvPath\" .. "
                virtualenv --no-site-packages --clear "$VirtualEnvPath" || exit 1
            }
            ;;
	esac

	sed -i -e "/^$VirtualEnvName\\b/ c $VirtualEnvName $RepoRoot $VirtualEnvPath" $ListFile
	egrep -q -w "^$VirtualEnvName " $ListFile || echo "$VirtualEnvName $RepoRoot $VirtualEnvPath" >> $ListFile
}

patch_django_pipeline() {
	shopt -s extglob
    local dir="$VIRTUAL_ENV/lib/python2.7/site-packages"
    local files="$RepoRoot/_misc/patches/django-pipeline/*.patch"
    cat $files | patch -d $dir -p1 -r- -N
}

patch_pusher() {
	shopt -s extglob
    local dir="$VIRTUAL_ENV/lib/python2.7/site-packages"
    local files="$RepoRoot/_misc/patches/pusher/*.patch"
    cat $files | patch -d $dir -p1 -r- -N
}

set_deploy_env() {
	DeployEnv=${1:-dev}
	VirtualEnvName="$(basename $RepoRoot)_$DeployEnv"

	if [[ ! ${SupportedEnvs[$DeployEnv]} ]]; then
		echo "\"$1\" is not a supported env."
		exit 1
	fi

	echo "## use set_deploy_env to modify this file" > $DjangoConfig
	echo "## should be readable from both python and bash" >> $DjangoConfig
	echo "DeployEnv='$DeployEnv'" >> $DjangoConfig
	echo "VirtualEnvName='$VirtualEnvName'" >> $DjangoConfig

	echo "remote \"DeployEnv\" set to \"$DeployEnv\""
}

[ -z "$1" ] && { echo 'noop'; exit 3; }
operation=$1
shift
case $operation in
	apply_patches)
		workon $VirtualEnvName || { echo 'cant ve'; exit 3; }
		patch_django_pipeline
		patch_pusher
		;;
	check_npm_deps)
		check_npm_deps
		;;
	install_bashrc)
		install_bashrc
		;;
	install_pip_deps)
		workon $VirtualEnvName || { echo 'cant ve'; exit 3; }
		pip install -r $RepoRoot/_misc/requirements/$DeployEnv.txt --download-cache=$PipCacheDir
		exit $?
		;;
	mkvirtualenv)
		workon "$VirtualEnvName" && exit
		mkvirtualenv
		;;
	run_once)
		## opposite to it's name, the run_once task runs everytime.
		mkdir -p $DjangoLogDir
		mkdir -p "$RepoRoot/static/media"
		mkdir -p ~/.node_libraries/
		[ -f /usr/lib/nodejs/uglify-js/uglify-js.js ] && ln -sf /usr/lib/nodejs/uglify-js/uglify-js.js ~/.node_libraries/
		[ -f /usr/local/lib/node_modules/uglify-js/uglify-js.js ] && ln -sf /usr/local/lib/node_modules/uglify-js/uglify-js.js ~/.node_libraries/
		;;
	set_deploy_env)
		set_deploy_env $*
		;;
	workon_name)
		echo $VirtualEnvName
		;;
	*)
		echo "unsupported operation: $operation"
		exit 3
		;;
esac

:

