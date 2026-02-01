// static/js/script.js

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.animation = 'slideOut 0.3s ease forwards';
            setTimeout(() => message.remove(), 300);
        }, 5000);
    });

    // Add slideOut animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideOut {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(100%);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const inputs = this.querySelectorAll('input[required], select[required]');
            let isValid = true;

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.style.borderColor = '#f44336';
                    
                    // Add error message
                    if (!input.nextElementSibling?.classList.contains('error-message')) {
                        const error = document.createElement('div');
                        error.className = 'error-message';
                        error.textContent = 'This field is required';
                        error.style.color = '#f44336';
                        error.style.fontSize = '0.8rem';
                        error.style.marginTop = '0.3rem';
                        input.parentNode.appendChild(error);
                    }
                } else {
                    input.style.borderColor = '#1e90ff';
                    
                    // Remove error message
                    const error = input.parentNode.querySelector('.error-message');
                    if (error) error.remove();
                }
            });

            if (!isValid) {
                e.preventDefault();
            }
        });
    });

    // GPA color coding
    const gpaCells = document.querySelectorAll('.gpa-cell');
    gpaCells.forEach(cell => {
        const gpa = parseFloat(cell.textContent);
        if (gpa >= 3.5) {
            cell.style.color = '#4CAF50';
        } else if (gpa >= 3.0) {
            cell.style.color = '#2196F3';
        } else if (gpa >= 2.0) {
            cell.style.color = '#FF9800';
        } else {
            cell.style.color = '#f44336';
        }
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Print result button functionality
    const printButtons = document.querySelectorAll('.print-btn');
    printButtons.forEach(button => {
        button.addEventListener('click', function() {
            window.print();
        });
    });

    // Dark mode toggle (optional)
    const darkModeToggle = document.createElement('button');
    darkModeToggle.className = 'dark-mode-toggle';
    darkModeToggle.innerHTML = '<i class="fas fa-moon"></i>';
    darkModeToggle.style.position = 'fixed';
    darkModeToggle.style.bottom = '20px';
    darkModeToggle.style.right = '20px';
    darkModeToggle.style.zIndex = '1000';
    darkModeToggle.style.background = '#1e90ff';
    darkModeToggle.style.color = 'white';
    darkModeToggle.style.border = 'none';
    darkModeToggle.style.borderRadius = '50%';
    darkModeToggle.style.width = '50px';
    darkModeToggle.style.height = '50px';
    darkModeToggle.style.cursor = 'pointer';
    darkModeToggle.style.fontSize = '1.2rem';
    darkModeToggle.style.boxShadow = '0 4px 12px rgba(0,0,0,0.2)';
    
    darkModeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        this.innerHTML = document.body.classList.contains('dark-mode') 
            ? '<i class="fas fa-sun"></i>' 
            : '<i class="fas fa-moon"></i>';
    });
    
    document.body.appendChild(darkModeToggle);

    // Add dark mode styles
    const darkModeStyles = document.createElement('style');
    darkModeStyles.textContent = `
        body.dark-mode {
            background: #121212;
            color: #ffffff;
        }
        
        body.dark-mode .university-header {
            background: linear-gradient(to right, #0a4a8a, #1e90ff);
        }
        
        body.dark-mode .main-nav {
            background: #1e1e1e;
        }
        
        body.dark-mode .nav-links a {
            color: #ffffff;
        }
        
        body.dark-mode .search-container,
        body.dark-mode .batch-card,
        body.dark-mode .result-card {
            background: #1e1e1e;
            color: #ffffff;
        }
        
        body.dark-mode .footer {
            background: #0a4a8a;
        }
    `;
    document.head.appendChild(darkModeStyles);
});

// Real-time clock
function updateClock() {
    const now = new Date();
    const clockElement = document.getElementById('clock');
    if (clockElement) {
        clockElement.textContent = now.toLocaleString('en-US', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });
    }
}

// Update clock every second
setInterval(updateClock, 1000);

// Initialize clock on page load
window.addEventListener('load', updateClock);