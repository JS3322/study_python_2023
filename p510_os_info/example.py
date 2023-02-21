import platform
import psutil


def printOSInfo():
    print('OS = ', platform.system())
    print('OS Version = ', platform.version())
    print('Process information  = ', platform.processor())
    print('Process Architecture = ', platform.machine())
    print('RAM Size             = ', str(round(psutil.virtual_memory().total / (1024.0 **3)))+"(GB)")


if __name__ == '__main__':
    printOSInfo()
