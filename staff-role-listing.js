const app = Vue.createApp({
    data() {
        return {
            //role_listing_id: sessionStorage.getItem('role_listing_id'),
            role_id: 0,
            role_listing: {},
            applications: [],
            role: {},
            role_listing_source: 0,
            manager: {},
            role_listing_open: '',
            role_listing_close: '',
            open_date: '',
            close_date: '',
            skills: [],
            position: {},
            staff_applications: [],
        }
    },
    methods: {

    },

    created(){
        $(async()=>{
            // Get role listings
            var serviceURL1 = 'http://localhost:5003/role_listing';
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
                    this.role_id = role_listing.RoleID // might be an issue
                    this.role_listing_source = role_listing.RoleListingSource
                    this.role_listing_open = new Date(role_listing.RoleListingOpen)
                    this.open_date = this.role_listing_open.getDate() + '/' + (this.role_listing_open.getMonth()+1) + '/' + this.role_listing_open.getFullYear()
                    this.role_listing_close = new Date(role_listing.RoleListingClose)
                    this.close_date = this.role_listing_close.getDate() + '/' + (this.role_listing_close.getMonth()+1) + '/' + this.role_listing_close.getFullYear()
                }
            }
            catch (error) {
                console.log('Error in get role listings.')
            }

            // Get role info
            console.log(this.role)
            var serviceURL2 = 'http://localhost:5001/role';
            try {
                const response2 =
                    await fetch(
                        serviceURL2, {method: 'GET'}
                    );
                const result2 = await response2.json();
                if (response2.status == 200){
                    var role = result2.data
                    console.log(role)
                    this.role = role
                }
            }
            catch (error) {
                console.log('Error in get role info.')
            }
            
            // Get hiring manager info
            console.log(this.staff)
            var serviceURL3 = 'http://localhost:5000/staff/'+this.role_listing_source;
            try {
                const response3 =
                    await fetch(
                        serviceURL3, {method: 'GET'}
                    );
                const result3 = await response3.json();
                if (response3.status == 200){
                    var staff = result3.data
                    console.log(staff)
                    this.manager = staff
                }
            }
            catch (error) {
                console.log('Error in get hiring manager info.')
            }

            //Get skills match
        })
    },
})

app.mount('#app');