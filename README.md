# file-splitter
## Usage
### Split a file
`split(filename, chunck_size)`

**filename** parameter is the path of the file to split
**chunk_size** parameter is the size per part
The result will be **n** files wich size equals to the **chunk_size**. All filename are appended by ".part{n}" 

### Join spitted file
`join_files(first_file, output_path`)

**first_file** will be the path to the first part of the file
**output_path** is the path of the joined file
