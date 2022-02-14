import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def uploadFile(image_name):
    access_token = 'sqAnqpyuEbEAAAAAAAAAAeq5g1lN-CiRqZXtpVgrcWvVqkN6WuEN3WN-TVd_WFcV'
    
    file = image_name
    file_from = file
    file_to = "/test images/" + (image_name)

    dbx = dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    access_token = 'sqAnqpyuEbEAAAAAAAAAAeq5g1lN-CiRqZXtpVgrcWvVqkN6WuEN3WN-TVd_WFcV'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer- ")
    file_to = input("Enter the full path to upload to dropbox- ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been uploaded")

if __name__ == '__main__':
    main()