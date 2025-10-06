// alert('Welcome to EduMeadow!');

document.querySelectorAll('.toggle-button').forEach(button => {
    button.addEventListener('click', () => {
        const commentBox = button.nextElementSibling;
        commentBox.classList.toggle('show');
    });
});