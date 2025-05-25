def main():
    print('File name:', end=' ')
    s = input()

    str = s.lower().strip()
    
    index = str.rfind('.')
    if index != -1:
        ext = str[index:]
    else:
        ext = str

    match ext:
        case ".gif":
            print('image/gif')
        case ".jpg" | ".jpeg":
            print('image/jpeg')
        case ".png":
            print('image/png')
        case ".pdf":
            print('application/pdf')
        case ".txt":
            print('text/plain')
        case ".zip":
            print('application/zip')
        case _:
            print('application/octet-stream')


main()