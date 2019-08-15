# ALF command line interface

Command line interface for ALF, functions including:

```
 Usage: alf [OPTIONS] COMMAND [ARGS]...

Options:
  --help         Show this message and exit.

Commands:
  configure  Configure API key.
  download   Download dataset via alf.
  upload     Upload dataset via alf.
```

```
Usage: alf structure [OPTIONS]

Options:
  --source TEXT         Source name of S3.
  --show_file TEXT      Show list file by the folder.
  --show_full_dir TEXT  Show full path of the folder.
  --help                Show this message and exit.
```

## How to install

```bash
pip install alf@git+https://github.com/hieutrieu/alf@master
# Or install using SSH
pip install alf@git+ssh://git@github.com/hieutrieu/alf@master
```


## How to use
 * Configure KEYS:
 ```
 alf configure

 ```
 * Download dataset:
 ```
 alf download --help

 ```
 * Upload dataset:
 ```
 alf upload --help
 ```
 * Show structure folder of S3
 ```
 alf structure
 ```
