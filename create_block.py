from prefect.filesystems import RemoteFileSystem
from smb_block import SMB


# smb = RemoteFileSystem(
#     basepath='smb://SHARE/path_dir/path_dir/',
#     settings={
#         'host': 'server.com',
#         'username': '<USERNAME>',
#         'password': '<PASSWORD>',
#     }
# )
# smb.save("temp", overwrite=True)


smb = SMB(
    share_path='/SHARE/path_dir/path_dir/',
    host='server.com',
    smb_access_username='<USERNAME>',
    smb_access_password='<PASSWORD>',
)
smb.save("test-smb", overwrite=True)
