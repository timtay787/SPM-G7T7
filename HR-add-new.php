<?php 
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
  <script src="setSessionStorage.js"></script>


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

      <div class="col-md-12 grid-margin stretch-card">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Add New Role Listing</h4>
                  <form id="role_listing" class="forms-sample">

                    <div class="form-group">
                      <label for="role_id">Select the role you wish to recruit for:</label>
                      <select class="form-control" form="role_listing" id="role_id" name="role_id" list="roles" v-model="role_id">
                        <option v-for="role of roles" v-bind:value="role.RoleID" v-bind:selected="role_id===role.RoleID">{{role.RoleName}}</option>
                      </select>
                    </div>

                    <div class="form-group">
                      <label for="role_listing_desc">Please enter a brief description of this role:</label>
                      <input type="text" class="form-control" id="role_listing_desc" v-model="role_listing_desc">
                    </div>
                    
                    <div class="form-group">
                      <label for="role_listing_source">Who is the manager/director of this role?</label>
                      <select class="form-control" form="role_listing" id="role_listing_source" name="role_listing_source" v-model="role_listing_source">
                        <option v-for="manager of managers" v-bind:value="manager.StaffID"  v-bind:selected="role_listing_source===manager.StaffID">{{manager.StaffFirstName}} {{manager.StaffLastName}}, {{manager.Department}}</option>
                      </select>
                    </div>
                    <div class="form-group">
                      <label for="role_listing_open">When should this role listing open?</label>
                      <input type="date" v-bind:min="current_date" class="form-control" id="role_listing_open" v-model="role_listing_open">
                    </div>
                    <div class="form-group">
                      <label for="role_listing_close">When should this role listing close?</label>
                      <input type="date" v-bind:min="role_listing_open" class="form-control" id="role_listing_close" v-model="role_listing_close">
                    </div>
                    <!-- <div class="form-check form-check-flat form-check-primary">
                      <label class="form-check-label">
                        <input type="checkbox" class="form-check-input">
                        I confirm that all the information above are true to the best of my ability.
                      </label>
                    </div> -->
                    <button type="submit" class="btn btn-primary me-2" @click="createlisting()">Confirm</button>
                    <button class="btn btn-light">Cancel</button>
                  </form>
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

  <script src="role_listing_form.js"></script>  
</body>

</html>

