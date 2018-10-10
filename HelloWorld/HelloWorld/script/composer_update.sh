#!/bin/bash
#date 20181010

y=$1

function composer_web () {
    ansible-playbook /etc/ansible/tasks/composer_update.yml --extra-vars "hosts=web webdomain=${y}"
}

composer_web