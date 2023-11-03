// remember to check role_listing_id/staff_id in session storage before testing
const app = Vue.createApp({
    data() {
        return {
            is_hr: sessionStorage.getItem('is_hr'),
            role_listing_id: sessionStorage.getItem('role_listing_id'),
            staff_id: sessionStorage.getItem('staff_id'),
            // role_listing_id: 3,
            // staff_id: 4,
            submission_error: false,
            reason_for_application : '',
            outcome: '',
            role_listing: {},
            role: {},
            hiring_manager: {},
            application: {},
            appDate: '',
        }
    },

    methods: {
        async submitapplication() {
            if (this.submission_error==false){
                create_application = {
                    "role_listing_id" : this.role_listing_id,
                    "staff_id" : this.staff_id,
                    "reason_for_application" : this.reason_for_application
                    
                }
                console.log(create_application)
                const response = await fetch('http://127.0.0.1:5004/role_application', {
                    method: 'POST',
                    body: JSON.stringify(create_application),
                    headers: {
                        'Content-Type': 'application/json'
                    },
                })
                const data = await response.json()
                console.log(data)

                if (response.status == 201) {
                    this.outcome = 'Application submitted successfully, please check your applications page to verify its status.'
                    this.submission_error = false
                    window.location.href = 'staff-application-success.html'
                }
                else {
                    this.outcome = 'Application submission failed, please try again.'
                    this.submission_error = true
                }
            }

            return false
        }
    },
    created(){
        $(async()=>{
            // Get role listing info
            var serviceURL1 = 'http://localhost:5003/role_listing/'+this.role_listing_id;
            try {
                const response1 =
                    await fetch(
                        serviceURL1, {method: 'GET'}
                    );
                const result1 = await response1.json();
                if (response1.status == 200){
                    var role_listing = result1.data
                    this.role_listing = role_listing
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }

            // Get role listing source info
            var serviceURL2 = 'http://localhost:5000/staff/'+this.role_listing.RoleListingSource;
            try {
                const response2 =
                    await fetch(
                        serviceURL2, {method: 'GET'}
                    );
                const result2 = await response2.json();
                if (response2.status == 200){
                    var hiring_manager = result2.data
                    this.hiring_manager = hiring_manager
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }

            // Get role info  
            var serviceURL3 = 'http://localhost:5001/role/'+this.role_listing.RoleID;
            try {
                const response3 =
                    await fetch(
                        serviceURL3, {method: 'GET'}
                    );
                const result3 = await response3.json();
                if (response3.status == 200){
                    var role = result3.data
                    this.role = role
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            } 

            // Check if staff member has already applied for this role
            var serviceURL4 = 'http://localhost:5004/role_application/staff/'+this.staff_id;
            try {
                const response4 =
                    await fetch(
                        serviceURL4, {method: 'GET'}
                    );
                const result4 = await response4.json();
                if (response4.status == 200){
                    var role_applications = result4.data.application
                    for (var i=0; i<role_applications.length; i++){
                        if (role_applications[i].RoleListingID == this.role_listing_id){
                            this.outcome = 'You have already applied for this role.'
                            this.submission_error = true
                            this.application = role_applications[i]
                        }
                    }
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
            if (this.application != ''){
                var Timestamp = new Date(this.application.RoleApplicationTimestampCreate)
                this.appDate = Timestamp.getDate() + '/' + (Timestamp.getMonth()+1) + '/' + Timestamp.getFullYear()
            }
            
        })
    }
})

app.mount('#app')

// http://127.0.0.1:5004/role_application
// http://localhost:5004/role_application