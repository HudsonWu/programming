# pathlib

## Path, deal with file paths on windows mac and linux

```
from pathlib import Path
import webbrowser

data_folder = Path("source_data/text_files/")

file_to_open = data_folder / "raw_data.txt"

print(file_to_open.read_text())

webbrowser.open(file_to_open.absolute().as_uri())
```

## standard file operations

```
from pathlib import Path

filename = Path("source_data/text_files/raw_data.txt")

print(filename.name)
# raw_data.txt

print(filename.suffix)
# txt

print(filename.stem)
# raw_data

if not filename.exists():
    print("Oops, file doesn't exist!")
else:
    print("Yay, the file exists!")
```

## PurePath and PureWindowsPath

```
from pathlib import PurePath

print(pathlib.PurePath(__file__).match('*.py'))
# True

pure_path = PurePath(__file__)
print(pure_path, type(pure_path))
# /path/to/example.py <class 'pathlib.PurePosixPath'>
```

```
from pathlib import Path, PureWindowsPath

filename = Path("source_data/text_files/raw_data.txt")

# Convert path to Windows format
path_on_windows = PureWindowsPath(filename)

print(path_on_windows)
# source_data\text_files\raw_data.txt
```

```
from pathlib import Path, PureWindowsPath

filename = PureWindowsPath("source_data\\text_files\\raw_data.txt")

correct_path = Path(filename)

print(correct_path)
# source_data/text_files/raw_data.txt  # on Mac and Linux
# source_data\text_files\raw_data.txt  # on Windows
```

## get file path

```
from pathlib import Path

# 获取文件当前路径
Path.cwd()

# 获取上层目录
Path.cwd().parent
Path.cwd().parent.parent

# 路径拼接
parts = ["dir1", "dir2", "dir3"]
Path.cwd().parent.joinpath(*parts)
```
