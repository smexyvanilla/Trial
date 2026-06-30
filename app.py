import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="for babybear", page_icon="🐻", layout="centered")

ASSETS = Path(__file__).parent / "assets"

def img_b64(name):
    p = ASSETS / name
    if not p.exists():
        return ""
    return base64.b64encode(p.read_bytes()).decode()

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
    background: radial-gradient(circle at 15% 10%, #2b2440 0%, #1a1530 45%, #100c20 100%);
    color: #f3ecff;
}

#MainMenu, footer, header {visibility: hidden;}

.block-container {
    max-width: 720px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.tape {
    display:inline-block;
    background: rgba(255, 222, 150, 0.55);
    height: 22px;
    width: 70px;
    transform: rotate(-3deg);
    box-shadow: 0 2px 4px rgba(0,0,0,.2);
}

.hero-title {
    font-family: 'Caveat', cursive;
    font-size: 4rem;
    line-height: 1;
    text-align: center;
    color: #ffd9a0;
    margin-bottom: 0;
    text-shadow: 0 0 18px rgba(255,217,160,.35);
}

.hero-sub {
    font-family: 'Patrick Hand', cursive;
    text-align: center;
    color: #cdbfff;
    font-size: 1.15rem;
    margin-top: 6px;
    margin-bottom: 0;
}

.note {
    background: #221c38;
    border: 1px solid rgba(255,255,255,.08);
    border-left: 4px solid #ffb37a;
    border-radius: 4px 14px 14px 4px;
    padding: 22px 26px;
    margin: 18px 0;
    font-size: 1.08rem;
    line-height: 1.85;
    color: #e9e2ff;
    box-shadow: 0 6px 18px rgba(0,0,0,.25);
}

.note b { color: #ffd9a0; }

.handwritten-label {
    font-family: 'Caveat', cursive;
    font-size: 1.7rem;
    color: #ffb37a;
    text-align:center;
    margin: 50px 0 4px;
}

.subtle-label {
    font-family: 'Patrick Hand', cursive;
    text-align:center;
    color: #998fc7;
    margin-bottom: 28px;
}

.polaroid {
    background: #fdf8ee;
    padding: 10px 10px 36px 10px;
    border-radius: 3px;
    box-shadow: 0 10px 24px rgba(0,0,0,.35);
    display:inline-block;
    width: 100%;
}
.polaroid img {
    width: 100%;
    border-radius: 1px;
    display:block;
    object-fit: cover;
    aspect-ratio: 4/5;
}
.polaroid-cap {
    font-family: 'Caveat', cursive;
    font-size: 1.2rem;
    color: #3a3144;
    text-align:center;
    margin-top: 6px;
}

.song-box {
    background: linear-gradient(135deg, #3a2f55, #261f3d);
    border-radius: 16px;
    padding: 28px;
    text-align:center;
    margin: 30px 0;
    border: 1px solid rgba(255,179,122,.25);
}
.song-title {
    font-family:'Caveat', cursive;
    font-size: 2.1rem;
    color:#ffd9a0;
    margin: 6px 0;
}

.divider-hr {
    border: none;
    border-top: 1px dashed rgba(255,255,255,.15);
    margin: 46px 0;
}

div.stButton > button {
    font-family: 'Patrick Hand', cursive;
    font-size: 1.15rem;
    background: #ffb37a;
    color: #1a1530;
    border: none;
    border-radius: 999px;
    padding: 12px 34px;
    box-shadow: 0 6px 16px rgba(255,179,122,.3);
    display:block;
    margin: 0 auto;
}
div.stButton > button:hover {
    background:#ffc796;
    color:#1a1530;
}

.hug-msg {
    text-align:center;
    font-family:'Caveat', cursive;
    font-size: 1.6rem;
    color:#ffd9a0;
    margin-top: 18px;
}

.sig {
    text-align:center;
    font-family:'Caveat', cursive;
    font-size: 1.7rem;
    color:#ffb37a;
    margin-top: 14px;
}

.foot {
    text-align:center;
    color:#6f6592;
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

# ---------- MESSAGE ----------
st.markdown('<div class="handwritten-label">from me, obviously</div>', unsafe_allow_html=True)
st.markdown('''
<div class="note">
i know your office has been making you feel small lately, and i hate it. you go in every day and deal with people who don't see half of what you're actually capable of, and then you still come home with enough energy to send me a meme. that's not nothing. that's actually kind of insane work ethic and i don't think you give yourself credit for it.
</div>
<div class="note">
and i know there's a part of you still stuck on stuff you did before — replaying it, being harder on yourself than literally anyone else ever was. <b>babybear.</b> you are allowed to have grown. i'm not with you despite who you were, i'm with you because of who you've become, and i watch you actively try to be better every single day. that counts for everything.
</div>
<div class="note">
you don't have to have it all figured out this week. you just have to get through it. i'm not going anywhere — not because i have to, but because there's genuinely no one else i'd rather text at 1am about nothing.
</div>
''', unsafe_allow_html=True)
st.markdown('<div class="sig">— your babybear\'s babybear</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider-hr">', unsafe_allow_html=True)

# ---------- OUR SONG ----------
st.markdown('''
<div class="song-box">
  <div class="handwritten-label" style="margin-top:0;">our song, btw</div>
  <div class="song-title">moonlight — dhruv</div>
  <div style="color:#cdbfff; font-family:'Lora',serif; font-size:1rem;">
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

<div class="note"><b>matching spider necklaces, obviously</b><br>
we match outfits we didn't plan and necklaces we definitely did. heart hands for the camera every single time, no exceptions, it's basically law now.</div>

<div class="note"><b>this week, specifically</b><br>
between the office being a whole mess and your brain being mean to you about old stuff — i see you still showing up. that's the entire reason this page exists.</div>
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