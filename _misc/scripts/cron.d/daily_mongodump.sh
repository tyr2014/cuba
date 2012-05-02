#!/bin/bash

BackupDirBase=/var/lib/mongodb/dbdump
ArchiveDir="$BackupDirBase/archive"
LogFile="$BackupDirBase/dump.log"
Database="toureet"

[ $(date +%H) -eq 04 ] && DirName="midnight" || DirName="$(date +%H)"
BackupDir="$BackupDirBase/dump_$(date +%m%d)/$DirName"

echo -e "\n### $(date) ###" >> "$LogFile"
mkdir -p "$BackupDir"
mongodump --db "$Database" --out "$BackupDir" >> "$LogFile" 2>&1
ln -sf -T "$BackupDir" "$BackupDirBase/dump_latest"

case $1 in
	rotate)
		## bi-monthly archive
		Archive="$ArchiveDir/$(date +%Y%m%d).7z"
		[[ $(date +%d) -eq 1 || $(date +%d) -eq 16 ]] && [ ! -f "$Archive" ] && 7z a "$Archive" "$BackupDir" >> "$LogFile"

		## prune
		ExpiringDir="$BackupDirBase/dump_$(date +%m%d -d '3 days ago')"
		[ -d "$ExpiringDir" ] && find "$ExpiringDir" -name "??" -exec rm -r {} \;
		ExpiringDir="$BackupDirBase/dump_$(date +%m%d -d '2 weeks ago')"
		[ -d "$ExpiringDir" ] && rm -r "$ExpiringDir"
		;;
esac

echo -e "\n### $(date) ###" >> "$LogFile"

:

