#!/bin/bash

BackupDirBase=/home/tukeq/cifs/dbdump
RemotePath="rack0.tukeq.com:/var/lib/mongodb/dbdump/dump_latest/"
LocalPath="$BackupDirBase/dump_latest/"
LogFile="$BackupDirBase/rsync.log"
LockFile="$BackupDirBase/rsync.lock"
WeeklyArchive="$BackupDirBase/archive.weekly"
DailyArchive="$BackupDirBase/archive.daily"

(
	[ -f "$LockFile" ] && exit
	touch "$LockFile"
	echo -e "\n### $(date) ###" >> "$LogFile"
	rsync -rvch "$RemotePath" "$LocalPath" >> "$LogFile" 2>&1
	rm "$LockFile"
	RotateDir="$BackupDirBase/dump_$(date +%m%d)"
	Compress="$RotateDir/$(date +%H).7z"
	mkdir -p "$RotateDir"
	7z u "$Compress" "$LocalPath"
) &

case $1 in
	rotate)
		## hourly backups are kept for 1 week
		## daily backups are kept for 4 weeks
		## weekly archives are kept forever

		ArchiveSourceDir="$BackupDirBase/dump_$(date +%m%d -d '1 week ago')"
		ArchiveSource="$ArchiveSourceDir/04.7z"
		if [ $(date +%w) -eq 0 ]; then
			ArchiveDest="$WeeklyArchive/$(date +%Y%m%d -d '1 week ago').7z"
		else
			ArchiveDest="$DailyArchive/$(date +%m%d -d '1 week ago').7z"
		fi
		[ -f "$ArchiveSource" ] && [ ! -f "$ArchiveDest" ] && mv "$ArchiveSource" "$ArchiveDest"
		[ -d "$ArchiveSourceDir" ] && rm -r "$ArchiveSourceDir"

		Obsolete="$DailyArchive/$(date +%m%d -d '4 weeks ago').7z"
		[ -f "$Obsolete" ] && rm "$Obsolete"
		;;
esac

:

