// Copyright (c) 2025, D-codE and contributors
// For license information, please see license.txt

frappe.ui.form.on("practice_1", {
// //   refresh(frm) {
//         // Refresh logic here
//     // },
//     //     validate: function(frm){
//     //     frappe.throw ("Hello D-code from 'validate' event");

//     // }


    validate:function(frm){
  
        let row=frm.add_child("details",{
            email:'devendrabhai@gmail.com',
            mobile_no: 1234567890 
        });
      }
  
});
