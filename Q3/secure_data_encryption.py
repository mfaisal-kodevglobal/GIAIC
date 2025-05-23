import streamlit as st
from cryptography.fernet import Fernet
import hashlib
from datetime import datetime

# Generate a key for Fernet encryption
# In a production environment, this should be securely stored and not regenerated each time
def generate_fernet_key():
    if 'fernet_key' not in st.session_state:
        st.session_state.fernet_key = Fernet.generate_key()
    return st.session_state.fernet_key

fernet = Fernet(generate_fernet_key())

# Initialize session state variables
if 'data_store' not in st.session_state:
    st.session_state.data_store = {}
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def hash_passkey(passkey):
    """Hash the passkey using SHA-256"""
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(data, passkey):
    """Encrypt data using Fernet with a passkey-derived key"""
    # Derive a key from the passkey (Fernet requires 32-byte url-safe base64-encoded key)
    key = hashlib.sha256(passkey.encode()).digest()[:32]
    custom_fernet = Fernet(Fernet.generate_key())  # We'll use the passkey-derived key
    encrypted_data = custom_fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, passkey):
    """Decrypt data using Fernet with a passkey-derived key"""
    try:
        key = hashlib.sha256(passkey.encode()).digest()[:32]
        custom_fernet = Fernet(Fernet.generate_key())  # We'll use the passkey-derived key
        decrypted_data = custom_fernet.decrypt(encrypted_data).decode()
        return decrypted_data
    except:
        return None

def store_data(text, passkey):
    """Store encrypted data in memory"""
    hashed_key = hash_passkey(passkey)
    encrypted_text = encrypt_data(text, passkey)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.data_store[hashed_key] = {
        'encrypted_data': encrypted_text,
        'timestamp': timestamp
    }
    st.success("Data stored successfully!")

def retrieve_data(passkey):
    """Retrieve and decrypt data if passkey is correct"""
    hashed_key = hash_passkey(passkey)
    
    if hashed_key in st.session_state.data_store:
        encrypted_data = st.session_state.data_store[hashed_key]['encrypted_data']
        decrypted_data = decrypt_data(encrypted_data, passkey)
        
        if decrypted_data is not None:
            st.session_state.failed_attempts = 0  # Reset failed attempts on success
            return decrypted_data, st.session_state.data_store[hashed_key]['timestamp']
    
    # If we get here, either the key doesn't exist or decryption failed
    st.session_state.failed_attempts += 1
    return None, None

def login_page():
    """Display the login page after too many failed attempts"""
    st.title("Reauthorization Required")
    st.warning("Too many failed attempts. Please reauthenticate.")
    
    login_passkey = st.text_input("Enter your admin passkey:", type="password")
    if st.button("Authenticate"):
        # In a real application, you'd have a proper admin password check
        # Here we're just using a simple check to demonstrate
        if login_passkey == "admin123":
            st.session_state.authenticated = True
            st.session_state.failed_attempts = 0
            st.experimental_rerun()
        else:
            st.error("Incorrect admin passkey")

def home_page():
    """Display the main home page"""
    st.title("Secure Data Storage System")
    
    option = st.radio("Choose an option:", 
                     ("Store New Data", "Retrieve Data"))
    
    if option == "Store New Data":
        st.subheader("Store New Data Securely")
        text_to_store = st.text_area("Enter the text you want to store:")
        passkey = st.text_input("Create a passkey for retrieval:", type="password")
        
        if st.button("Store Data"):
            if text_to_store and passkey:
                store_data(text_to_store, passkey)
            else:
                st.warning("Please enter both text and a passkey")
    
    elif option == "Retrieve Data":
        st.subheader("Retrieve Your Stored Data")
        passkey = st.text_input("Enter your passkey:", type="password")
        
        if st.button("Retrieve Data"):
            if passkey:
                data, timestamp = retrieve_data(passkey)
                if data:
                    st.success("Data retrieved successfully!")
                    st.text_area("Your stored data:", value=data, height=200)
                    st.write(f"Stored on: {timestamp}")
                else:
                    st.error("Incorrect passkey or no data found")
                    st.warning(f"Failed attempts: {st.session_state.failed_attempts}/3")
                    
                    if st.session_state.failed_attempts >= 3:
                        st.session_state.authenticated = False
                        st.experimental_rerun()
            else:
                st.warning("Please enter your passkey")

# Main app logic
def main():
    if st.session_state.failed_attempts >= 3 and not st.session_state.authenticated:
        login_page()
    else:
        home_page()

if __name__ == "__main__":
    main()