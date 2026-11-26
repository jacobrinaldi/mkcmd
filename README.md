# MKCMD

Make many langues into commands with ease


## Install

**### Automatic install
curl -fsSL https://raw.githubusercontent.com/jacobrinaldi/mkcmd/main/install.sh | bash


   bash
``curl -fsSL https://raw.githubusercontent.com/jacobrinaldi/mkcmd/main/install.sh | bash
``

### Manual Install
1. Clone the repository:
   ```bash
   git clone https://github.com/jacobrinaldi/mkcmd
   cd mkcmd
   ```
2. Run the included installer script:
   ```bash
   chmod +x install.sh
   ./install.sh

## Usage

1. Add the required shebang line to Line 1 of your script.
2. Run `mkcmd` from anywhere in your terminal:
   ```bash
   mkcmd
   ```
3. Enter the prompted details:
   * **File name** (without the file extension)
   * **Language** (`python`, `javascript`, `bash`, `ruby`, or `lua`)
   * **Project path** (use `.` if you are already inside the folder)
   * **Command name** (the command you want to type in your terminal)

## Uninstall

To remove `mkcmd` from your system:
```bash
sudo rm /usr/local/bin/mkcmd
```

### Language and feature requests

Any language or feature requests? You can open an issue or email me at jacob.a.rinaldi@gmail.com

### Planned and upcoming features

1. Windows support
2. Uninstalling commands you have made
3. Automaticly adding an install.sh file to your project folder to make your project much simpler to set up for others
4. More languages!
