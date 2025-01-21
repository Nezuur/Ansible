#!/bin/bash
# Pre-hook for certbot checks for existing rules and add RULE if it's not found

RULES=(
    "-p tcp --dport 80 -j ACCEPT"
    )

for rule in "${RULES[@]}"; do

    if iptables -C INPUT $RULE 2>/dev/null; then
        # Rule exists, do nothing
        :
    else
        iptables -A INPUT $RULE -m comment --comment "certbot hook"
        # Add rule if it doesn't exist
    fi
done
