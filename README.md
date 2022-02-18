# Renamer-Drag-n'-Drop

This simple python script allows you to drag and drop any files and operate some renaming operations on them.
This tool will always do all the operations to all the dragged-n'-dropped files, but only after you confirmed that the alterations are correct.

No GUI available yet. By default the separators inside the filename is the underscore-character '_'


## Operations

Possible renaming operations are:
1. append
	Appends a specified string to all filenames
	./asdf-dir/01_filename.pdf -> ./asdf-dir/01_filename_date.pdf
2. replace
	Replaces a substring of the filename with a new substring
	./asdf-dir/01_filename.pdf -> ./asdf-dir/01_newname.pdf
3. insert
	Suffixes the filename with the provided new string
	./asdf-dir/01_filename.pdf -> ./asdf-dir/old_01_filename.pdf
4. switch
	Lets you switch around substrings divided by a separators
	./asdf-dir/01_filename_date.pdf -> ./asdf-dir/date_01_filename.pdf

Lastly, after checking the final output, execute the renaming operations by entering 'e'