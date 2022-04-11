function mudaActiveNav(label) {
	let activeNav = document.querySelector('.active')
	activeNav.classList.remove('active')
	let nav = document.querySelector('#link-' + label)
	nav.classList.add('active')
}
