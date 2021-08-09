from conans import ConanFile, CMake, tools


class MathlibConan(ConanFile):
    name = "mathlib"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Vijayakumar> <vijay.selvimani@gmail.com>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Mathlib here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/msvijay90/math.git")

        tools.replace_in_file("math/CMakeLists.txt", "PROJECT(CalculatorApp)",
                              '''PROJECT(CalculatorApp)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="math")
        cmake.build()
        
    def package(self):
        self.copy("*.h", dst="include", src="math")
        self.copy("*math.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["math"]

