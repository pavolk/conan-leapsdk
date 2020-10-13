from conans import ConanFile, tools
import os, shutil

class LeapsdkConan(ConanFile):
    name = "leapsdk"
    version = "4.1.0"
    settings = "os", "compiler", "build_type", "arch"
    description = "<Description of Leapsdk here>"
    url = "None"
    license = "None"
    author = "None"
    topics = None

    def source(self):
        install_dir = os.environ.get("LeapSDK_DIR")
        shutil.copytree(os.path.join(install_dir, "LeapSDK/lib"), "lib")   
        shutil.copytree(os.path.join(install_dir, "LeapSDK/include"), "include")

    def build(self):
        pass

    def package(self):
        self.copy("*", src="include", dst="include")
        libdir = "lib/x86"
        if self.settings.arch == "x86_64":
            libdir = "lib/x64"
        self.copy("*.dll", src=libdir, dst="lib")
        self.copy("*.lib", src=libdir, dst="lib")
        self.copy("*.so", src=libdir, dst="lib")
        self.copy("*.a", src=libdir, dst="lib")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.includedirs = ['include']
