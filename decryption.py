import pyAesCrypt
import os


# file decryption function
def decryption(file, password):

    # set the buffer size
    buffer_size = 512 * 1024

    # call the decryption method
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    # to see the result print the name of the encrypted file
    print("[File '" + str(os.path.splitext(file)[0]) + "' is decrypted")
    # delete the original file
    os.remove(file)


# directory scanning function
def walking_by_dirs(dir, password):
    # iterate through all subdirectories in the specified directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # if we find a file, we decrypt it
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
            # if we find a directory, then repeat the cycle in search of files
        else:
            walking_by_dirs(path, password)


password = input("Enether the password for encrypting")
walking_by_dirs("" , password)
# The "" is the path to the file\s