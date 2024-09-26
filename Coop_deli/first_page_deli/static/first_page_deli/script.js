document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for internal links
    const links = document.querySelectorAll('a[href^="#"]');
    for (const link of links) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            window.scrollTo({
                top: targetElement.offsetTop,
                behavior: 'smooth'
            });
        });
    }

    // Interactive form validation
    const form = document.querySelector('form');
    const input = form.querySelector('input[type="text"]');

    form.addEventListener('submit', function(event) {
        if (input.value.trim() === '') {
            event.preventDefault();
            input.style.borderColor = 'red';
        } else {
            input.style.borderColor = '#c0392b';
        }
    });
});
