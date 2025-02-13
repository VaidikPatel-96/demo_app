// Copyright (c) 2025, D-codE and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client Side Scripting", {
	// refresh(frm) {
    //     // frappe.msgprint("Hello vaidik")
    //     frappe.throw("THis is an Error");



    //#####frappe EVENTS####### //
        
	// }
    // onload: function(frm){
    //     frappe.msgprint("hello D-code from 'onload' event")
    // }
    // validate: function(frm){
    //     frappe.throw ("Hello D-code from 'validate' event");
        
    // }
    // before_save: function(frm){
    //     frappe.throw ("Hello D-code from 'before_save' event");
        
    // }
    // after_save: function (frm) {
    //     frappe.throw("hello D-code from 'after_save'event")
    // },
    // enable: function(frm){
    //     frappe.msgprint("hello'enable' fieldname event")
    // },
    // age: function(frm){
    //     frappe.msgprint("hello 'age' fieldname event")
    // }

    // before_submit: function (frm) {
    //     frappe.throw ("hello 'before_submit' event");
        
    // },
    // on_submit: function (frm) {
    //     frappe.msgprint("hello 'on_submit'event")
    // },
    // before_cancel: function (frm) {
    //     frappe.throw("hello 'before_cancle'event")
    
    // },
    // after_cancel: function (frm) {
    //     frappe.msgprint("hello 'after_cancel'event")
    // },


//  #######    child table script      #####///

// frappe.ui.form.on('Family Members',{
//     name1:function(frm){
//         frappe.msgprint("hello child doctype 'name1' event")
//     }
    // age(frm,cdt,cdn){
    //     frappe.msgprint("hello 'age'child doctype fildname event")
    // }
// })


//  ####  value fetching  ### //

    // after_save: function (frm) {
    //     frappe.msgprint(__("The Full name is '{0}'",
    //              [frm.doc.firstname +" " + frm.doc.middlename+" "+frm.doc.lastname]))
    //     for (let row of frm.doc.family_members){
    //         frappe.msgprint(__("{0}.The family member name is '{1}'and relation is '{2}' ",
    //             [row.idx.row.name1,row.relation]))
    //     }         
    // }
        

//  ######## frm.set_intro & frm.is_new() ######/////  

    // refresh: function (frm) {
    //     // frm.set_intro('Now you can ctrate a new Client side scripting doctype')
    //     if(frm.is_new()){
    //         frm.set_intro('Now you can ctreate a new clint side scripting doctype')
    //     }
    // },


//  ######  frm.set_value  #####//// 

    // validate:function(frm) {
  
    //   frm.set_value('fullname',frm.doc.firstname+" " + frm.doc.middlename+" "+frm.doc.lastname)
    //     let row=frm.add_child("family_members",{
    //         name1:'vaidik',
    //         relation:'father',
    //         age:56
    //     })
    // },


////  #####events#### /////    

    // enable:function(frm){
    //         // frm.set_df_property('firstname','reqd',1)
    //         // // frm.refresh_field('firstname');

    //         // frm.set_df_property('middlename','read_only',1)
    //         // frm.refresh_field('middlename');

    //         // frm.toggle_reqd('age',true)
    // }


//// ####### Button  #####///////
    refresh: function (frm) {
        
    
        frm.add_custom_button('Click me Button',()=>{
            frappe.msgprint(__('You clicked me!!'));
        })

         frm.add_custom_button(__('CLick me1'), () => {
           frappe.msgprint(__('You Clicked 1 !!'));
        },'click me')

        frm.add_custom_button(__('CLick me2'), () => {
            frappe.msgprint(__('You Clicked 2 !!'));
         },'click me')

    },    
});