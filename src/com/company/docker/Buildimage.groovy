package com.company.docker

class Buildimage {

    def steps

    Buildimage(steps) {
        this.steps = steps
    }

    def buildImage(String imageName) {

        steps.echo "Building Docker image: ${imageName}"

        steps.sh "docker build -t ${imageName} ."

        steps.echo "Docker image ${imageName} built successfully"
    }
}