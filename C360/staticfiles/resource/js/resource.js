window.onload = function() {
    showFlashMessage('success');
};

function showFlashMessage(type) {
    var flashMessage = document.getElementById('flash-message');
    var flashMessageText = document.getElementById('flash-message-text');

    if (type === 'success') {
        flashMessage.className = 'flash-message success';
        flashMessageText.textContent = 'Success! authentication passed.';
        flashMessage.style.color = 'white';
        flashMessage.style.fontSize= '24px';
        flashMessage.style.backgroundColor ='#28a745;';
        flashMessage.style.width = '100%';
    } else if (type === 'error') {
        flashMessage.className = 'flash-message error';
        flashMessageText.textContent = 'Error! Please fill in all the required fields.';
    }

    flashMessage.style.display = 'block';
    setTimeout(function() {
        flashMessage.style.opacity = '0';
        setTimeout(function() {
            flashMessage.style.display = 'none';
            
            flashMessage.style.opacity = '1';
        }, 300);
    }, 3000);
}