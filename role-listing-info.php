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

            <h1>Social Media Manager</h1>
            <h1></h1>
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
                            <td>Social Media Manager</td>
                          </tr>
                          <tr>
                            <th>Department</th>
                            <td>Marketing</td>
                          </tr>
                          <tr>
                            <th>Country</th>
                            <td>Singapore</td>
                          </tr>
                          <tr>
                            <th>Post Date</th>
                            <td>19/06/2023</td>
                          </tr>
                          <tr>
                            <th>Career Level</th>
                            <td>Entry</td>
                          </tr>
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
                            <td>Jack Sock</td>
                          </tr>
                          <tr>
                            <th>Position</th>
                            <td>Head of Marketing</td>
                          </tr>
                          <tr>
                            <th>Email</th>
                            <td>jacksock@allinone.com</td>
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
                    <p>We're seeking a passionate and creative individual to join our team as an Entry-Level Social Media Manager. If you're excited about harnessing the power of social media to engage audiences, drive brand awareness, and contribute to meaningful causes, this is the perfect opportunity for you to kick-start your career.</p>
                    </br>
                    <h4>Responsibilities</h4>
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
                    </br>
                    <h4>Skills</h4>
                    <div class="template-demo">
                        <button type="button" class="btn btn-outline-primary btn-fw">Communication</button>
                        <button type="button" class="btn btn-outline-primary btn-fw">Marketing</button>
                        <button type="button" class="btn btn-outline-primary btn-fw">Content Creation</button>
                        <button type="button" class="btn btn-outline-primary btn-fw">Social Media</button>
                    </div>
                </div>   
                </div>
              </div>
            </div>

            <div>
                <h2>Skills Match : </h2>
                <h2 class="text-success">80%</h2>
                <button type="button" class="btn btn-primary" onclick="location.href = 'role-listing-applicationform.php'">Apply Now</button>
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

