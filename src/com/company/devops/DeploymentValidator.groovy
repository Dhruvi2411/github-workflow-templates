package com.company.devops

class DeploymentValidator {
    
    boolean isValidEnvironment(String env) {
        // if(env in ['dev', 'qa', 'stage', 'prod']) {
        //     return true
        // }
        // else{
        //     return false
        // }
        return env in ['dev', 'qa', 'stage', 'prod']
    }
}