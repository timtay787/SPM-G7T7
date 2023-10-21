// remember to check role_listing_id/staff_id in session storage before testing
const app = Vue.createApp({
    data() {
        return {
            role_listing_id: sessionStorage.getItem('role_listing_id'),
            staff_id: sessionStorage.getItem('staff_id'),
            // role_listing_id: 3,
            // staff_id: 4,
            submission_error: false,
            reason_for_application : '',
            outcome: '',
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
    }
})

app.mount('#app')

// http://127.0.0.1:5004/role_application
// http://localhost:5004/role_application