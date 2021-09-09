#!/bin/bash
# Gen mirrorlist
# jim945@mail.ru 

workdir=`dirname "$(readlink -e "$0")"`
reflector -a 1 --completion-percent 100 -p rsync -n 5 > $workdir/mirrorlist
