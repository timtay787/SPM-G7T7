// remember to check role_listing_id/staff_id in session storage before testing
const app = Vue.createApp({
    data() {
        return {
            is_hr: sessionStorage.getItem('is_hr'),
            role_listing_id: sessionStorage.getItem('role_listing_id'),
            staff_id: sessionStorage.getItem('staff_id'),
            role_id: 0,
            role_listing: {},
            role: {},
            role_listing_source: 0,
            manager: {},
            role_listing_open: '',
            role_listing_close: '',
            open_date: '',
            close_date: '',
            skills: [],
            position: {},
            skillsmatch: 0,
      
        }
    },

    methods: {
        
    },

    created(){
        $(async()=>{
            // Get role listing info
            var serviceURL1 = 'http://localhost:5003/role_listing/'+this.role_listing_id;
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
                console.log('Error in processing the request.')
            }

            // Get role info
            console.log(this.role)
            var serviceURL3 = 'http://localhost:5001/role/'+this.role_id;
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

            // Get hiring manager info
            console.log(this.staff)
            var serviceURL4 = 'http://localhost:5000/staff/'+this.role_listing_source;
            try {
                const response4 =
                    await fetch(
                        serviceURL4, {method: 'GET'}
                    );
                const result4 = await response4.json();
                if (response4.status == 200){
                    var staff = result4.data
                    console.log(staff)
                    this.manager = staff
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
            
            // Get skills for role
            var serviceURL5 = 'http://localhost:5001/role/skill/'+this.role_id;
            try {
                const response5 =
                    await fetch(
                        serviceURL5, {method: 'GET'}
                    );
                const result5 = await response5.json();
                if (response5.status == 200){
                    var skills = result5.data.role_skill
                    for (var i=0; i<skills.length; i++){
                        var skillid = skills[i].SkillID
                        var serviceURL6 = 'http://localhost:5002/skill/'+skillid;
                        try {
                            const response6 =
                                await fetch(
                                    serviceURL6, {method: 'GET'}
                                );
                            const result6 = await response6.json();
                            if (response6.status == 200){
                                var skill = result6.data
                                this.skills.push(skill)
                            }
                        }
                        catch (error) {
                            console.log('Error in processing the request.')
                        }
                    }
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }

            // Get position of hiring manager
            var serviceURL7 = 'http://localhost:5000/staff/p_role/'+this.role_listing_source;
            try {
                const response7 =
                    await fetch(
                        serviceURL7, {method: 'GET'}
                    );
                const result7 = await response7.json();
                if (response7.status == 200){
                    var p_role = result7.data.RoleID
                    console.log(p_role)
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
            var serviceURL8 = 'http://localhost:5001/role/'+p_role;
            try {
                const response8 =
                    await fetch(
                        serviceURL8, {method: 'GET'}
                    );
                const result8 = await response8.json();
                if (response8.status == 200){
                    var position = result8.data
                    this.position = position
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }


            // Get skill match for staff members
            var serviceURL11 = 'http://localhost:5000/staff/skillsofstaff/'+this.staff_id;
            try {
                const response11 =
                    await fetch(
                        serviceURL11, {method: 'GET'}
                    );
                const result11 = await response11.json();
                if (response11.status == 200){
                    var staff_skills = result11.data.staff_skills
                }
            }
            catch (error) {
                console.log('Error in processing the request.')
            }
            var skill_match = 0
            for (var j=0; j<staff_skills.length; j++){
                for (var k=0; k<this.skills.length; k++){
                    if (staff_skills[j].SkillID == this.skills[k].SkillID){
                        skill_match += 1
                    }
                }
            }
            console.log(skill_match)
            if (skill_match == 0){
                this.skillsmatch = 0
            }
            else{
                this.skillsmatch = Math.floor((skill_match / this.skills.length) * 100) 
            }

        })
    },

    computed:{
        is_open(){
            return (new Date(this.role_listing.RoleListingClose)).getTime() > (new Date().getTime())
        }
    }

})


app.mount('#app')
