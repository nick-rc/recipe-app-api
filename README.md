# recipe-app-api
Course Example

# Setup Walkthrough
Running Windows 10 Pro
Setup Docker Desktop w/ Docker Compose

1.) Add Dockerfile
- Dockerfile sets up the docker image and defines the project scope.
- See file Dockerfile

2.) Link docker-compose file
- see docker-compose.yml

3.) Link Travis-CI
- see .travis.yml

4.) Add flake8 linting
- see .flake8

Order of operations:
A.) Dockerfile defines environment
B.) docker-compose setups up the project for running in container.
    - Can use docker-compose for running testing locally as well.
C.) travis.yml responsible for running commands related to Travis-CI online testing
D.) Run tests in tests.py file.
