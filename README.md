<h2 align="center">Autotests API project for https://reqres.in/ & https://demowebshop.tricentis.com/</h2>

<h2 align="center">Stack and tools</h2>

<p  align="center">
  <code><img width="5%" title="Pycharm" src="attach/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="attach/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="attach/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="attach/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="attach/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="attach/logo/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="attach/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="attach/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="attach/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="attach/logo/telegram.png"></code>
  <code><img width="5%" title="Telegram" src="attach/logo/selenoid.png"></code>
</p>

### What does the test do:
![Screen](attach/screenshots/about_tests.png)

### :man_technologist: Launch tests form cli
```bash
pytest tests/test_reqres.py --env=prod
pytest tests/test_demowebshop.py --env=prod
```

The project uses logger
![Screen](attach/screenshots/requests_logging.png)

### <img width="3%" title="Jenkins" src="attach/logo/jenkins.png"> Project in Jenkins

### [Job](https://jenkins.autotests.cloud/job/nvfedo_API_reqres_in/)

#### Just click "Build Now" and the tests will start building and passing them through the virtual machine.
![Screen](attach/screenshots/jenkins_main.png)

### <img width="2%" title="Allure Report" src="attach/logo/allure_report.png"> Allure report

#### After passing the tests, the results are recorded in the Allure report. Tests have attachments such as screenshot, video, page_source and browser log.
![Screen](attach/screenshots/allure_report.png)

### <img width="2%" title="Allure TestOps" src="attach/logo/allure_testops.png"> Allure TestOps

Integration with Allure TestOps is also configured. After running a job from Jenkins, a launch is automatically created in Allure TestOps.
For example, this launch was created at the same time as the launch of the job from Jenkins.
![Screen](attach/screenshots/launches.png)
We can also create test cases and run jobs
![Screen](attach/screenshots/testcase.png)
It is also possible to select the necessary ones from the test cases tab and run the launch with them (without visiting Jenkins
![Screen](attach/screenshots/job_run.png)

### <img width="2%" title="Jira " src="attach/logo/jira.png"> Jira 
Integration with bug tracking system Jira has been set up, allowing you to link launches and test cases to tasks.
![Screen](attach/screenshots/jira.png)

### <img width="2%" title="Telegram" src="attach/logo/telegram.png"> Telegram
Configured a telegram bot that sends a notification with a report after completing a job from Jenkins.
![Screen](attach/screenshots/telegram_notification.png)