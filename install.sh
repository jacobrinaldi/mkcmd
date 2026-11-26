
#!/usr/bin/env bash
set -e

echo "Installing mkcmd..."

curl -fsSL \
  https://raw.githubusercontent.com/jacobrinaldi/mkcmd/main/main.py \
  -o /tmp/mkcmd

sudo install -m 755 /tmp/mkcmd /usr/local/bin/mkcmd

rm /tmp/mkcmd

echo "mkcmd installed successfully!"
echo "Run 'mkcmd' to get started."
