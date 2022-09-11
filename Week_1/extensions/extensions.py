def main():
    file_name = input("File name: ")
    file_type(file_name)

def file_type(ft):
    # loer() returns the lowercase version of the string
    # strip() removes whitespace from the beginning and end of the string
    # split() splits the string into a list of substrings
    ft = ft.lower().strip().split(".")
    # receive the last element of the list
    ft = ft[-1]
    if ft == "gif" or ft == "png":
        # Split() returns a list of strings split at the specified separator.
        print(f"image/{ft.split('.')[-1]}")
    elif ft == "jpg" or ft == "jpeg":
        print("image/jpeg")
    elif ft == "pdf" or ft == "zip":
        #[-1] returns the last element of the list
        print(f"application/{ft.split('.')[-1]}")
    elif ft == "txt":
        print(f"text/plain")
    else:
        print("application/octet-stream")

main()