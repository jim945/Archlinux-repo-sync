#!/bin/bash
# Mirroring repositories ArchLinux.
# jim945@mail.ru 

workdir=`dirname "$(readlink -e "$0")"`

DIR="$1" # Куда грузим
REPOS="core extra community" # multilib testing community-testing multilib-testing kde-unstable gnome-unstable
arch="x86_64"
EX_FILE="$workdir"/pac.exclude # Файл исключений
MAX_SIZE="100M"
PARAM="--exclude-from=$EX_FILE --max-size=$MAX_SIZE --partial --progress --safe-links --copy-links --delete --delete-before"
# --delete-after --delay-updates Удалять после загрузки




#LCK_FLE='/var/run/repo-sync.lck'

#if [ -e "$LCK_FLE" ] ; then
	#OTHER_PID=$(cat $LCK_FLE)
	#echo "Another instance already running: $OTHER_PID"
	#exit 1
#fi
#echo $$ > "$LCK_FLE"


i=0
for repo in $REPOS ; do
        echo "Sync $repo"
        
        eval SERVER=($(cat "$workdir"/mirrorlist | grep "Server = " | cut -d " " -f 3)/)
        
        SYNC_DIR="$DIR"/archlinux/$repo/os/$arch/
        if [ ! -e "$SYNC_DIR" ]; then
        mkdir -p "$SYNC_DIR"
        fi
        
        while (( $i < ${#SERVER[@]} )) ; do
		eval rsync -rtlH "$PARAM" "${SERVER[$i]}"/ "$SYNC_DIR" && break
            (( i++ ))
        done
        
done


# Cleanup
#rm -f "$LCK_FLE"

#exit 0
