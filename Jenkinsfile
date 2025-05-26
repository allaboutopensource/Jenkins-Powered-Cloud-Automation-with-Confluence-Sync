pipeline {
    agent {
        label "linux-agent"
    }

    environment {
        GIT_CREDENTIALS = 'git-token'
        API_KEY = credentials('27')
        email = 'svc_jenkins_confluen@your-company.com'
        BASELINE_REPO = 'git.your-company.com:7999/ci/openstack-project-list.git'
        BASELINE_BRANCH = 'main'
        BASELINE_CMD = './openstack_project_list.py'
        OS_AUTH_URL = 'https://your-company.com:5000'
        OS_PROJECT_ID = 'sdfbsjdhfbq82yjshfb8yq2q33'
        OS_PROJECT_NAME = 'Devops'
        OS_USER_DOMAIN_NAME = 'R&D'
        OS_PROJECT_DOMAIN_ID = 'sdfkjhsjkef2qi483847jdfbjsdbfgp324'
        OS_REGION_NAME = 'PROD'
        OS_INTERFACE = 'public'
        OS_IDENTITY_API_VERSION = '3'

    }

    stages {

       stage('Run OpenStack Project List Report') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'yourcreds', usernameVariable: 'OS_USERNAME', passwordVariable: 'OS_PASSWORD')]) {
                  sh "python3 openstack_project_list.py > Openstack-Project-List.txt"
                  sh "python3 Confluence.py"
                }
              }
       }
       stage('Upload Data to Confluence') {
        steps {
                withCredentials([usernamePassword(credentialsId: 'yourcreds', usernameVariable: 'OS_USERNAME', passwordVariable: 'OS_PASSWORD')]) {
                  sh "python3 Confluence.py"
                }
              }
       }
      stage('Send Email') {
            steps {
                emailext (
                    subject: "Current OpenStack Project List",
                    body: "Attached is the OpenStack Project List Report.",
                    to: "test@yourcompany.com",
                    attachmentsPattern: "Openstack-Project-List.txt"
                )
            }
        }
    }    
}
