# SPM-G7T7
SPM Project Repository

# Installation and Running the Application
1. Ensure wamp is installed and turned on
2. In phpmyadmin (http://localhost/phpmyadmin), run script.sql to load the databases
3. Also in phpmyadmin, create a new account 'sbrp' with no password, with all Data privileges checked
4. Launch docker and log in
5. Delete any existing containers and images
6. In the docker-compose.yaml file in the ‘microservices’ folder, replace all DockerIDs (if you're pulling this code from the repo it should currently be 'timtay') with your own DockerID.
7. Open a new CMD terminal and set the directory to that of the ‘dockercompose’ folder
8. Enter the command “docker-compose build”, followed by “docker-compose up” to build the images and run containers
9. Open staff-profile.html on a live server and you should see a staff profile page with all its data loaded

Note: you may have to change the localhost port in each dbURL entry in the docker-compose.yaml file to match yours

