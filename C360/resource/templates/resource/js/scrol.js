// scrollToBottom.js

// Function to scroll to the bottom of the message container
function scrollToBottom() {
    var messageContainer = document.getElementById('message-container');
    messageContainer.scrollTop = messageContainer.scrollHeight;
  }
  
  // Call the scrollToBottom function when new content is added to the message container
  function observeMessageContainer() {
    var messageContainer = document.getElementById('message-container');
  
    // Create a new MutationObserver instance
    var observer = new MutationObserver(function (mutations) {
      // Scroll to the bottom when new content is added
      scrollToBottom();
    });
  
    // Configure and start the observer
    var observerConfig = { childList: true, subtree: true };
    observer.observe(messageContainer, observerConfig);
  
    // Scroll to the bottom initially
    scrollToBottom();
  }
  
  // Call the observeMessageContainer function after the DOM content is loaded
  document.addEventListener('DOMContentLoaded', observeMessageContainer);