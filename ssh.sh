#!/bin/sh 
ssh $@

echo "Dumping SSH actions:" > ssh.log
echo $@ >> ssh.log
echo $1 >> ssh.log
echo $2 >> ssh.log