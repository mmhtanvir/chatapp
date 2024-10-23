function toggleMode() {
    // Toggle the body class between light and dark modes
    document.body.classList.toggle('bg-light');
    document.body.classList.toggle('bg-dark');
    document.body.classList.toggle('text-dark');
    document.body.classList.toggle('text-light');
  
    // Toggle offcanvas background and text color
    const offcanvas = document.getElementById('offcanvasNavbar');
    const listItems = offcanvas.getElementsByClassName('list-group-item');
  
    offcanvas.classList.toggle('bg-light');
    offcanvas.classList.toggle('bg-dark');
    offcanvas.classList.toggle('text-dark');
    offcanvas.classList.toggle('text-light');
  
    // Update the individual list items inside offcanvas
    for (let i = 0; i < listItems.length; i++) {
        listItems[i].classList.toggle('bg-light');
        listItems[i].classList.toggle('bg-dark');
        listItems[i].classList.toggle('text-dark');
        listItems[i].classList.toggle('text-light');
    }
  
    // Update button icon and text
    const modeToggleBtn = document.getElementById('modeToggleBtn');
    if (document.body.classList.contains('bg-dark')) {
        modeToggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
        modeToggleBtn.classList.remove('btn-outline-dark');
        modeToggleBtn.classList.add('btn-outline-light');
    } else {
        modeToggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
        modeToggleBtn.classList.remove('btn-outline-light');
        modeToggleBtn.classList.add('btn-outline-dark');
    }
  }