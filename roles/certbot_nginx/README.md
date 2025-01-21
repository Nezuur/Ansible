# Ansible Role: Certbot with Nginx

## Description

This Ansible role automates the deployment and renewal of Let's Encrypt SSL certificates for Nginx on Linux servers using Certbot, and is configured to run within a Python virtual environment. Key features of this role include:

## Features

- **Python and Virtual Environment**: Installs a specific Python version and sets up a virtual environment to operate Certbot.
- **Certbot Installation**: Deploys Certbot and the Certbot-Nginx plugin via pip within the virtual environment.
- **Iptables Configuration**: Manages iptables rules to ensure HTTP and HTTPS traffic is allowed, crucial for ACME challenges during certificate issuance.
- **Certificate Checks and Installation**: Automatically checks for existing SSL certificates and installs them if not present.
- **Automatic Certificate Renewal**: Configures cron jobs to handle certificate renewal automatically. This step is unnessecary as certbot has a built-in renewal feature, but is included for convenience.
- **Webhook Scripts for Iptables Management**: Includes `pre-hook` and `post-hook` bash scripts to manage iptables rules during the certificate renewal process:
  - *Pre-hook Script*: Checks for necessary iptables rules (e.g., allowing traffic on port 80) and adds them if they are missing, ensuring that the HTTP challenge can be completed.
  - *Post-hook Script*: Cleans up iptables by removing any rules added by the pre-hook that are specifically tagged to indicate they were for Certbot's use, ensuring no unnecessary open ports remain.

## Requirements

Designed to work on systems supporting the Apt package manager, this role uses the `deadsnakes` repository for Python installations and is highly customizable through the defined defaults in the `main.yml` file under the `defaults` directory.
