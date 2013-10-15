#!/bin/sh
##
# NAME: genkeys.sh - generate multi private and public key files
# AUTHOR: alphwe 
# SYNOPSIS: genkeys OPTION
##

members=('alphwe' 'ph87')
while getopts "ra:g" arg
do
  case $arg in
    a)
      echo generate $OPTARG private and public key
      ssh-keygen -qf $OPTARG -N '' -C $OPTARG
      ;;
    r)
      for member in ${members[@]};
      do
        rm -f $member $member.pub
      done
      ;;
    g)
      for member in ${members[@]}; do
        echo generate $member private and public key
        ssh-keygen -qf $member -N '' -C $member
      done
      ;;
    ?)
      echo "未知命令"
      exit 1
      ;;
    esac
done
