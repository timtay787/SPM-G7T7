<?php 
  // $name = $_SESSION['userid'];
  $name = 'Megan Tan';
  $email = 'megantan@gmail.com';
  $index = 'staff-profile.php';

  //set variables
  $servername = 'localhost';
  $username = 'root';
  $password = '';

  //create connection
  $connection_1 = mysqli_connect($servername, $username, $password, 'role_listing_db');
  $connection_2 = mysqli_connect($servername, $username, $password, 'role_db');

  //Check connection
  if(!$connection_1){
    die("Connection_1 failed: ".mysqli_connect_error());
  }
  echo "Connected_1 successfully <br>";

  if(!$connection_2){
    die("Connection_2 failed: ".mysqli_connect_error());
  }
  echo "Connected_2 successfully <br>";

  //Fetch Data
  $fetchDataQuery_1 = "SELECT * from role_listings";
  $result_1 = mysqli_query($connection_1, $fetchDataQuery_1);

  $fetchDataQuery_2 = "SELECT * from role_details";
  $result_2 = mysqli_query($connection_2, $fetchDataQuery_2);

  //For own testing: Check if any data
  //if(mysqli_num_rows($result)>0){

    //while($row = mysqli_fetch_assoc($result)){
    //    echo "Job Title: ".$row["Role_ID"]. "<br>";
    //}
 // }
  //else{ echo "No record found <br>"; } 

  //Close connection
  //mysqli_close($connection);

?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>All-In-One Connect</title>

  <!-- CUSTOM JS -->
  <link rel="icon" type="image/x-icon" href="/images/favicon.png">
  <link rel="stylesheet" href="vendors/feather/feather.css">
  <link rel="stylesheet" href="vendors/mdi/css/materialdesignicons.min.css">
  <link rel="stylesheet" href="vendors/ti-icons/css/themify-icons.css">
  <link rel="stylesheet" href="vendors/typicons/typicons.css">
  <link rel="stylesheet" href="vendors/simple-line-icons/css/simple-line-icons.css">
  <link rel="stylesheet" href="vendors/css/vendor.bundle.base.css">
  <link rel="stylesheet" href="vendors/datatables.net-bs4/dataTables.bootstrap4.css">
  <link rel="stylesheet" href="js/select.dataTables.min.css">
  <link rel="stylesheet" href="css/vertical-layout-light/style.css">
</head>

<body>

<!-- TOP BAR -->
  <div class="container-scroller">
      <!-- LOGO-->
    <nav class="navbar default-layout col-lg-12 col-12 p-0 fixed-top d-flex align-items-top flex-row">
      <div class="text-center navbar-brand-wrapper d-flex align-items-center justify-content-start">
        <div class="me-3">
          <button class="navbar-toggler navbar-toggler align-self-center" type="button" data-bs-toggle="minimize">
            <span class="icon-menu"></span>
          </button>
        </div>
        <div>
          <a class="navbar-brand brand-logo" href="staff-profile.php">
            <img src="images/logo.png" alt="logo" />
          </a>
          <a class="navbar-brand brand-logo-mini" href="staff-profile.php">
            <img src="images/logo-mini.png" alt="logo" />
          </a>
        </div>
      </div>
      <div class="navbar-menu-wrapper d-flex align-items-top"> 
      <!-- WELCOME ADMIN -->
        <ul class="navbar-nav">
          <li class="nav-item font-weight-semibold d-none d-lg-block ms-0">
            <h1 class="welcome-text">Hello, <span class="text-black fw-bold"><?php echo $name?></span></h1>
            <h3 class="welcome-sub-text">Welcome to All-In-One Connect.</h3>
          </li>
        </ul>
      </div>
    </nav>

    <!-- SIDE BAR -->
    <div class="container-fluid page-body-wrapper">      
      <nav class="sidebar sidebar-offcanvas" id="sidebar">
        <ul class="nav">
          <li class="nav-item">
            <a class="nav-link" href="staff-profile.php" aria-expanded="false" aria-controls="form-elements">
              <i class="menu-icon mdi mdi-account-circle-outline"></i>
              <span class="menu-title">Profile</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="staff-role-listings.php" aria-expanded="false" aria-controls="form-elements">
              <i class="menu-icon mdi mdi-card-text-outline"></i>
              <span class="menu-title">Role Listings</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="staff-my-applications.php">
              <i class="mdi mdi-grid-large menu-icon"></i>
              <span class="menu-title">Applications</span>
            </a>
          </li>
        </ul>
      </nav>
      
      <!-- MAIN PANEL -->
      <div class="main-panel">
        <div class="content-wrapper">
          <div class="row">
          <h2 class="text-black fw-bold">Role Listings</h2>
          <h2> </h2>
          <h2 class="text-black fw-bold"> </h2>
          <div class="col-lg-12 grid-margin stretch-card">              
            <div class="card">
                <div class="card-body">
                  <div class="table-responsive">
                    <table class="table table-hover">
                      <thead>
                        <tr>
                          <th><h6>Job Title</h6><p>Department</p></th>
                          <th>Hiring Manager</th>
                          <th>Skills Match</th>
                          <th>Status</th>
                        </tr>
                      </thead>
                      <tbody>
                        <?php
                        if(mysqli_num_rows($result_1)>0){
                            while($row1 = mysqli_fetch_assoc($result_1) and $row2 = mysqli_fetch_assoc($result_2)){
                                $roleID = $row1["Role_ID"];
                                //$roleID = array();
                                $roleDesc = $row1["Role_Listing_Desc"];
                                $jobTitle = $roleID[$row2["Role_Name"]];
                        ?>
                        
                        
                        <tr>
                          <td><h6><?php echo $jobTitle; ?></h6><p>Marketing</p></td>
                          <td>Julie Tan</td>
                          <td>
                            <div class="progress">
                                <div class="progress-bar bg-success" role="progressbar" style="width: 80%" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                            <div class="text-success"> 90% </div>
                          </td>
                          <td><button type="button" onclick="location.href = 'role-listing-info.php'" class="btn btn-success">Open</button></td>
                        </tr>
                        <?php } 
                            }
                            else{ echo "No record found <br>"; }
                        ?>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>


  <!-- CUSTOM JS -->
  <script src="vendors/js/vendor.bundle.base.js"></script>
  <script src="vendors/chart.js/Chart.min.js"></script>
  <script src="vendors/bootstrap-datepicker/bootstrap-datepicker.min.js"></script>
  <script src="vendors/progressbar.js/progressbar.min.js"></script>
  <script src="js/off-canvas.js"></script>
  <script src="js/hoverable-collapse.js"></script>
  <script src="js/template.js"></script>
  <script src="js/settings.js"></script>
  <script src="js/todolist.js"></script>
  <script src="js/jquery.cookie.js" type="text/javascript"></script>
  <script src="js/dashboard.js"></script>
  <script src="js/Chart.roundedBarCharts.js"></script>
</body>

</html>