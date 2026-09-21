import com.company.test.TestUtils

def call(String imagename) {

    def t1 = new TestUtils()

    def ans = t1.buildImage(imagename)

    echo ans
}