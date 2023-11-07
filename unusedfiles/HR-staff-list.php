<?php 
  // $name = $_SESSION['userid'];
  $name = 'HR123';
  $email = 'HR@gmail.com';
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
            <a class="nav-link" href="HR-staff-list.php" aria-expanded="false" aria-controls="form-elements">
              <i class="menu-icon mdi mdi-account-circle-outline"></i>
              <span class="menu-title">Staff Members</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="HR-role-listings.php" aria-expanded="false" aria-controls="form-elements">
              <i class="menu-icon mdi mdi-card-text-outline"></i>
              <span class="menu-title">Role Listings</span>
            </a>
          </li>
        </ul>
      </nav>
      
      <!-- MAIN PANEL -->
      <div class="main-panel">
        <div class="content-wrapper">
          <div class="row">
            <div class="col-lg-12 grid-margin stretch-card">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Staff List</h4>
                  <div class="table-responsive">
                    <table class="table table-striped">
                      <thead>
                        <tr>
                          <th>
                            Profile Picture
                          </th>
                          <th>
                            First Name
                          </th>
                          <th>
                            Last Name
                          </th>
                          <th>
                            Current Department
                          </th>
                          <th>
                            Country
                          </th>
                          <th></th>
                        </tr>
                      </thead>
<<<<<<< Updated upstream:HR-staff-list.php
                      <tbody>
                        <tr>
                          <td class="py-1"><img src="images/faces/face2.jpg" alt="image"/></td>
                          <td>Herman</td>
                          <td>Tan</td>
                          <td>Marketing</td>
                          <td>Singapore</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
                        </tr>
                        <tr>
                          <td class="py-1"><img src="images/faces/face3.jpg" alt="image"/></td>
                          <td>Mervyn</td>
                          <td>Yeo</td>
                          <td>IT</td>
                          <td>Singapore</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
                        </tr>
                        <tr>
                          <td class="py-1"><img src="images/faces/face4.jpg" alt="image"/></td>
                          <td>Alice</td>
                          <td>Ng</td>
                          <td>Sales</td>
                          <td>Singapore</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
                        </tr>
                        <tr>
                          <td class="py-1"><img src="images/faces/face5.jpg" alt="image"/></td>
                          <td>Max</td>
                          <td>Smith</td>
                          <td>Customer Support</td>
                          <td>Singapore</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
                        </tr>
                        <tr>
                          <td class="py-1"><img src="images/faces/face6.jpg" alt="image"/></td>
                          <td>Ethan</td>
                          <td>Murray</td>
                          <td>Marketing</td>
                          <td>USA</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
                        </tr>
                        <tr>
                          <td class="py-1"><img src="images/faces/face7.jpg" alt="image"/></td>
                          <td>Herman</td>
                          <td>Tan</td>
                          <td>Sales</td>
                          <td>Singapore</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
                        </tr>
                        <tr>
                          <td class="py-1"><img src="images/faces/face8.jpg" alt="image"/></td>
                          <td>Benjamin</td>
                          <td>Sim</td>
                          <td>IT</td>
                          <td>Singapore</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
                        </tr>
                        <tr>
                          <td class="py-1"><img src="images/faces/face9.jpg" alt="image"/></td>
                          <td>Anthony</td>
                          <td>Hartono</td>
                          <td>Sales</td>
                          <td>Indonesia</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
                        </tr>
                        <tr>
                          <td class="py-1"><img src="images/faces/face10.jpg" alt="image"/></td>
                          <td>Susan</td>
                          <td>Tan</td>
                          <td>Marketing</td>
                          <td>Malaysia</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
                        </tr>
                        <tr>
                          <td class="py-1"><img src="images/faces/face11.jpg" alt="image"/></td>
                          <td>Sok Boon</td>
                          <td>Lim</td>
                          <td>IT</td>
                          <td>Malaysia</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
                        </tr>
                        <tr>
                          <td class="py-1"><img src="images/faces/face12.jpg" alt="image"/></td>
                          <td>Jun Jie</td>
                          <td>Lee</td>
                          <td>Customer Support</td>
                          <td>Singapore</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
                        </tr>
                        <tr>
                          <td class="py-1"><img src="images/faces/face13.jpg" alt="image"/></td>
                          <td>Emily</td>
                          <td>Tan</td>
                          <td>Marketing</td>
                          <td>Singapore</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-success">View Profile</button></td>
=======
                      <tbody id="myTable">
                        <tr v-for="staff in staff_members">
                          <!-- <td class="py-1"><img src="images/faces/face2.jpg" alt="image"/></td> -->
                          <td>{{staff.StaffFirstName}} {{staff.StaffLastName}}</td>
                          <td>{{staff.Department}}</td>
                          <td>{{staff.Email}}</td>
                          <td>{{staff.BusinessAddress}}</td>
                          <td><button type="button" v-bind:name="staff.StaffID" onclick="location.href = 'HR-staff-profile.php'; sessionStorage.setItem('staff_lookup_id', name)" class="btn btn-success">View Profile</button></td>
>>>>>>> Stashed changes:php/HR-staff-list.php
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- content-wrapper ends -->
        <!-- partial:../../partials/_footer.html -->
        <footer class="footer">
          <div class="d-sm-flex justify-content-center justify-content-sm-between">
            <span class="text-muted text-center text-sm-left d-block d-sm-inline-block">Premium <a href="https://www.bootstrapdash.com/" target="_blank">Bootstrap admin template</a> from BootstrapDash.</span>
            <span class="float-none float-sm-right d-block mt-1 mt-sm-0 text-center">Copyright © 2021. All rights reserved.</span>
          </div>
        </footer>
        <!-- partial -->
      </div>
      <!-- main-panel ends -->
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

