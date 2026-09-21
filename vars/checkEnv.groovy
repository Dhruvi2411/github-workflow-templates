import com.company.devops.DeploymentValidator

def call(String env) {
    def m1 = new DeploymentValidator()

    def ans = m1.isValidEnvironment(env)

    return ans
}
