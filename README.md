# Python-rewrite branch for UnRen 2 (working title)
For now here resides the still unfinished python rewrite of the _UnRen application._ This
branch is intended to replace _master/main_ if development finished is.

Dev state is stable enough to do some testing and contribution of ideas or constructive
critique if anyone wishes.
> **Do not use for productive work!**

The following description is still a raw outline of the current project state respectively
development plans and subject to change **at any given time**.

<!-- madeddy: This line and above is to be removed on dev completion -->

# UnRen
Small multifunctional wrapper app around tools for the work with RenPy files.
The features offered include:
- Decompressing RPA files
- Decompiling RenPy script files (rpyc)
- Activating respectively reactivating:
 - Developer menu and console
 - Quick Save and Quick Load
 - Rollback function
 - Text skipping

This project adheres to [Semantic Versioning](https://semver.org).

## Usage
### Pure Python version
We can start the python-only scripts in two ways. Either we use the in your operating
system installed python or the one which comes with your RenPy game.

#### Using naitive Python
Open your systems terminal and use the command line for your use case.
With python 3.6+:
```sh
python3 unren_py36.py ../your_path/game_name/
```
With python 2.7+:
```sh
python2 unren_py27.py ../your_path/game_name/
```

#### Using RenPy's Python
To use the Python distribution which came along your game, the corresponding system
architecture must be selected in the lib folder. Also, if more as one OS available is
the correct OS directory must be considered.

_Any python 3 examples are for future use. There is as of now(March 2021) still no python 3
support in RenPy._

e.g. 
To use **64** Bit on **Linux** and with a Python **3** game:
```sh
../your_path/game_name/lib/linux-x86_64/python -EOO unren_py37.py ../your_path/game_name/
```
For **32** Bit on **Windows** and with a Python **2** game:
```sh
../your_path/game_name/lib/windows-i686/python -EOO unren_py27.py ../your_path/game_name/
```

### Console command version for win
Double click to start the app file or open a cmd terminal and execute there for example
```batch
C:\..\your_path\unren27.cmd
```
Alternatively use in the code line `unren36.cmd` if the game needs Python 3.

> Inside the game directory we called above `game_name` must be the directorys
`renpy`, `lib` and a starter file like `your_game_name.(exe|py|sh)`.
e.g. `the_question.py`
If not, you're in the wrong loction!

## Contributing
If you want to add something to this project, feel free to fork the UnRen repo
and open a pull request with your addition.

> Pull requests should by standard targeted at the develop branch

Though not interested in complicating things, we want to set some basic standards:
- Don't make commits and/or pull request to big; separate thematic if possible
- We mostly adhere to the pep8 standard. However, a line length of 90 is used and
  naming conventions not this strict.
- Purely cosmetic changes such as corrected typos or formatting are only accepted
  subject to reservation. They will also take a backseat behind other things.
- Fill always a self explaining commit message.
- If you're unsure if your contribution will be accepted ask beforehand. It's cost
  free.


---
_TBD:_
## Legal
### License

### Credits 
