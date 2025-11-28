document.addEventListener('DOMContentLoaded', () => {
    const signInForm = document.getElementById('signInForm');
    const signUpForm = document.getElementById('signUpForm');
    const responseMessage = document.getElementById('responseMessage');

    const API_BASE_URL = 'http://127.0.0.1:8000/api';

    const handleResponse = (message, isError = false) => {
        if (responseMessage) {
            responseMessage.textContent = message;
            responseMessage.className = 'response-message'; // Reset classes
            if (isError) {
                responseMessage.classList.add('error');
            } else {
                responseMessage.classList.add('success');
            }
        }
    };

    if (signInForm) {
        signInForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(signInForm);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch(`${API_BASE_URL}/signin`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                const result = await response.json();

                if (response.ok) {
                    handleResponse(result.message);
                } else {
                    handleResponse(`Error: ${result.detail || 'Sign-in failed'}`, true);
                }
            } catch (error) {
                console.error('Sign-in error:', error);
                handleResponse('An unexpected error occurred. Please try again.', true);
            }
        });
    }

    if (signUpForm) {
        signUpForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(signUpForm);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch(`${API_BASE_URL}/signup`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                const result = await response.json();

                if (response.ok) {
                    handleResponse(`Sign-up successful for ${result.user_name}. You can now sign in.`);
                } else {
                    handleResponse(`Error: ${result.detail || 'Sign-up failed'}`, true);
                }
            } catch (error) {
                console.error('Sign-up error:', error);
                handleResponse('An unexpected error occurred. Please try again.', true);
            }
        });
    }
});
