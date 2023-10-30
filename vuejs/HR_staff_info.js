// remember to check role_listing_id/staff_id in session storage before testing
const app = Vue.createApp({
    data() {
        return {
            is_hr: sessionStorage.getItem('is_hr'),
            staff_id: sessionStorage.getItem('staff_id'),
            lookup_id : sessionStorage.getItem('staff_lookup_id'),
            staff: {},
            manager: {},
            p_role: {},
            s_roles: [],
            active_skills : [],
            inactive_skills : []      
        }
    },

    methods: {

        
    },

    created(){
        $(async()=>{
            // Get staff info
            var serviceURL1 = 'http://localhost:5000/staff/'+this.lookup_id;
            try {
                const response =
                    await fetch(
                        serviceURL1, {method: 'GET'}
                    );
                const result = await response.json();
                if (response.status == 200){
                    var staff = result.data
                    this.staff = staff
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }

            // Get manager info
            var serviceURL2 = 'http://localhost:5000/staff/officerofstaff/'+this.lookup_id;
            try {
                const response2 =
                    await fetch(
                        serviceURL2, {method: 'GET'}
                    );
                const result2 = await response2.json();
                if (response2.status == 200){
                    var manager = result2.data
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
            var serviceURL9 = 'http://localhost:5000/staff/'+manager.StaffID;
            try {
                const response9 =
                    await fetch(
                        serviceURL9, {method: 'GET'}
                    );
                const result9 = await response9.json();
                if (response9.status == 200){
                    var manager_info = result9.data
                    this.manager = manager_info
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }


            // Get primary role info
            var serviceURL3 = 'http://localhost:5000/staff/p_role/'+this.lookup_id;
            try {
                const response3 =
                    await fetch(
                        serviceURL3, {method: 'GET'}
                    );
                const result3 = await response3.json();
                if (response3.status == 200){
                    var p_role = result3.data.RoleID
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
            var serviceURL4 = 'http://localhost:5001/role/'+p_role;
            try {
                const response4 =
                    await fetch(
                        serviceURL4, {method: 'GET'}
                    );
                const result4 = await response4.json();
                if (response4.status == 200){
                    var p_role = result4.data
                    this.p_role = p_role
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }

            // Get secondary role info
            var serviceURL5 = 'http://localhost:5000/staff/role/'+this.lookup_id;
            try {
                const response5 =
                    await fetch(
                        serviceURL5, {method: 'GET'}
                    );
                const result5 = await response5.json();
                if (response5.status == 200){
                    var roles = result5.data.staff_roles
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
            for (i=0; i<roles.length; i++){
                if (roles[i].RoleType == 'secondary'){
                    var serviceURL6 = 'http://localhost:5001/role/'+roles[i].RoleID;
                    try {
                        const response6 =
                            await fetch(
                                serviceURL6, {method: 'GET'}
                            );
                        const result6 = await response6.json();
                        if (response6.status == 200){
                            var s_role = result6.data
                            this.s_roles.push(s_role)
                        }
                    }
                    catch (error) {
                        console.log('Error in processing the request.')
                    }
                }
            }

            // Get staff skills
            var serviceURL7 = 'http://localhost:5000/staff/skillsofstaff/'+this.lookup_id;
            try {
                const response7 =
                    await fetch(
                        serviceURL7, {method: 'GET'}
                    );
                const result7 = await response7.json();
                if (response7.status == 200){
                    var skills = result7.data.staff_skills
                    console.log(skills)
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
            for (i=0; i<skills.length; i++){
                var serviceURL8 = 'http://localhost:5002/skill/anystatus/'+skills[i].SkillID;
                try {
                    const response8 =
                        await fetch(
                            serviceURL8, {method: 'GET'}
                        );
                    const result8 = await response8.json();
                    if (response8.status == 200){
                        var skill = result8.data
                        if (skills[i].Status == 'active'){
                            this.active_skills.push(skill)
                        }
                        else{
                            this.inactive_skills.push(skill)
                        }
                    }
                }
                catch (error) {
                    console.log('Error in processing the request.')
                }
            }

        })
    },

})


app.mount('#app')
