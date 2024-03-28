import streamlit as st

# Fungsi untuk merespons pesan pengguna
def respond_to_message(user_input):
    # Contoh aturan sederhana
    if user_input.lower() == "halo":
        return "Halo! Ada yang bisa saya bantu?"
    if user_input.lower() == "siapa kamu":
        return "Hai, Saya Simple "
    else:
        return "Maaf, saya tidak mengerti pertanyaan Anda."

# Fungsi untuk menampilkan pesan
def display_message(sender, message):
    st.write(f"**{sender}:** {message}")

# Judul halaman
st.title("Minator")

# Input text untuk pengguna memasukkan pesan
user_message = st.text_input("Masukkan pesan Anda di sini:")

# Tombol untuk mengirim pesan
if st.button("Kirim"):
    # Menampilkan pesan pengguna
    display_message("Anda", user_message)
    
    # Menanggapi pesan pengguna
    response = respond_to_message(user_message)
    
    # Menampilkan pesan respons
    display_message("Chatbot", response)
