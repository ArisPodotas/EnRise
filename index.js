window.addEventListener('scroll', function() {
    const item = document.getElementsByClassName('btn')[0]; // [0] to select and element object from the list
    const scrollPosition = window.scrollY + window.innerHeight; // How much the user has scrolled (from the top)
    const documentHeight = document.documentElement.scrollHeight; // Total page height
    if (scrollPosition >= documentHeight * 0.90) {
        item.classList.remove('hidden');
    } else {
        item.classList.add('hidden'); // Optional: to hide the element again when scrolling back up
    }
});

