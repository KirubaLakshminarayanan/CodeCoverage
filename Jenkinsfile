pipeline {
    agent any
    environment {
        COVERAGE_REPORT_DIR = 'C:/Reports/Codecoveragereport'
        LOG_FILE = "${COVERAGE_REPORT_DIR}/build.log"
    }
    stages {
        stage('Clone Repository') {
            steps {
                // Checkout code from GitHub repository
                git url: 'https://github.com/KirubaLakshminarayanan/CodeCoverage.git'
            }
        }
        stage('Setup') {
            steps {
                script {
                    if (!fileExists(env.COVERAGE_REPORT_DIR)) {
                        bat "mkdir ${COVERAGE_REPORT_DIR}"
                    }
                }
                // Install dependencies and redirect output to log file
                bat 'pip install -r requirements.txt > ${LOG_FILE} 2>&1'
            }
        }
        stage('Run Tests with Coverage') {
            steps {
                // Run tests and generate coverage report
                bat 'coverage run -m pytest test_calculator.py >> ${LOG_FILE} 2>&1'
                bat "coverage html -d ${COVERAGE_REPORT_DIR}/html >> ${LOG_FILE} 2>&1"
                bat "coverage xml -o ${COVERAGE_REPORT_DIR}/coverage.xml >> ${LOG_FILE} 2>&1"
                // Log coverage results
                bat "coverage report >> ${LOG_FILE} 2>&1"
            }
        }
        stage('Publish Coverage Report') {
            steps {
                // Publish HTML report
                publishHTML(target: [
                    reportDir: "${COVERAGE_REPORT_DIR}/html",
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])
            }
        }
    }
    post {
        always {
            script {
                def emailBody = """
                    <p>Build Number: ${BUILD_NUMBER}</p>
                    <p>Code coverage report for build ${BUILD_NUMBER}:</p>
                    <p>See attached HTML and XML reports.</p>
                """
                if (fileExists(env.LOG_FILE)) {
                    emailBody += "<p>Build Log:</p><pre>${readFile(env.LOG_FILE)}</pre>"
                }
                emailext attachmentsPattern: "${COVERAGE_REPORT_DIR}/coverage.xml, ${COVERAGE_REPORT_DIR}/html/index.html",
                         subject: "Build ${BUILD_NUMBER} - Code Coverage Report",
                         body: emailBody,
                         to: "kiruba.lakshminarayanan@gmail.com"
            }
        }
    }
}
