import os

def join_files(first_file:str, output_path:str):
    
    output_file = open(output_path, 'wb')
    list_file = []
    print(os.path.dirname(first_file))
    for _, _, files in os.walk(os.path.dirname(first_file)):
        for f in files:
            if '.part' in f:
                list_file.append(f)
                
                
                print(f)
        break
    list_file.sort()
    for f in list_file:
        with open(os.path.join(os.path.dirname(first_file), f), 'rb') as file:
            output_file.write(file.read())

    
        
    output_file.close()

def split(filename:str, chunk_size:int):
    filename = filename
    
    
    with open(filename, 'rb') as file:
        bytes_ = file.read()
        start_ = 0
        end_ = 1
        part = 1
        current_size = 0
        output = open(f'{filename}.part{part}', 'wb')
        
        
        while end_ <= len(bytes_):
            output.write(bytes_[start_: end_])
            
            start_ = end_
            end_ += 1
            current_size += 1

            if current_size >= chunk_size:
                part += 1
                output = open(f'{filename}.part{part}', 'wb')
                current_size = 0
        output.close()


if __name__ == "__main__":
    # filename = input("Path of the file to split > ")
    # split(filename)

    filename = input("path of first file to join > ")
    # chunk_size = int(input("File size per file > "))

    # split(filename, chunk_size)


    join_files(filename, filename.replace('.part1', ''))

