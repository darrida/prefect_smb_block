from typing import Optional
from pydantic import Field, SecretStr
from prefect.filesystems import RemoteFileSystem, ReadableFileSystem, WritableFileSystem
from pydantic import Field, SecretStr


class SMB(ReadableFileSystem, WritableFileSystem):
    """
    Store data as a file on a Samba (SMB) share.
    Example:
        Load stored SMB config:
        ```python
        from prefect.filesystems import SMB
        smb_block = SMB.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "SMB"
    _logo_url = "https://www.wikidancesport.com/Attachments/dances/Samba/Samba-2-crop.jpg?h=250"

    share_path: str = Field(
        ..., description="A Samba Share", example="share/a-directory-within"
    )
    smb_access_username: SecretStr = Field(None, title="Samba Username")
    smb_access_password: SecretStr = Field(None, title="Samba Password")
    host: str
    port: int = None

    _remote_file_system: RemoteFileSystem = None

    @property
    def basepath(self) -> str:
        return f"smb://{self.host.rstrip('/')}/{self.share_path.lstrip('/')}"

    @property
    def filesystem(self) -> RemoteFileSystem:
        settings = {}
        if self.smb_access_username:
            settings["username"] = self.smb_access_username.get_secret_value()
        if self.smb_access_password:
            settings["password"] = self.smb_access_password.get_secret_value()
        if self.host:
            settings["host"] = self.host
        if self.port:
            settings["port"] = self.port
        self._remote_file_system = RemoteFileSystem(
            basepath=f"smb://{self.host.rstrip('/')}/{self.share_path.lstrip('/')}", settings=settings
        )
        return self._remote_file_system

    async def get_directory(
        self, from_path: Optional[str] = None, local_path: Optional[str] = None
    ) -> bytes:
        """
        Downloads a directory from a given remote path to a local direcotry.
        Defaults to downloading the entire contents of the block's basepath to the current working directory.
        """
        return await self.filesystem.get_directory(
            from_path=from_path, local_path=local_path
        )

    async def put_directory(
        self,
        local_path: Optional[str] = None,
        to_path: Optional[str] = None,
        ignore_file: Optional[str] = None,
    ) -> int:
        """
        Uploads a directory from a given local path to a remote direcotry.
        Defaults to uploading the entire contents of the current working directory to the block's basepath.
        """
        return await self.filesystem.put_directory(
            local_path=local_path, to_path=to_path, ignore_file=ignore_file, overwrite=False
        )

    async def read_path(self, path: str) -> bytes:
        return await self.filesystem.read_path(path)

    async def write_path(self, path: str, content: bytes) -> str:
        return await self.filesystem.write_path(path=path, content=content)
