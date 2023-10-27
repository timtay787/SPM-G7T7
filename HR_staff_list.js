const app = Vue.createApp({
    data() {
        return {
            staff_members: [],
        }
    },

    methods: {
        
    },

    created(){
        $(async()=>{
            // Get all staff members
            var serviceURL1 = 'http://localhost:5000/staff';
            try {
                const response =
                    await fetch(
                        serviceURL1, {method: 'GET'}
                    );
                const result = await response.json();
                if (response.status == 200){
                    var staff_members = result.data.staff
                    this.staff_members = staff_members
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }

        })
    },

})


app.mount('#app')
