class StorageProvider:
    def upload(self, file):
        pass


class AWS(StorageProvider):
    def upload(self, file):
        print(f"Uploading {file} to AWS")


class GoogleCloud(StorageProvider):
    def upload(self, file):
        print(f"Uploading {file} to Google Cloud")


def upload_file(provider):
    provider.upload("data.txt")


upload_file(AWS())
upload_file(GoogleCloud())
