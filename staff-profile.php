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

            <div class="col-md-8 grid-margin stretch-card">
              <div class="card">
                <div class="row">
                  <div class="col-md-4">
                    <div class="card-body">
                    <h4 class="card-title">General Information</h4>
                    <div class="template-demo d-flex justify-content-between flex-nowrap">
                      <img src="images/faces/profile.png" style="border-radius: 100%; max-width: 100%; height: auto;">
                    </div>
                  </div>
                  </div> 
                  <div class="col-md-8">
                    <div class="card-body">
                      <h4 class="card-title">  </h4>
                      
                      <div class="table-responsive">
                        <table class="table">
                          <tr>
                            <th>First Name</th>
                            <td>Megan</td>
                          </tr>
                          <tr>
                            <th>Last Name</th>
                            <td>Tan</td>
                          </tr>
                          <tr>
                            <th>Current Department</th>
                            <td>IT</td>
                          </tr>
                          <tr>
                            <th>Country</th>
                            <td>Malaysia</td>
                          </tr>
                          <tr>
                            <th>Email Address</th>
                            <td>megantan@gmail.com</td>
                          </tr>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
                <div class = "row">
                  <div class="col-md-12">
                    <div class="card-body">
                      <h6> About Me </h4>
                      <p>Hi, I'm Megan, and I'm currently an IT analyst with over 8 years of professional experience in the tech industry. During my career, I've had the privilege of working on a wide range of IT projects, honing my skills in data analysis, system optimization, and problem-solving. Beyond my work in the IT world, I've developed a personal passion for social media analytics. In my free time, I've delved deep into the intricacies of tracking online trends, audience engagement, and content performance across various social media platforms. This journey has sparked a desire within me to pivot and explore new horizons within the digital landscape.</p>
                      <br>
                      <button type="button" class="btn btn-outline-primary btn-fw">Edit</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-md-4 grid-margin stretch-card">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Skills</h4>

                  <div class="template-demo">
                        <button type="button" class="btn btn-outline-primary btn-fw">Word</button>
                        <button type="button" class="btn btn-outline-primary btn-fw">Powerpoint</button>
                        <button type="button" class="btn btn-outline-primary btn-fw">Excel</button>
                        <button type="button" class="btn btn-outline-primary btn-fw">Marketing</button>
                        <button type="button" class="btn btn-outline-primary btn-fw">Content Creation</button>
                        <button type="button" class="btn btn-outline-primary btn-fw">Social Media</button>
                        <button type="button" class="btn btn-outline-primary btn-fw">Sales</button>
                        <button type="button" class="btn btn-outline-primary btn-fw">Communication</button>
                      </div>
                </div>
              </div>
            </div>
            <div class="col-12 grid-margin stretch-card">
              <div class="card">
                  <div class="card-body">
                    <h4 class="card-title">Learning Management System History</h4>
                    <div class="table-responsive">
                    <table class="table">
                      <thead>
                        <tr>
                          <th>Course Code</th>
                          <th>Course Name</th>
                          <th>Skills</th>
                          <th>Date Started</th>
                          <th>Status</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>MK135</td>
                          <td>Marketing Essentials</td>
                          <td>Marketing, Social Media</td>
                          <td>10/06/2022</td>
                          <td><label class="badge badge-success">Completed</label></td>
                        </tr>
                        <tr>
                          <td>SD101</td>
                          <td>Introduction to Software Development</td>
                          <td>Python, CSS</td>
                          <td>04/06/2022</td>
                          <td><label class="badge badge-warning">In Progress</label></td>
                        </tr>
                        <tr>
                          <td>MK134</td>
                          <td>Social Media Analytics</td>
                          <td>Analytics, Social Media</td>
                          <td>01/06/2022</td>
                          <td><label class="badge badge-success">Completed</label></td>
                        </tr>
                        <tr>
                          <td>COMMS202</td>
                          <td>Communication Skills</td>
                          <td>Communication</td>
                          <td>10/05/2022</td>
                          <td><label class="badge badge-success">Completed</label></td>
                        </tr>
                        <tr>
                          <td>CYS101</td>
                          <td>Introduction to Cybersecurity</td>
                          <td>Cybersecurity, Python</td>
                          <td>10/10/2021</td>
                          <td><label class="badge badge-warning">In Progress</label></td>
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
        </div>
      </div>
      <!-- main panel ends here -->
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

