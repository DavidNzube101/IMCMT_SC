function askToSubmit(title, body) {
	hm_modal = document.querySelector("#modal-menu")
	hm_modal.style.display = "block"


	document.querySelector(".finish-add-to-record").style.display = "block"
	document.querySelector(".status-text").innerHTML = ""

	document.querySelector(".modal-title").innerHTML = title
	document.querySelector(".modal-data").innerHTML = `${body}<br> <b>Name:</b> ${document.querySelector("#record_name").value} <br> <b>Amount:</b> ${document.querySelector("#record_amount").value} <br> <b>For:</b> ${document.querySelector("#record_for").value} <br> <b>Money is Where:</b> ${document.querySelector("#record_where").value} <br> <b>Description:</b> ${document.querySelector("#record_description").value}`

	if (document.querySelector("#record_name").value == "" | document.querySelector("#record_amount").value == "") {
		document.querySelector(".finish-add-to-record").style.display = "none"
		document.querySelector(".status-text").innerHTML = "Name or Amount cannot be empty"
	}

	close_hm_modal = document.querySelector("#closemodal-menuBtn")
	close_hm_modal.addEventListener("click", ()=>{
		hm_modal.style.display = 'none'
	})
}

function submitData(url){
	def_url = '/add-to-record'
	document.querySelector(".add-record").innerHTML = "Adding to Record"
	document.querySelector(".add-record").style.opacity = "0.4"

	if (url == "/add-to-record") {

		from_screen = document.querySelector("#screen_id").value
		record_name = document.querySelector("#record_name").value
		record_amount = document.querySelector("#record_amount").value
		record_for = document.querySelector("#record_for").value
		record_where = document.querySelector("#record_where").value
		record_description = document.querySelector("#record_description").value

		fetch (url, {
			method: 'POST',
			body: JSON.stringify({ name: record_name, amount: record_amount, _for: record_for, where: record_where, description: record_description, screen: from_screen }),
		}).then((_res) => {
			window.location.href = '/dashboard'
		})
	}

	document.querySelector("#modal-menu").style.display = 'none'	
}