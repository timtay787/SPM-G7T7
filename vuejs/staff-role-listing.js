const app = Vue.createApp({
    data() {
        return {
            //hardcoded staff_id for testing purposes
            is_hr: sessionStorage.getItem('is_hr'),
            staff_id: sessionStorage.getItem('staff_id'),
            //staff_id: 1,
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
            staff_match: [],
            staff: {},
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
            var serviceURL3 = 'http://localhost:5000/staff';
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

            //Get skills of staff
            var serviceURL4 = 'http://localhost:5000/staff/skillsofstaff/'+this.staff_id;
            try {
                const response4 =
                    await fetch(
                        serviceURL4, {method: 'GET'}
                    );
                const result4 = await response4.json();
                if (response4.status == 200){
                    var staff_skills = result4.data.staff_skills
                }
            }
            catch (error) {
                console.log('Error in processing the skills of staff.')
            }

            // Get skills for each role in role_listing
            console.log(JSON.stringify(this.role_listing.role_listing[0].RoleID))
            console.log(this.role_listing.role_listing.length)
            console.log(role_listing.role_listing)

            // HELP: the outer for loop won't loop, the inner one (skill match rate) okay
            for (var i=0; i<role_listing.role_listing.length; i++){
                console.log(i)
                var serviceURL5 = 'http://localhost:5001/role/skill/'+JSON.stringify(this.role_listing.role_listing[i].RoleID);
                try {
                    const response5 =
                        await fetch(
                            serviceURL5, {method: 'GET'}
                        );
                    const result5 = await response5.json();
                    if (response5.status == 200){
                        var skills = result5.data.role_skill
                    }
                }
                catch (error) {
                    console.log('Error in processing the request.')
                }
                console.log(skills)
                for (var j=0; j<skills.length; j++){
                    var skillid = skills[j].SkillID
                    console.log(skillid)
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
                
                //Get skill match rate
                var skill_match = 0
                for (var j=0; j<staff_skills.length; j++){
                    for (var k=0; k<this.skills.length; k++){
                        if (staff_skills[j].SkillID == this.skills[k].SkillID){
                            skill_match += 1
                        }
                    }
                }
                match_rate = Math.floor((skill_match / this.skills.length) * 100)
                console.log(match_rate)
                this.staff_match.push({'match_rate': match_rate})
                console.log(this.staff_match[0])
            }
        })
    },
})

app.mount('#app');