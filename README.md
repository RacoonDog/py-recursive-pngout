# py-recursive-pngout

Simple utility for recursively PNGOUT compressing files in a directory.

### Requirements

- [PNGOUT](http://advsys.net/ken/utils.htm) executable on the path/directory
- python obviously

### Usage

`py recursive-pngout -e <pngout executable location> -i <input directory> -p <pngout parameters>`

Optional parameters:
- `-e`: PNGOUT executable location, defaults to `pngout`
- `-i`: Input directory relative to cwd, defaults to cwd
- `-p`: PNGOUT parameters, defaults to `/y`