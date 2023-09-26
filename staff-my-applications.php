<?php 
  // $name = $_SESSION['userid'];
  $name = 'Megan Tan';
  $email = 'megantan@gmail.com';
  $index = 'staff-profile.php'
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
          <h2 class="text-black fw-bold">Applications</h2>
          <h2> </h2>
          <h2 class="text-black fw-bold"> </h2>
          <div class="col-lg-12 grid-margin stretch-card">              
            <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Pending</h4>
                  <div class="table-responsive">
                    <table class="table table-hover">
                      <thead>
                        <tr>
                            <th>Application ID</th>
                            <th><h6>Job Title</h6><p>Department</p></th>
                            <th>Hiring Manager</th>
                            <th>Date of Application</th>
                            <th>Status</th>
                            <th><th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                            <td>01234</td>
                            <td><h6>Social Media Manager</h6><p>Marketing</p></td>
                            <td>Julie Tan</td>
                            <td>01/06/2023</td>
                            <td><label class="badge badge-warning">Draft</label></td>
                            <td><button type="button" onclick="location.href = 'staff-application.php'" class="btn btn-primary">View Application</button></td>
                        </tr>
                        <tr>
                            <td>02345</td>
                            <td><h6>Content Creator</h6><p>Marketing</p></td>
                            <td>Julie Tan</td>
                            <td>01/06/2023</td>
                            <td><label class="badge badge-warning">Pending</label></td>
                            <td><button type="button" onclick="location.href = 'staff-application.php'" class="btn btn-primary">View Application</button></td>
                        </tr>
                        <tr>
                            <td>03456</td>
                            <td><h6>Data Analytics</h6><p>Strategy</p></td>
                            <td>Tan Kim Seng</td>
                            <td>02/06/2023</td>
                            <td><label class="badge badge-warning">Pending</label></td>
                            <td><button type="button" onclick="location.href = 'staff-application.php'" class="btn btn-primary">View Application</button></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
            <h2 class="text-black fw-bold"> </h2>
          <div class="col-lg-12 grid-margin stretch-card">              
            <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Past</h4>
                  <div class="table-responsive">
                    <table class="table table-hover">
                      <thead>
                        <tr>
                            <th>Application ID</th>
                            <th><h6>Job Title</h6><p>Department</p></th>
                            <th>Hiring Manager</th>
                            <th>Date of Application</th>
                            <th>Status</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                            <td>01234</td>
                            <td><h6>Data Analytics</h6><p>Strategy</p></td>
                            <td>Tan Kim Seng</td>
                            <td>01/06/2021</td>
                            <td><label class="badge badge-danger">Rejected by Hiring Manager</label></td>
                            <td><button type="button" onclick="location.href = 'staff-application.php'" class="btn btn-primary">View Application</button></td>
                        </tr>
                        <tr>
                            <td>01234</td>
                            <td><h6>Sales Representative</h6><p>Sales</p></td>
                            <td>Melvin Ng</td>
                            <td>01/06/2021</td>
                            <td><label class="badge badge-success">Accepted</label></td>
                            <td><button type="button" onclick="location.href = 'staff-application.php'" class="btn btn-primary">View Application</button></td>
                        </tr>
                        <tr>
                            <td>01234</td>
                            <td><h6>Sales Support</h6><p>Sales</p></td>
                            <td>Melvin Ng</td>
                            <td>01/06/2021</td>
                            <td><label class="badge badge-danger">Rejected by Hiring Manager</label></td>
                            <td><button type="button" onclick="location.href = 'staff-application.php'" class="btn btn-primary">View Application</button></td>
                        </tr>
                        <tr>
                            <td>01234</td>
                            <td><h6>Cybersecurity Intern</h6><p>Security</p></td>
                            <td>Goh Jun Jie</td>
                            <td>01/06/2021</td>
                            <td><label class="badge badge-danger">Rejected by Staff</label></td>
                            <td><button type="button" onclick="location.href = 'staff-application.php'" class="btn btn-primary">View Application</button></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- end of main panel -->
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

