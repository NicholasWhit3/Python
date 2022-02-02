import pyAesCrypt
import os


# file encryption function
def encryption(file, password):
    # set the buffer size
    buffer_size = 512 * 1024

    # call the encryption method
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # to see the result print the name of the encrypted file
    print("[File '" + str(os.path.splitext(file)[0]) + "' is encrypted")

    # delete the original file
    os.remove(file)


# directory scanning function
def walking_by_dirs(dir, password):
    # iterate through all subdirectories in the specified directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # if we find a file, we encrypt it
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
            # if we find a directory, then repeat the cycle in search of files
        else:
            walking_by_dirs(path, password)


password = input("Enter the password for encrypting")
walking_by_dirs("", password)
# The "" is the path to the file\s
