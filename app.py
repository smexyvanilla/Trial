import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="for babybear", page_icon="🐻", layout="centered")

ASSETS = Path(__file__).parent / "assets"

def img_b64(name):
    # try a few likely locations in case the folder structure got nested wrong
    candidates = [
        ASSETS / name,
        Path(__file__).parent / "App" / "assets" / name,
        Path.cwd() / "assets" / name,
    ]
    for p in candidates:
        if p.exists():
            return base64.b64encode(p.read_bytes()).decode()
    return ""

PHOTOS = [
    "1000233435.jpg",
    "1000233436.jpg",
    "1000233434.jpg",
    "1000233439.jpg",
    "1000233438.jpg",
    "1000233437.jpg",
    "1000233433.jpg",
]
ROTATIONS = [-4, 3, -2, 5, -3, 2, -5]

# ---------- STYLE ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Patrick+Hand&family=Lora:ital@0;1&display=swap');

html, body, [class*="css"] {
    font-family: 'Lora', serif;
}

.stApp {
    background: linear-gradient(180deg, #FFF6F0 0%, #FDEFE9 40%, #FBEAEF 100%);
    color: #5b4640;
}

#MainMenu, footer, header {visibility: hidden;}

.block-container {
    max-width: 700px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.hero-title {
    font-family: 'Caveat', cursive;
    font-size: 4rem;
    line-height: 1;
    text-align: center;
    color: #e8806a;
    margin-bottom: 0;
}

.hero-sub {
    font-family: 'Patrick Hand', cursive;
    text-align: center;
    color: #a9837c;
    font-size: 1.15rem;
    margin-top: 6px;
    margin-bottom: 0;
}

.note {
    background: #fffaf6;
    border: 1px solid rgba(232,128,106,.12);
    border-left: 4px solid #f3a98a;
    border-radius: 6px 18px 18px 6px;
    padding: 22px 26px;
    margin: 16px 0;
    font-size: 1.08rem;
    line-height: 1.85;
    color: #5b4640;
    box-shadow: 0 6px 16px rgba(232,128,106,.08);
}

.note b { color: #e8806a; }

.handwritten-label {
    font-family: 'Caveat', cursive;
    font-size: 1.9rem;
    color: #e8806a;
    text-align:center;
    margin: 50px 0 4px;
}

.subtle-label {
    font-family: 'Patrick Hand', cursive;
    text-align:center;
    color: #b89a92;
    margin-bottom: 28px;
}

.polaroid {
    background: #fffaf6;
    padding: 10px 10px 36px 10px;
    border-radius: 6px;
    box-shadow: 0 8px 20px rgba(232,128,106,.16);
    display:inline-block;
    width: 100%;
}
.polaroid img {
    width: 100%;
    border-radius: 2px;
    display:block;
    object-fit: cover;
    aspect-ratio: 4/5;
}
.polaroid-cap {
    font-family: 'Caveat', cursive;
    font-size: 1.2rem;
    color: #8a6e64;
    text-align:center;
    margin-top: 6px;
}

.song-box {
    background: linear-gradient(135deg, #ffe3d6, #ffd9e6);
    border-radius: 20px;
    padding: 28px;
    text-align:center;
    margin: 30px 0;
    border: 1px solid rgba(232,128,106,.18);
}
.song-title {
    font-family:'Caveat', cursive;
    font-size: 2.1rem;
    color:#e8806a;
    margin: 6px 0;
}

.divider-hr {
    border: none;
    border-top: 1px dashed rgba(232,128,106,.22);
    margin: 46px 0;
}

div.stButton > button {
    font-family: 'Patrick Hand', cursive;
    font-size: 1.15rem;
    background: #f3a98a;
    color: #fff;
    border: none;
    border-radius: 999px;
    padding: 12px 34px;
    box-shadow: 0 8px 18px rgba(232,128,106,.3);
    display:block;
    margin: 0 auto;
}
div.stButton > button:hover {
    background:#e8806a;
    color:#fff;
}

.hug-msg {
    text-align:center;
    font-family:'Caveat', cursive;
    font-size: 1.7rem;
    color:#e8806a;
    margin-top: 18px;
}

.sig {
    text-align:center;
    font-family:'Caveat', cursive;
    font-size: 1.8rem;
    color:#e8806a;
    margin-top: 14px;
}

.foot {
    text-align:center;
    color:#b89a92;
    font-family:'Patrick Hand', cursive;
    margin-top: 50px;
    font-size: .9rem;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown('<div class="hero-title">hey babybear 🐻</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">get off your phone for a sec, i made you something</div>', unsafe_allow_html=True)

st.markdown('<div class="note">i know this week has genuinely sucked for you. so instead of texting "it\'ll be okay" for the fifth time, i made you this whole little page. yes i\'m unhinged. keep scrolling.</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider-hr">', unsafe_allow_html=True)

# ---------- OUR STORY ----------
st.markdown('<div class="handwritten-label">our story, the real one</div>', unsafe_allow_html=True)
st.markdown('''
<div class="note">
i still remember the day pranathi came up to me and said "tujhe pata hai gaurav bhaiya mile aaj, wo aise the waise the" — and she made me think i like you, even though i never thought so before that.
</div>
<div class="note">
from her random stories about you, following you and "stalking" became part of my daily routine. with some courage she made me text you, and i still remember how scared i was — yet without thinking, i did it anyway.
</div>
<div class="note">
talking behind the phone was cool, until you wanted to see me. scared of how i looked, a thousand insecurities deep, i sent you the photo... thought you'd never talk to me again after that. don't know why you did, but you did.
</div>
<div class="note">
the crossover i was trying to avoid actually happened. my heart was racing like those cars in f1. that text in december made me feel my first real heartbeat for someone, and i realised i'd gotten attached to you far beyond just "do i like him."
</div>
<div class="note">
today, 2.5 years have passed and i still love you like crazy. your smallest validation makes all my effort feel worth it. i developed the courage to face a camera with my teeth wide open without fear — and i thank you for all the effort you put in to make me feel confident, and loved.
</div>
<div class="note">
but as they say, the story can never always be happy. so was mine. plots i never expected showed up right in front of my eyes. i wanted to disappear, all my insecurities and hatred for myself took over me — i felt heartbroken, restless, emotions i'd never felt before. but at the end, i'm still here, with you, hoping that things won't happen again and that this story always gets its happy ending.
</div>
''', unsafe_allow_html=True)
st.markdown('<div class="sig">— your muskmelon, still here, still yours</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider-hr">', unsafe_allow_html=True)

# ---------- OUR SONG ----------
st.markdown('''
<div class="song-box">
  <div class="handwritten-label" style="margin-top:0;">our song, btw</div>
  <div class="song-title">moonlight — dhruv</div>
  <div style="color:#8a6e64; font-family:'Lora',serif; font-size:1rem;">
  you know the one. the one that comes on and we both just go quiet for a second.
  put it on, lie down, and pretend i'm there arguing with you about which side of the bed is "mine."
  </div>
</div>
''', unsafe_allow_html=True)

st.markdown('<hr class="divider-hr">', unsafe_allow_html=True)

# ---------- TIMELINE ----------
st.markdown('<div class="handwritten-label">2.5 years of this circus</div>', unsafe_allow_html=True)
st.markdown('<div class="subtle-label">a highly biased recap</div>', unsafe_allow_html=True)

st.markdown('''
<div class="note"><b>somehow it worked</b><br>
2.5 years and i still don't fully know how we ended up this attached to each other. but here we are — mirror selfies, random bicycles, gates we pose behind for no reason.</div>
''', unsafe_allow_html=True)

st.markdown('<hr class="divider-hr">', unsafe_allow_html=True)

# ---------- GALLERY ----------
st.markdown('<div class="handwritten-label">exhibit a through g</div>', unsafe_allow_html=True)
st.markdown('<div class="subtle-label">evidence we are, in fact, cute</div>', unsafe_allow_html=True)

captions = [
    "the brown tank top fit", "bicycle, sunset, no plan", "mirror, garden, us",
    "heart hands, mandatory", "matching necklaces day", "behind the gate",
    "just us, just talking"
]

cols = st.columns(2)
for i, (photo, rot, cap) in enumerate(zip(PHOTOS, ROTATIONS, captions)):
    b64 = img_b64(photo)
    if not b64:
        continue
    with cols[i % 2]:
        st.markdown(f'''
        <div style="transform: rotate({rot}deg); margin-bottom: 26px;">
          <div class="polaroid">
            <img src="data:image/jpeg;base64,{b64}">
            <div class="polaroid-cap">{cap}</div>
          </div>
        </div>
        ''', unsafe_allow_html=True)

st.markdown('<hr class="divider-hr">', unsafe_allow_html=True)

# ---------- REASONS ----------
st.markdown('<div class="handwritten-label">things i won\'t shut up about</div>', unsafe_allow_html=True)
st.markdown('''
<div class="note"><b>your curls</b> — you act like you don't care but you absolutely check the mirror twice.</div>
<div class="note"><b>the photographer arc</b> — phone up, head tilted, you've made a stairwell look like a magazine shoot.</div>
<div class="note"><b>you show up anyway</b> — toxic office day, bad headspace, doesn't matter. you still text me back.</div>
<div class="note"><b>your laugh</b> — it ruins my whole "i'm mad at you" plan every single time.</div>
<div class="note"><b>you're not the worst thing you've done</b> — i need you to actually believe that one.</div>
''', unsafe_allow_html=True)

st.markdown('<hr class="divider-hr">', unsafe_allow_html=True)

# ---------- HUG BUTTON ----------
st.markdown('<div class="handwritten-label">okay one last thing</div>', unsafe_allow_html=True)

if "hugged" not in st.session_state:
    st.session_state.hugged = False

if st.button("tap this, babybear"):
    st.session_state.hugged = True

if st.session_state.hugged:
    st.markdown('<div class="hug-msg">there. you\'ve been hugged. virtually, badly, but with full intent. go drink some water and go to sleep. 🐻</div>', unsafe_allow_html=True)

st.markdown('<div class="foot">made by your babybear, who is currently very proud of you</div>', unsafe_allow_html=True)