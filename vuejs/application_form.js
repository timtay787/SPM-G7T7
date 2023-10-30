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

                if (data['message'] == "Application created successfully.") {
                    this.outcome = 'Application submitted successfully, please check your applications page to verify its status.'
                }
            }
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
            
        })
    }
})

app.mount('#app')

// http://127.0.0.1:5004/role_application
// http://localhost:5004/role_application