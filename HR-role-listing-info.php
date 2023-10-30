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
      <div class="main-panel">          
        <div class="content-wrapper">
          <div class="row">

            <h1>{{role.role_name}}</h1>
            <h1> </h1>
            <button type="button" class="btn btn-primary">Edit Role Listing</button>
            <h1> </h1>
            <button type="button" class="btn btn-primary">Close Applications</button>
            <h1> </h1>
            <div class="col-md-8 grid-margin stretch-card">
              <div class="card">
                <div class="row">
                  <div class="col-md-4">
                    <div class="card-body">
                    <h4 class="card-title">General Information</h4>
                    <div class="template-demo d-flex justify-content-between flex-nowrap">
                      <img src="images/faces/socialmedia.png" style="border-radius: 100%; max-width: 100%; height: auto;">
                    </div>
                  </div>
                  </div> 
                  <div class="col-md-8">
                    <div class="card-body">
                      <h4 class="card-title">  </h4>
                      
                      <div class="table-responsive">
                        <table class="table">
                          <tr>
                            <th>Job Title</th>
                            <td>{{role.RoleName}}</td>
                          </tr>
                          <tr>
                            <th>Department</th>
                            <td>{{manager.Department}}</td>
                          </tr>
                          <tr>
                            <th>Job Location</th>
                            <td>{{manager.BusinessAddress}}</td>
                          </tr>
                          <tr>
                            <th>Post Date</th>
                            <td>{{open_date}}</td>
                          </tr>
                          <tr>
                            <th>Closing Date</th>
                            <td>{{close_date}}</td>
                          </tr>
                          <!-- <tr>
                            <th>Career Level</th>
                            <td>Entry</td>
                          </tr> -->
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-4 grid-margin stretch-card">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Hiring Manager</h4>
                  <img src="images/faces/face1.jpg" style="border-radius: 100%; max-width: 50%; height: auto;">
                  <div class="table-responsive">
                        <table class="table">
                          <tr>
                            <th>Name</th>
                            <td>{{manager.StaffFirstName}} {{manager.StaffLastName}}</td>
                          </tr>
                          <tr>
                            <th>Position</th>
                            <td>{{position.RoleName}}</td>
                          </tr>
                          <tr>
                            <th>Email</th>
                            <td>{{manager.Email}}</td>
                          </tr>
                        </table>
                      </div>
                  
                </div>
              </div>
            </div>
            <div class="col-md-12 grid-margin stretch-card">
              <div class="card">
                  <div class="card-body">
                    <h4>Description</h4>
                    <p>{{role_listing.RoleListingDescription}}</p>
                    </br>
                    <!-- <h4>Responsibilities</h4>
                    <ul>
                        <li>Develop and implement social media content strategies across platforms, including Facebook, Twitter, Instagram, LinkedIn, and more.</li>
                        <li>Create and curate engaging and shareable content, including text, images, videos, and infographics.</li>
                        <li>Monitor and respond to comments, messages, and mentions, maintaining a positive and interactive online presence.</li>
                        <li>Analyze social media metrics and track performance using tools like Google Analytics and social media management software.</li>
                        <li>Stay up-to-date with industry trends and best practices, adapting strategies accordingly.</li>
                        <li>Assist in creating and managing social media advertising campaigns.</li>
                        <li>Engage with influencers and develop partnerships for cross-promotion.</li>
                    </ul>
                    </br>
                    <h4>Requirements</h4>
                    <ul>
                        <li>Strong passion for and knowledge of social media platforms and trends.</li>
                        <li>Completion of Marketing LMS modules</li>
                        <li>Basic understanding of social media analytics and tools.</li>
                        <li>Creative mindset with the ability to generate engaging content.</li>
                        <li>Completion of Communication LMS modules</li>
                        <li>Strong team player with excellent collaboration skills.</li>
                    </ul>   
                    </br> -->
                    <h4>Skills</h4>
                    <div class="template-demo">
                        <button type="button" class="btn btn-outline-primary btn-fw"  v-for="skill of skills">{{skill.SkillName}}</button>
                    </div>
                </div>   
                </div>
              </div>
            </div>

            <div class="col-lg-12 grid-margin stretch-card">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Applicants</h4>
                  <div class="table-responsive">
                    <table class="table table-striped">
                      <thead>
                        <tr>
                          <!-- <th>
                            Profile Picture
                          </th> -->
                          <th>
                            First Name
                          </th>
                          <th>
                            Last Name
                          </th>
                          <th>
                            Email
                          </th>
                          <th>
                            Skills Match
                          </th>
                          <th>Application</th>
                          <!-- <th>Results</th> -->


                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="staff_application of staff_applications">
                          <!-- <td class="py-1"><img src="images/faces/face2.jpg" alt="image"/></td> -->
                          <td>{{staff_application.staff.StaffFirstName}}</td>
                          <td>{{staff_application.staff.StaffLastName}}</td>
                          <td>{{staff_application.staff.Email}}</td>
                          <td class="text-success">{{staff_application.match_rate}}%</td>
                          <td><button type="button" onclick="location.href = 'HR-staff-profile.php'" class="btn btn-primary">View Profile</button><p> </p><button type="button" onclick="location.href = 'HR-application.php'" class="btn btn-primary">View Application</button></td>
                          <!-- <td>
                            <div class="dropdown">
                                <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                                Pending
                                </button>
                                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                                    <a class="dropdown-item" href="#">Accept</a>
                                    <a class="dropdown-item" href="#">Reject</a>
                                </div>
                            </div>
                        </td> -->
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

  <script src="role_listing_info.js"></script>
</body>

</html>

