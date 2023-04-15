from OneDrive_API import *


def main():
    with open("Settings.json") as file:
        settings = json.load(file)

    # Initialize
    onedrive = OneDrive(settings)

    # Creating directories
    onedrive_path = "/"
    new_foldername = time.strftime("%Y-%m")
    onedrive.MakeDir(onedrive_path,
                     new_foldername)

    # Uploading files
    files = os.listdir("upload_test")
    files = ["upload_test/" + file for file in files]
    onedrive_path += "/"+new_foldername
    onedrive.Upload(files, onedrive_path)

    # # Fetching
    # onedrive_path = ""
    # found_files, found_folders = onedrive.FetchAllFiles(onedrive_path)
    # print("Found files in " + onedrive_path + ":", list(found_files.keys()))
    # print("Found folders in " + onedrive_path + ":", list(found_folders.keys()))
    #
    # # # Downloading files (all available files in 'onedrive_path')
    # # onedrive_path = "Test/download_test"
    # # local_path = "download_test"
    # # onedrive.Download(onedrive_path, local_path)
    #

    #
    # # Moving files
    # onedrive_path_dest = "Test/move_test"
    # onedrive_path_src = "Test/download_test/"
    # onedrive.MoveAllFiles(onedrive_path_dest, onedrive_path_src)


if __name__ == "__main__":
    main()
