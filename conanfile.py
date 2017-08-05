from conans import ConanFile, tools, os

class BoostSpiritConan(ConanFile):
    name = "Boost.Spirit"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/spirit"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "spirit"
    requires =  "Boost.Algorithm/1.64.0@bincrafters/testing", \
                      "Boost.Array/1.64.0@bincrafters/testing", \
                      "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Concept_Checks/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Endian/1.64.0@bincrafters/testing", \
                      "Boost.Filesystem/1.64.0@bincrafters/testing", \
                      "Boost.Foreach/1.64.0@bincrafters/testing", \
                      "Boost.Function/1.64.0@bincrafters/testing", \
                      "Boost.Function_Types/1.64.0@bincrafters/testing", \
                      "Boost.Fusion/1.64.0@bincrafters/testing", \
                      "Boost.Integer/1.64.0@bincrafters/testing", \
                      "Boost.Io/1.64.0@bincrafters/testing", \
                      "Boost.Iostreams/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Lexical_Cast/1.64.0@bincrafters/testing", \
                      "Boost.Locale/1.64.0@bincrafters/testing", \
                      "Boost.Math/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Optional/1.64.0@bincrafters/testing", \
                      "Boost.Phoenix/1.64.0@bincrafters/testing", \
                      "Boost.Pool/1.64.0@bincrafters/testing", \
                      "Boost.Predef/1.64.0@bincrafters/testing", \
                      "Boost.Preprocessor/1.64.0@bincrafters/testing", \
                      "Boost.Proto/1.64.0@bincrafters/testing", \
                      "Boost.Range/1.64.0@bincrafters/testing", \
                      "Boost.Regex/1.64.0@bincrafters/testing", \
                      "Boost.Serialization/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Thread/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Tti/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Typeof/1.64.0@bincrafters/testing", \
                      "Boost.Unordered/1.64.0@bincrafters/testing", \
                      "Boost.Utility/1.64.0@bincrafters/testing", \
                      "Boost.Variant/1.64.0@bincrafters/testing"

                      #algorithm9 array3 assert1 concept_check5 config0 core2 endian6 filesystem8 foreach8 function5 function_types5 fusion5 integer3 io1 iostreams10 iterator5 lexical_cast8 locale6 math8 mpl5 optional5 phoenix9 pool11 predef0 preprocessor0 proto8 range7 regex6 serialization11 smart_ptr4 static_assert1 thread11 throw_exception2 tti6 type_traits3 typeof5 unordered8 utility5 variant9
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)

    def package_id(self):
        self.info.header_only()