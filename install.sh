
#!/usr/bin/env bash
set -e

echo "Mkcmd will ask for sudo to install"

sudo mkdir -p /usr/local/bin

sudo curl -fsSL \
  https://raw.githubusercontent.com/jacobrinaldi/mkcmd/main/main.py \
  -o /usr/local/bin/mkcmd

sudo chmod +x /usr/local/bin/mkcmd

echo "mkcmd installed successfully!"
echo "Run 'mkcmd' to get started."
