// remember to check role_listing_id/staff_id in session storage before testing
const app = Vue.createApp({
    data() {
        return {
            is_hr: sessionStorage.getItem('is_hr'),
            role_listing_id: sessionStorage.getItem('role_listing_id'),
            staff_id: sessionStorage.getItem('staff_id'),
            applications: [],
            role_application: [],
        }
    },

    methods: {
        
    },

    created(){
        $(async()=>{
            // Get role application info
            var serviceURL1 = 'http://localhost:5004/role_application/staff/'+this.staff_id;
            try {
                const response =
                    await fetch(
                        serviceURL1, {method: 'GET'}
                    );
                const result = await response.json();
                if (response.status == 200){
                    var applications = result.data.application
                    console.log(applications)
                    this.applications = applications
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }


            // Get multiple role info from single application
            for(var i = 0; i < this.applications.length; i++){
                var serviceURL3 = 'http://localhost:5003/role_listing/'+this.applications[i].RoleListingID;
                try {
                    const response3 =
                        await fetch(
                            serviceURL3, {method: 'GET'}
                        );
                    const result3 = await response3.json();
                    if (response3.status == 200){
                        var role_listing = result3.data
                        console.log(role_listing)
                    }
                }
                catch (error) {
                    console.log('Error in processing the request.')
                }


                var serviceURL2 = 'http://localhost:5001/role/'+role_listing.RoleID;
                try {
                    const response2 =
                        await fetch(
                            serviceURL2, {method: 'GET'}
                        );
                    const result2 = await response2.json();
                    if (response2.status == 200){
                        var role = result2.data
                        console.log(role)
                        
                    }
                }
                catch (error) {
                    console.log('Error in processing the request.')
                }
                var Timestamp = new Date(this.applications[i].RoleApplicationTimestampCreate)
                var appDate = Timestamp.getDate() + '/' + (Timestamp.getMonth()+1) + '/' + Timestamp.getFullYear()

                this.role_application.push({'role': role, 'application': this.applications[i], 'date': appDate})
            }
            console.log(role_application)

        })
    },

})


app.mount('#app')
