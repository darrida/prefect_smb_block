from prefect.filesystems import RemoteFileSystem
from smb_block import SMB
# from prefect.filesystems import SMB


# had to create a share on a Windows computer on the network, with a read/write user


# have to comment out "overwrite=True" on line 298
# poetry run prefect deployment build test_flow.py:test_smb -sb remote-file-system/test-smb --name smb-test
smb = RemoteFileSystem(
    basepath='smb://benha/smb_test/',
    settings={
        'host': 'benha',
        'username': 'web',
        'password': '<password>',
    }
)
smb.save("test-smb", overwrite=True)

# had to made adjustment to filesystems.py (adjusted file in this repo) to get this to work
# poetry run prefect deployment build test_flow.py:test_smb -sb smb/test-smb --name smb-test
smb = SMB(
    share_path='/smb_test/', #'/SHARE/path_dir/path_dir/',
    host='benha', #'server.com',
    port=445,
    smb_access_username='web',
    smb_access_password='<password>',
)
smb.save("test-smb", overwrite=True)
