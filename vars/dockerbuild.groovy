import com.company.devops.Buildimage

def call(String imageName) {

    def docker = new Buildimage(this)

    docker.buildImage(imageName)
}