from conans import ConanFile
import TM_CommonPy as TM


class OBSEPackaging_Conan(ConanFile):
    name = "Plog"
    version = "0.1"
    license = "MPL v2.0"
    url = "https://github.com/SergiusTheBest/plog"
    description = "C++ Logger."
    author = "SergiusTheBest"

    def source(self):
        TM.Run("git clone https://github.com/SergiusTheBest/plog.git")

    def package(self):
        self.copy("*", src="plog/include", dst='include/')

    def package_info(self):
        self.cpp_info.includedirs = ['include']
