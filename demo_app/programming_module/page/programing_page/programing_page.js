frappe.pages['programing-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Demo page',
		single_column: true
	});

	page.set_title('My Page')
	page.set_indicator('Done','green')

	let $btn = page.set_primary_action('New',()=>frappe.msgprint("Clicked New"))
	let $btn2 = page.set_secondary_action('Refresh',()=>frappe.msgprint("Clicked Refresh"))

	page.add_menu_item('Send Email',()=>frappe.msgprint("Clicked Send Email"))
	page.add_action_item('Delete',()=>frappe.msgprint("Clicked Delete"))

	let field = page.add_field({
		label:'Status',
		fieldtype: 'Select',
		fieldname: 'Status',
		options:[
			'Open',
			'Closed',
			'cancelled'
		],
		change(){
			frappe.msgprint(field.get_value());
		}
	});

	// $(frappe.render_template("programming_page", {})).appendTo(page.body);

	$(frappe.render_template("programing-page", {
		data:"rendering with data"
	})).appendTo(page.body);


}