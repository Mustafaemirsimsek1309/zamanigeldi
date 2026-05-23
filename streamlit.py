import streamlit as st
import time

# Sayfa Ayarları
st.set_page_config(page_title="Küçük Bir Sürpriz... 🌼", page_icon="🌼", layout="centered")

# Sayfa akışı için session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'choice' not in st.session_state:
    st.session_state.choice = None

# --- ADIM 1: GİRİŞ ---
if st.session_state.step == 1:
    st.markdown("<h1 style='text-align: center; color: #f4a261;'>✨ Söz Verdiğim O An Geldi...</h1>", unsafe_allow_html=True)
    st.write("")
    st.write(
        "Günlerdir 'Zamanı gelince söylerim' diyerek merakını canlı tutmaya çalıştım. "
        "Çünkü kim olduğumu sıradan bir mesajla söylemek yerine, sana küçük bir sürpriz yapmak istedim."
    )
    st.write(
        "Seninle konuşmak, o pozitif enerjini ve tatlı muhabbetini tanımak gerçekten çok keyifliydi. "
        "Şimdi hazırsan, arkasındaki ismi öğrenme vakti."
    )
    st.write("---")
    
    if st.button("Hadi Başlayalım 🚀", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# --- ADIM 2: BİLMECE ---
elif st.session_state.step == 2:
    st.markdown("<h2 style='text-align: center; color: #f4a261;'>🕵️‍♂️ Hafıza Testi</h2>", unsafe_allow_html=True)
    st.write("Sana yazan bu gizemli arkadaşın, seninle ilgili anlattığın hiçbir detayı kaçırmadı. Mesela şu menü sence kime ait?")
    
    st.write("### 📜 Favoriler Listesi:")
    st.write("✨ **En Sevilen Yemek:** Şöyle bol soslu harika bir **Mantı** 🥟")
    st.write("✨ **Favori İçecekler:** Buz gibi bir **Mangolu Soğuk Çay** ya da moduna göre bir **Çilekli Süt** 🧋🍓")
    st.write("✨ **En Sevilen Çiçek:** Zarafetiyle bilinen **Papatyalar** 🌼")
    
    st.write("---")
    
    cevap = st.radio(
        "Sence bu kadar güzel zevkleri olan şanslı kişi kim?",
        [
            "Tanıdığım en pozitif ve en güzel enerjiye sahip o kıza! ✨",
            "Zevkleriyle ve samimiyetiyle fark yaratan birine! 🌼",
            "Yukarıdaki listenin dünyadaki tek ve gerçek sahibine! 🥰"
        ]
    )
    
    if st.button("Devam Et ➡️", use_container_width=True):
        st.success("Kesinlikle doğru! Bu detayları unutmak zaten imkansızdı. Şimdi büyük ana geçelim...")
        time.sleep(1.5)
        st.session_state.step = 3
        st.rerun()

# --- ADIM 3: PROGRESS BAR VE BÜYÜK AN ---
elif st.session_state.step == 3:
    st.markdown("<h1 style='text-align: center; color: #f4a261;'>🌼 Ve Karşındaki Kişi... </h1>", unsafe_allow_html=True)
    st.write("")
    
    if 'revealed' not in st.session_state:
        st.session_state.revealed = False

    if not st.session_state.revealed:
        if st.button("Maskeyi Düşür 😎", use_container_width=True):
            progress_text = "İsim yükleniyorrrrr..."
            my_bar = st.progress(0, text=progress_text)
            
            for percent_complete in range(100):
                time.sleep(0.02)
                my_bar.progress(percent_complete + 1, text=progress_text)
            
            time.sleep(0.3)
            my_bar.empty()
            st.session_state.revealed = True
            st.rerun()

    if st.session_state.revealed:
        st.balloons() 
        
        st.markdown("<h2 style='text-align: center; color: #2a9d8f;'>Ben Mustafa Emir Şimşek 👋</h2>", unsafe_allow_html=True)
        st.write("---")
        
        st.write(
            "Evet, günlerdir o tatlı merakınla çözmeye çalıştığın kişi bendim. Fake hesaptan "
            "yazışmak başta küçük bir fikirdi ama senin gibi harika bir enerjisi olan, "
            "konuşmasıyla insanı gülümseten biriyle karşılaşınca sohbeti uzatmak istedim."
        )
        st.write(
            "Seni hem çok güzel hem de çok samimi buluyorum. Artık saklanmak istemedim ve "
            "bu akşam kimliğimi açık etmeye karar verdim. Umarım bu küçük Streamlit sürprizi hoşuna gitmiştir. :)"
        )
        
        # Eklediğin yeni kısım:
        st.write(
            "**İstersen DM'e gel, sana bütüüüün olayları eksiksiz anlatayım.** Merak ettiğin ne varsa "
            "konuşuruz, her şeyi anlatmaya hazırım! 😉"
        )
        
        st.write("---")
        st.markdown("<h3 style='text-align: center;'>Şimdi ne yapıyoruz? 👇</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Bir gün çilekli süt içelim?", use_container_width=True):
                st.session_state.choice = "kahve"
                st.rerun()
        with col2:
            if st.button("Şaşırdım, biraz sindirmem lazım 😲", use_container_width=True):
                st.session_state.choice = "sindirme"
                st.rerun()

        # Seçime göre kalıcı mesajlar
        if st.session_state.choice == "kahve":
            st.success("Harika! O zaman hem planı yapmak hem de tüm detayları dinlemek için seni DM'e bekliyorum. 😉")
        elif st.session_state.choice == "sindirme":
            st.warning("Çok normal, nasıl istersen... Ne zaman yazıp bütün olayları dinlemek istersen ben buralardayım. 😊")