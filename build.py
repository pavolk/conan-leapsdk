import os, sys
import platform

def system(command):
    retcode = os.system(command)
    if retcode != 0:
        raise Exception("Error while executing:\n\t %s" % command)

if __name__ == "__main__":
    params = " ".join(sys.argv[1:])

    if platform.system() == "Windows":
        system('conan create . -s arch=x86 -s build_type=Debug %s' % params)
        system('conan create . -s arch=x86 -s build_type=Release %s' % params)
        system('conan create . -s arch=x86_64 -s build_type=Debug %s' % params)
        system('conan create . -s arch=x86_64 -s build_type=Release %s' % params)
    else:
        pass