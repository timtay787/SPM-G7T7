const app = Vue.createApp({
    data() {
        return {
            role_listing_id: 4,
            role_id: null,
            role_listing_desc: '',
            role_listing_source: null,
            role_listing_open: null,
            role_listing_close: null,
            role_listing_creator: null,
            role_listing_updater: null,

            roles : [],
            managers : [],
            current_date : new Date().toISOString().slice(0, 10),
            submission_error: false,
            outcome: '',
        }
    },

    methods: {
        async createlisting() {
            if (this.submission_error==false){
                create_role_listing = {
                    "role_listing_id" : this.role_listing_id,
                    "role_id" : this.role_id,
                    "role_listing_desc" : this.role_listing_desc,
                    "role_listing_source" : this.role_listing_source,
                    "role_listing_open" : this.role_listing_open,
                    "role_listing_close" : this.role_listing_close,
                    "role_listing_creator" : sessionStorage.getItem('staff_id'),
                    
                }
                console.log(create_role_listing)
                const result = await fetch('http://127.0.0.1:5003/role_listing', {
                    method: 'POST',
                    body: JSON.stringify(create_role_listing),
                    headers: {
                        'Content-Type': 'application/json'
                    },
                })
                const data = await result.json()
                console.log(data)

                if (data['message'] == "Role Listing created successfully") {
                    this.outcome = 'Role listing created successfully. Please verify the listing in the Role Listing page.'
                }
            }
        }
    },

    created(){
        $(async()=>{
            console.log(this.role_id)
            var serviceURL1 = 'http://localhost:5001/role';

            try {
                const response =
                    await fetch(
                        serviceURL1, {method: 'GET'}
                    );
                const result = await response.json();
                if (response.status == 200){
                    var roles = result.data.role
                    console.log(roles)
                    this.roles = roles
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
        })

        $(async()=>{
            var serviceURL2 = 'http://localhost:5000/staff/manager';

            try {
                const response2 =
                    await fetch(
                        serviceURL2, {method: 'GET'}
                    );
                const result2 = await response2.json();
                if (response2.status == 200){
                    var managers = result2.data.staff
                    console.log(managers)
                    this.managers = managers
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
        })
    }

})

app.mount('#app')

// http://127.0.0.1:5003/role_listing
// http://localhost:5003/role_listing