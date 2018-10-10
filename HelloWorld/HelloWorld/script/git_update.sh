#!/bin/bash
#date 20181010

x=$1

function git_web () {
    ansible-playbook /etc/ansible/tasks/git_update.yml --extra-vars "hosts=web webdomain=${x}"
}

git_web