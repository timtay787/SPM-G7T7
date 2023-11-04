// remember to check role_listing_id/staff_id in session storage before testing
const app = Vue.createApp({
    data() {
        return {
            is_hr: sessionStorage.getItem('is_hr'),
            role_listing_id: sessionStorage.getItem('role_listing_id'),
            staff_id: sessionStorage.getItem('staff_id'),
            applications: [],
            role_application: [],
            staff_skills: [],
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

            var serviceURL6 = 'http://localhost:5000/staff/skillsofstaff/'+this.staff_id;
            try {
                const response6 =
                    await fetch(
                        serviceURL6, {method: 'GET'}
                    );
                const result6 = await response6.json();
                if (response6.status == 200){
                    var staff_skills = result6.data.staff_skills
                    console.log(staff_skills)
                    this.staff_skills = staff_skills
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
                
                var serviceURL4 = 'http://localhost:5000/staff/'+role_listing.RoleListingSource;
                try {
                    const response4 =
                        await fetch(
                            serviceURL4, {method: 'GET'}
                        );
                    const result4 = await response4.json();
                    if (response4.status == 200){
                        var manager = result4.data
                        console.log(manager)
                        
                    }
                }
                catch (error) {
                    console.log('Error in processing the request.')
                }

                var serviceURL5 = 'http://localhost:5001/role/skill/'+role_listing.RoleID;
                try {
                    const response5 =
                        await fetch(
                            serviceURL5, {method: 'GET'}
                        );
                    const result5 = await response5.json();
                    if (response5.status == 200){
                        var skills = result5.data.role_skill
                        console.log(skills)
                    }
                }
                catch (error) {
                    console.log('Error in processing the request.')
                }

                var skill_match = 0
                for (var j=0; j<this.staff_skills.length; j++){
                    for (var k=0; k<skills.length; k++){
                        if (this.staff_skills[j].SkillID == skills[k].SkillID){
                            skill_match += 1
                        }
                    }
                }
                console.log(skill_match)
                if (skill_match == 0){
                    var skillsmatch = 0
                }
                else{
                    var skillsmatch = Math.floor((skill_match / skills.length) * 100) 
                }

                var Timestamp = new Date(this.applications[i].RoleApplicationTimestampCreate)
                var appDate = Timestamp.getDate() + '/' + (Timestamp.getMonth()+1) + '/' + Timestamp.getFullYear()

                this.role_application.push({'role': role, 'manager':manager, 'application': this.applications[i], 'date': appDate, 'skillsmatch': skillsmatch})
            }

        })
    },

})


app.mount('#app')
