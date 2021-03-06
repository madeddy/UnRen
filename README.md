# Dev branch
At the moment **this is the development branch** for the python rewrite of the
_UnRen application._
> **Do not use for productive work!**

The following content is just a raw outline of the current project state respectively
development plans and subject to change **at any given time**.

<!-- madeddy: This line and above is to be removed on dev completion -->


This project adheres to [Semantic Versioning](https://semver.org).



## Project content overview
### _Release version files_
`unren_py36.py` / `unren_py27.py`  
The UnRen main app for py 3.6+ or 2.7 completely in python. Users who want to use
this variant must be able to work with a terminal.
_In progress_

_Perhaps never used
`unren_36.cmd` / `unren_27.cmd`  
A command script wrapper for the UnRen main app for py 3.6+ or 2.7. For users who
want to use one-click start for the app._


### _Internal used project module files_ 

`unren_build.py`  
A helper script who constructs the final release versions from different source
files.
- Step 1: Collects the rpy snippeds and embeds them in the raw python script. Converts
also the tools to a bytestream and embeds them also(+ pickled and base coded).
- Step 2 (optional, just windows): Writes the previously prepaired UnRen python
script in the batch file. 
_In progress_

`_ur_vers.py`
Holds the global version number for the project.

`ur_raw_36.py` / `ur_raw_27.py`  
The basic development files (py3.6+ / py2.7) before embedding of additional data
taked places.
_In progress_

`ur_tools/*`  
Contains actual versions of the used third party tools which will be embeddet in
the python script.
_Completed_

`operable/*`  
Here will reside the projects release versions.

`_storage/*`  
For safekeeping of unused or old project files in case they're needed again.

`ur_base.cmd`  
This Windows command file is planed as the one-click starter for the python main
app. The python code will be embeded so we get a hybrid file.
_Completed_

`ur_embed_36.py` / `ur_embed_27.py`  
The reduced version of the UnRen(py3.6+ / py2.7) for embedding in the batch
script.
_Not started_

`readme.md`  
...the file for the stuff you read just now.

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

