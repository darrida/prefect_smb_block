from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner
from smb_block import SMB


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



# Brief notes for setup
# prefect block register --file ..\smb_block.py
# python ..\block.py
# prefect deployment build test_smb.py:test_smb -sb smb/test-smb --name test_flow
