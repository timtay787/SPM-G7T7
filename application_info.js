// remember to check role_listing_id/staff_id in session storage before testing
const app = Vue.createApp({
    data() {
        return {
            application_id: sessionStorage.getItem('application_id'),
            application: {},
            role_listing: {},
            role: {},
            hiring_manager: {},
            appdate: '',
        }
    },

    methods: {
        
    },

    created(){
        $(async()=>{
            // Get role application info
            var serviceURL1 = 'http://localhost:5004/role_application/'+this.application_id;
            try {
                const response =
                    await fetch(
                        serviceURL1, {method: 'GET'}
                    );
                const result = await response.json();
                if (response.status == 200){
                    var application = result.data
                    this.application = application
                    var appdate = new Date(this.application.RoleApplicationTimestampCreate)
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
            this.appdate = appdate.getDate() + '/' + (appdate.getMonth()+1) + '/' + appdate.getFullYear()

            // Get role listing info
            var serviceURL2 = 'http://localhost:5003/role_listing/'+this.application.RoleListingID;
            try {
                const response2 =
                    await fetch(
                        serviceURL2, {method: 'GET'}
                    );
                const result2 = await response2.json();
                if (response2.status == 200){
                    var role_listing = result2.data
                    this.role_listing = role_listing
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

            // Get role listing source info
            var serviceURL4 = 'http://localhost:5000/staff/'+this.role_listing.RoleListingSource;
            try {
                const response4 =
                    await fetch(
                        serviceURL4, {method: 'GET'}
                    );
                const result4 = await response4.json();
                if (response4.status == 200){
                    var hiring_manager = result4.data
                    this.hiring_manager = hiring_manager
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }

        })
    },

})


app.mount('#app')
