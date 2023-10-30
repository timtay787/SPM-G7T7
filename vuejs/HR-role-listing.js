// remember to check role_listing_id/staff_id in session storage before testing
const app = Vue.createApp({
    data() {
        return {
            is_hr: sessionStorage.getItem('is_hr'),
            staff_id: sessionStorage.getItem('staff_id'),
            role_listings: [], 
            role_listing_info: [],  
        }
    },

    methods: {
        
    },

    created(){
        $(async()=>{
            // Get role_listings
            var serviceURL1 = 'http://localhost:5003/role_listing';
            try {
                const response =
                    await fetch(
                        serviceURL1, {method: 'GET'}
                    );
                const result = await response.json();
                if (response.status == 200){
                    var role_listings = result.data.role_listing
                    this.role_listings = role_listings
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
            for (i=0; i<this.role_listings.length; i++){
                var serviceURL2 = 'http://localhost:5001/role/'+this.role_listings[i].RoleID;
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
                var serviceURL3 = 'http://localhost:5000/staff/'+this.role_listings[i].RoleListingSource;
                try {
                    const response3 =
                        await fetch(
                            serviceURL3, {method: 'GET'}
                        );
                    const result3 = await response3.json();
                    if (response3.status == 200){
                        var hiring_manager = result3.data
                        console.log(hiring_manager)
                    }
                }
                catch (error) {
                    console.log('Error in processing the request.')
                }
                var serviceURL4 = 'http://localhost:5004/role_application/listing/'+this.role_listings[i].RoleListingID;
                try {
                    const response4 =
                        await fetch(
                            serviceURL4, {method: 'GET'}
                        );
                    const result4 = await response4.json();
                    if (response4.status == 200){
                        var applications = result4.data.application
                        console.log(applications)
                    }
                }
                catch (error) {
                    console.log('Error in processing the request.')
                }
                var is_open = (new Date(this.role_listings[i].RoleListingClose)).getTime() > (new Date().getTime())
                this.role_listing_info.push({
                    'role_listing': this.role_listings[i],
                    'role': role,
                    'hiring_manager': hiring_manager,
                    'no_of_applications': applications.length,
                    'is_open': is_open,
                })
            }

        })
    },

})


app.mount('#app')
