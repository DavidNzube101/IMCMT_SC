console.log(`[INFO]: Loaded page to screen ${current_screen}`)

// ScreenElement, ScreenID 

main_screen = [document.querySelector("#main-screen"), 1]
collection_screen = [document.querySelector("#collection-screen"), 2]
profile_screen = [document.querySelector("#profile-screen"), 3]
yearR_screen = [document.querySelector("#year-report"), 4]

// Trigger's
main_trigger = document.querySelector("#home-trigger")
collection_trigger = document.querySelector("#collection-trigger")
profile_trigger = document.querySelector("#profile-trigger")
yearR_trigger = document.querySelector("#year-trigger")

window.addEventListener('load', ()=>{
	// window.location.href = `/dashboard/${current_screen}`
	switch (current_screen) {
		case 2:
			main_screen[0].style.display = 'none'
			collection_screen[0].style.display = 'block'
			profile_screen[0].style.display = 'none'
			yearR_screen[0].style.display = 'none'
			current_screen = 2
			break;

		case 3:
			main_screen[0].style.display = 'none'
			collection_screen[0].style.display = 'none'
			profile_screen[0].style.display = 'block'
			yearR_screen[0].style.display = 'none'
			current_screen = 3
			break;

		case 4:
			main_screen[0].style.display = 'none'
			collection_screen[0].style.display = 'none'
			profile_screen[0].style.display = 'none'
			yearR_screen[0].style.display = 'block'
			current_screen = 4
			break;

		default:
			main_screen[0].style.display = 'block'
			collection_screen[0].style.display = 'none'
			profile_screen[0].style.display = 'none'
			yearR_screen[0].style.display = 'none'
	}

})

main_trigger.addEventListener('click', ()=>{
	window.location.href = "/dashboard"
	main_screen[0].style.display = 'block'
	collection_screen[0].style.display = 'none'
	profile_screen[0].style.display = 'none'
	yearR_screen[0].style.display = 'none'	
	current_screen = 1
})
collection_trigger.addEventListener('click', ()=>{
	main_screen[0].style.display = 'none'
	collection_screen[0].style.display = 'block'
	profile_screen[0].style.display = 'none'
	yearR_screen[0].style.display = 'none'
	current_screen = 2
})
profile_trigger.addEventListener('click', ()=>{
	main_screen[0].style.display = 'none'
	collection_screen[0].style.display = 'none'
	profile_screen[0].style.display = 'block'
	yearR_screen[0].style.display = 'none'
	current_screen = 3
})
yearR_trigger.addEventListener('click', ()=>{
	main_screen[0].style.display = 'none'
	collection_screen[0].style.display = 'none'
	profile_screen[0].style.display = 'none'
	yearR_screen[0].style.display = 'block'
	current_screen = 4
})