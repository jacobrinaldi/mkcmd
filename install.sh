#!/usr/bin/env bash
set -e

echo "mkcmd will ask for sudo to install"

sudo mkdir -p /usr/local/bin
sudo curl -fsSL https://githubusercontent.com -o /usr/local/bin/mkcmd
sudo chmod +x /usr/local/bin/mkcmd

echo "run mkcmd in your termnial to make a command for any project"
