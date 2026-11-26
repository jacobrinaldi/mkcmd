
# mkcmd

**Turn your scripts into commands you can run from anywhere.**

`mkcmd` lets you create terminal commands from your own scripts, making it easier to run your projects without remembering long file paths.

## Features

- Turn scripts into terminal commands.
- Run commands from anywhere in your terminal.
- Simple installation.
- Support for multiple scripting languages (where implemented).

## Installation

### Linux

#### Option 1: Install using the installation script (recommended)

Clone the repository:

```bash
git clone https://github.com/jacobrinaldi/mkcmd.git
cd mkcmd
```

Make the installer executable:

```bash
chmod +x install.sh
```

Run the installer:

```bash
./install.sh
```

The installer downloads the latest `main.py` and installs it into `/usr/local/bin/mkcmd`.

You will be asked for your sudo password during installation.

#### Option 2: Manual installation

If the installation script doesn't work, install manually:

```bash
curl -fL https://raw.githubusercontent.com/jacobrinaldi/mkcmd/main/main.py -o /tmp/mkcmd
sudo install -m 755 /tmp/mkcmd /usr/local/bin/mkcmd
rm /tmp/mkcmd
```

## Verify Installation

Check that mkcmd is installed:

```bash
which mkcmd
```

Start mkcmd:

```bash
mkcmd
```

## Usage

Run:

```bash
mkcmd
```

Follow the interactive prompts to create a command from your script.

## Troubleshooting

### `curl: command not found`

Install curl:

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install curl
```

**Fedora:**

```bash
sudo dnf install curl
```

**Arch Linux:**

```bash
sudo pacman -S curl
```

### `Permission denied`

Make sure you run the installer with:

```bash
chmod +x install.sh
./install.sh
```

### `mkcmd: command not found`

Check whether `/usr/local/bin` is in your PATH:

```bash
echo "$PATH"
```

If necessary, add it to your PATH:

```bash
export PATH="/usr/local/bin:$PATH"
```

### GitHub download errors

Test the download:

```bash
curl -fL https://raw.githubusercontent.com/jacobrinaldi/mkcmd/main/main.py -o /tmp/mkcmd-test
```

If this fails, check your internet connection and GitHub access.

## Requirements

- Linux
- Python 3
- curl (for installation)
- sudo privileges (for system-wide installation)

## Contributing

Contributions, bug reports, and suggestions are welcome!

Feel free to open an issue or submit a pull request.

## License

See the repository for license information.

