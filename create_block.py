from prefect.filesystems import RemoteFileSystem
from smb_block import SMB


# smb = RemoteFileSystem(
#     basepath='smb://prefect_storage/test/',
#     settings={
#         'host': 'pi4-main',
#         'username': 'pi',
#         'password': 'Qf6DJBecymsQKa4xwFmviqYHQfewxz',
#     }
# )
# smb.save("test-smb", overwrite=True)


smb = SMB(
    share_path='/share/', #'/SHARE/path_dir/path_dir/',
    host='127.0.0.1', #'server.com',
    port=444,
    smb_access_username='web',
    smb_access_password='new',
)
smb.save("test-smb", overwrite=True)


# docker run -it -v/var/www:/share/web -p 444:445 -e sharename=web -e password=1234578 ahmetozer/samba
# useradd
# web
# new
# reload-samba
