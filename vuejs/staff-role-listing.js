const app = Vue.createApp({
    data() {
        return {
            //hardcoded staff_id for testing purposes
            is_hr: sessionStorage.getItem('is_hr'),
            staff_id: sessionStorage.getItem('staff_id'),
            role_listings: [],
            listing_info_list: [],
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
                    var role_listings = result.data.role_listing
                    console.log(role_listings)
                    this.role_listings = role_listings
                }
            }
            catch (error) {
                console.log('Error in getting role listings.')
            }

            // Get role info for each role listing
            for (var i=0; i<this.role_listings.length; i++){
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
                    console.log('Error in getting role info.')
                }

                // Get hiring manager info for each role listing
                var serviceURL3 = 'http://localhost:5000/staff/'+this.role_listings[i].RoleListingSource;
                try {
                    const response3 =
                        await fetch(
                            serviceURL3, {method: 'GET'}
                        );
                    const result3 = await response3.json();
                    if (response3.status == 200){
                        var manager = result3.data
                        console.log(manager)
                    }
                }
                catch (error) {
                    console.log('Error in getting hiring manager info.')
                }

                // Get skills for each role in role_listing
                var serviceURL4 = 'http://localhost:5001/role/skill/'+this.role_listings[i].RoleID;
                try {
                    const response4 =
                        await fetch(
                            serviceURL4, {method: 'GET'}
                        );
                    const result4 = await response4.json();
                    if (response4.status == 200){
                        var skills = result4.data.role_skill
                        console.log(skills)
                    }
                }
                catch (error) {
                    console.log('Error in getting skills for each role.')
                }

                //Get skills of staff
                var serviceURL5 = 'http://localhost:5000/staff/skillsofstaff/'+this.staff_id;
                try {
                    const response5 =
                        await fetch(
                            serviceURL5, {method: 'GET'}
                        );
                    const result5 = await response5.json();
                    if (response5.status == 200){
                        var staff_skills = result5.data.staff_skills
                        console.log(staff_skills)
                    }
                }
                catch (error) {
                    console.log('Error in processing the skills of staff.')
                }

                var skill_match = 0
                for (var j=0; j<staff_skills.length; j++){
                    for (var k=0; k<skills.length; k++){
                        if (staff_skills[j].SkillID == skills[k].SkillID){
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

                this.listing_info_list.push({'role_listing': this.role_listings[i],'role': role, 'manager': manager, 'skillsmatch': skillsmatch})
            }
        })
    },
})

app.mount('#app');