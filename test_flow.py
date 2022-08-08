from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner
# from smb_block import SMB
# from prefect.filesystems import SMB


# smb = SMB.load('test-smb')
# print(smb.host)


@task()
def put_dir():
    print(27)


@flow(name="test_smb", task_runner=SequentialTaskRunner)
def test_smb():
    put_dir()


if __name__ == '__main__':
    test_smb()



# # Brief notes for setup
# # - custom changes to make work
# #    - Adjusted prefect.filesystems.py with changes present in prefect_filesystems.py in this repo
# #    - Copied SMB() Block class from smb_block.py into bottom of prefect.filesystems.py
# prefect block register --file .\smb_block.py
# python .\create_block.py
# # local run
# prefect deployment build test_smb.py:test_smb -sb smb/test-smb --name test_flow  (can successfully test this because I run it in the local environment I changed filesystems.py in)
# # docker run
# prefect deployment build test_smb.py:test_smb -sb smb/test-smb -ib docker-container/prefect-2-0-2-python39 --name test_flow  (cannot yet successfully run this because the vendor container doesn't have adjusted filesystems.py)
