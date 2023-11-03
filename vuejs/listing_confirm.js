// remember to check role_listing_id/staff_id in session storage before testing
const app = Vue.createApp({
    data() {
        return {
            is_hr: sessionStorage.getItem('is_hr'),
            staff_id: sessionStorage.getItem('staff_id'),
            role_listing_id: sessionStorage.getItem('role_listing_id'),
            role_listing: {},
            manager: {},
            create_date: '',
            update_date: '',
            role: {},
        }
    },

    methods: {
    },

    created(){
        $(async()=>{
            console.log(this.role_id)
            var serviceURL1 = 'http://localhost:5003/role_listing/' + this.role_listing_id;
            try {
                const response =
                    await fetch(
                        serviceURL1, {method: 'GET'}
                    );
                const result = await response.json();
                if (response.status == 200){
                    var role_listing = result.data
                    console.log(role_listing)
                    this.role_listing = role_listing
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
            var Timestamp = new Date(this.role_listing.RoleListingTimestampCreate)
            this.create_date = Timestamp.getDate() + '/' + (Timestamp.getMonth()+1) + '/' + Timestamp.getFullYear()
            if (this.role_listing.RoleListingTimestampUpdate != ''){
                var UTimestamp = new Date(this.role_listing.RoleListingTimestampUpdate)
                this.update_date = UTimestamp.getDate() + '/' + (UTimestamp.getMonth()+1) + '/' + UTimestamp.getFullYear()
            }

            var serviceURL2 = 'http://localhost:5000/staff/' + this.role_listing.RoleListingSource;
            try {
                const response2 =
                    await fetch(
                        serviceURL2, {method: 'GET'}
                    );
                const result2 = await response2.json();
                if (response2.status == 200){
                    var manager = result2.data
                    console.log(manager)
                    this.manager = manager
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }

            var serviceURL3 = 'http://localhost:5001/role/' + this.role_listing.RoleID;
            try {
                const response3 =
                    await fetch(
                        serviceURL3, {method: 'GET'}
                    );
                const result3 = await response3.json();
                if (response3.status == 200){
                    var role = result3.data
                    console.log(role)
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