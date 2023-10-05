const app = vue.createApp({
    data() {
        return {
            // role_listing_id: '',
            // staff_id: '',
            submission_error: false,
            submission_message : '',
            outcome: '',
        }
    },

    methods: {
        async submitapplication() {
            if (this.submission_error==false){
                create_application = {
                    "Data" : {
                        "role_listing_id" : sessionStorage.getItem('role_listing_id'),
                        "staff_id" : sessionStorage.getItem('staff_id')
                    }
                }
                console.log(create_application)
                const response = await fetch('http://localhost:5004/role_application', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(create_application)
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