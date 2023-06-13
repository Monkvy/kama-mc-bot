import os
import subprocess


def open(pid: int) -> subprocess.Popen:
    fd = os.open(f"/proc/{pid}/fd/0", os.O_RDWR)
    subprocess.Popen("", stdin=fd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.close(fd)

