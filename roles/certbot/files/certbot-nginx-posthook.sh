#!/bin/bash
# Post-hook for certbot that deletes iptable rule that contains COMMENT

COMMENT="certbot hook"

RULES=$(iptables --line-number -nL INPUT | grep "$COMMENT" | awk '{print $1}' | tac)

for rule in $RULES; do
    /sbin/iptables -D INPUT $rule;
    sleep 0.1;
done
