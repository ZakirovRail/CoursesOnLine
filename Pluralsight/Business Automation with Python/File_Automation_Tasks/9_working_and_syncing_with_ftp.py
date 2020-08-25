# ftpsync library shuld be installed


from ftpsync.targets import FsTarget
from ftpsync.ftp_target import FtpTarget
from ftpsync.syncronizers import UploadSynchronizer

local = FsTarget('C:\\foo')
user = 'user'
passwd = 'pwd'
remote = FtpTarget("/foo", "svr.com", username=user, password=passwd)
opts = {"force":False, "delete_unmatched":True, "verbose":3}
s = UploadSynchronizer(local, remote, opts)
s.run()

