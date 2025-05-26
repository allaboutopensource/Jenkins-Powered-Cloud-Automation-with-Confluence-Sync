pipeline {
    agent {
        label "debian-python3"
    }

    environment {
        GIT_CREDENTIALS = 'itops-scm-git-token'
        API_KEY = credentials('27')
        email = 'svc_jenkins_confluen@ellucian.com'
        BASELINE_REPO = 'git.ellucian.com:7999/ci/openstack-project-list.git'
        BASELINE_BRANCH = 'main'
        BASELINE_CMD = './openstack_project_list.py'
        OS_AUTH_URL = 'https://iadosvip01.ece.ellucian.com:5000'
        OS_PROJECT_ID = '7b9b3c86a8ab4a6e9a1cdc8bb07ae190'
        OS_PROJECT_NAME = 'IT Admin'
        OS_USER_DOMAIN_NAME = 'Corp'
        OS_PROJECT_DOMAIN_ID = '4fbe9bec195c4f4c85dbb68d7c529088'
        OS_REGION_NAME = 'iadprod'
        OS_INTERFACE = 'public'
        OS_IDENTITY_API_VERSION = '3'

    }

    stages {

       stage('Run OpenStack Project List Report') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'openstack-autobot-integration', usernameVariable: 'OS_USERNAME', passwordVariable: 'OS_PASSWORD')]) {
                  sh "python3 openstack_project_list.py > Openstack-Project-List.txt"
                  sh "python3 Confluence.py"
                }
              }
       }
       stage('Upload Data to Confluence') {
        steps {
                withCredentials([usernamePassword(credentialsId: 'openstack-autobot-integration', usernameVariable: 'OS_USERNAME', passwordVariable: 'OS_PASSWORD')]) {
                  sh "python3 Confluence.py"
                }
              }
       }
      stage('Send Email') {
            steps {
                emailext (
                    subject: "Current OpenStack Project List",
                    body: "Attached is the OpenStack Project List Report.",
                    to: "RD-Operations-IA@ellucian.com",
                    attachmentsPattern: "Openstack-Project-List.txt"
                )
            }
        }
    }    
}
