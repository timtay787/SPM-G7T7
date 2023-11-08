# SPM-G7T7
SPM Project Repository

# Installation and Running the Application
1. Ensure wamp is installed and turned on
2. In phpmyadmin (http://localhost/phpmyadmin), run script.sql to load the databases
3. Also in phpmyadmin, create a new account 'sbrp' with no password, with all Data privileges checked
4. Launch docker and log in
5. Delete any existing containers and images
6. In the docker-compose.yaml file in the ‘microservices’ folder, replace all DockerIDs (if you're pulling this code from the repo it should currently be 'timtay') with your own DockerID.
7. Open a new CMD terminal and set the directory to the microservices folder.
8. Enter the command “docker-compose build”, followed by “docker-compose up” to build the images and run containers
9. Open staff-profile.html on a live server and you should see a staff profile page with all its data loaded
10. To switch between staff and HR view of the application, change the "is_hr" variable in vuejs/setSessionStorage.js to 0 and 1 respectively. We plan to have this value set by the staff member's log in credentials in future implementations.

Note: you may have to change the localhost port in each dbURL entry in the docker-compose.yaml file to match yours

# Running the integration test files
1. Before running the integration tests, make sure to set the 'SQLALCHEMY_DATABASE_URI' by commenting out the line "app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')" and uncommenting the line "app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/sbrp_db'"
2. Import the file script2.sql into localhost. You will need to repeat this step again before switching over to the next integration test file.
3. Run the test files