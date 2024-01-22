"""
Custom storage backend for media files using Amazon S3.
"""

from storages.backends.s3boto3 import S3Boto3Storage


class MediaStore(S3Boto3Storage):
    """
    Custom storage class for handling media files.

    Attributes:
        location (str): The subdirectory within the S3 bucket where media files will be stored.
        file_overwrite (bool): Flag indicating whether existing files should be overwritten.
    """
    location = 'media'
    file_overwrite = False

    def get_accessed_time(self, name):
        """
        Get the last accessed time of the file.

        Args:
            name (str): The name of the file.

        Returns:
            datetime: The last accessed time.
        """
        # Implement your logic here

    def get_created_time(self, name):
        """
        Get the creation time of the file.

        Args:
            name (str): The name of the file.

        Returns:
            datetime: The creation time.
        """
        # Implement your logic here

    def path(self, name):
        """
        Get the local filesystem path of the file.

        Args:
            name (str): The name of the file.

        Returns:
            str: The local filesystem path.
        """
        # Implement your logic here
