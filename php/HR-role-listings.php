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
  
  <!-- Vue 3 -->
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script> 

  <!-- JQuery-->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

  <!-- SessionStorage-->
  <style>
      #myInput {
    background-image: url('/images/searchicon.png');
    background-size: 25px;
    background-position: 10px 10px;
    background-repeat: no-repeat;
    width: 100%;
    font-size: 16px;
    padding: 12px 20px 12px 40px;
    border: 1px solid #ddd;
    margin-bottom: 12px;
  }

  #category_select {
    color: darkslategray;
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  </style>
</head>

<body>
<div id="app">
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
<!-- MAIN PANEL -->
<div class="main-panel">
        <div class="content-wrapper">
          <div class="row">
          <!-- <h2 class="text-black fw-bold">Role Listings</h2> -->
          <td><button type="button" onclick="location.href = 'HR-add-new.php'" class="btn btn-primary">Add New</button></td>
          <h2> </h2>
          <h2 class="text-black fw-bold"> </h2>
          <div class="col-lg-12 grid-margin stretch-card">              
            <div class="card">
                <div class="card-body">
                  <div class="row">
                    <div class="col-md-6"><h4 class="card-title">Role Listings</h4></div>
                    <div class="col-md-6">
                    <div class = row>
                      <div class = col-md-4>
                        <h4 class="card-title" style="text-align: right">Search for:</h4>
                      </div>
                      <div class = col-md-2>
                        <select name="cars" id="category_select">
                        <option value="0">Job Title</option>
                        <option value="1">Department</option>
                        <option value="2">Hiring Manager</option>
                      </select>
                      </div>
                    </div>
                  </div>
                  </div>
                  <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names.." title="Type in a name">
                  <div class="table-responsive">
                    <table class="table table-hover">
                      <thead>
                        <tr>
                          <th><h6>Job Title</h6></th>
                          <th>Department</th>
                          <th>Hiring Manager</th>
                          <th>No. of Applications</th>
                          <th>Status</th>
                        </tr>
                      </thead>
                      <tbody id="myTable">
                        <tr v-for="info in role_listing_info">
                          <td><h6>{{info.role.RoleName}}</h6></td>
                          <td>{{info.hiring_manager.Department}}</td>
                          <td>{{info.hiring_manager.StaffFirstName}} {{info.hiring_manager.StaffLastName}}</td>
                          <td>{{info.no_of_applications}}</td>
                          <td><button type="button" v-bind:name="info.role_listing.RoleListingID" onclick="location.href = 'HR-role-listing-info.php'; sessionStorage.setItem('role_listing_id', name)" class="btn btn-outline-primary btn-fw">View</button></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
      </div>
      <!-- main panel ends here -->
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
  <script src="HR-role-listing.js"></script>

    <script>
    function myFunction() {
      var input, filter, table, tr, td, i, txtValue;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      table = document.getElementById("myTable");
      tr = table.getElementsByTagName("tr");
      category = document.getElementById("category_select").value;
      for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[category];
        if (td) {
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }       
      }
    }
  </script>

</body>

</html>



