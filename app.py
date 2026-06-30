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

def photo_tag(name, rot=0):
    b64 = img_b64(name)
    if not b64:
        return f'<div style="color:#b5847a;font-family:\'Patrick Hand\',cursive;">missing: {name}</div>'
    return f'''
    <div style="transform:rotate({rot}deg);">
      <div class="polaroid"><img src="data:image/jpeg;base64,{b64}"></div>
    </div>
    '''

# ---------- STYLE ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Patrick+Hand&family=Lora:ital@0;1&display=swap');

html, body, [class*="css"] { font-family: 'Lora', serif; }

.stApp {
    background: linear-gradient(160deg, #FFF3EC 0%, #FFE8E0 35%, #FDE2EC 70%, #F7E4F2 100%);
    color: #5b4640;
}
#MainMenu, footer, header {visibility: hidden;}
.block-container { max-width: 680px; padding-top: 1.5rem; padding-bottom: 4rem; }

.title-card{
    text-align:center;
    margin-bottom: 6px;
}
.title-card .pet-names{
    font-family:'Patrick Hand', cursive;
    color:#c98a78;
    font-size:1rem;
    letter-spacing:.06em;
    text-transform:uppercase;
}
.title-card h1{
    font-family:'Caveat', cursive;
    font-weight:700;
    font-size:3.6rem;
    line-height:1.05;
    color:#e8704f;
    margin:6px 0 4px;
}
.title-card p{
    font-family:'Patrick Hand', cursive;
    color:#a9837c;
    font-size:1.1rem;
}

.scrap{
    background:#fffaf6;
    border-radius:22px;
    padding:24px 26px;
    box-shadow:0 10px 26px rgba(232,112,79,.10);
    margin: 22px 0;
    border:1px solid rgba(232,112,79,.10);
}
.scrap p{font-size:1.06rem; line-height:1.85; color:#5b4640; margin:0;}
.scrap b{color:#e8704f;}

.tag{
    display:inline-block;
    font-family:'Caveat', cursive;
    font-size:1.5rem;
    color:#fff;
    background:#f0a98e;
    padding:2px 18px;
    border-radius:999px;
    margin-bottom:10px;
    transform:rotate(-2deg);
}

.polaroid{
    background:#fffaf6;
    padding:8px 8px 8px 8px;
    border-radius:10px;
    box-shadow:0 10px 22px rgba(232,112,79,.18);
}
.polaroid img{
    width:100%;
    border-radius:4px;
    display:block;
    object-fit:cover;
    aspect-ratio:1/1;
}

.divider{
    text-align:center;
    color:#e8a796;
    font-family:'Caveat', cursive;
    font-size:1.4rem;
    margin:46px 0 8px;
}
.divider::before, .divider::after{ content:"⋆"; margin:0 12px; opacity:.7;}

.song-box{
    background: linear-gradient(135deg, #ffd9c4, #ffd2e3);
    border-radius:24px;
    padding:30px;
    text-align:center;
    margin:36px 0;
}
.song-box .tag2{font-family:'Patrick Hand',cursive; color:#c45a3e; letter-spacing:.08em; text-transform:uppercase; font-size:.85rem;}
.song-box h2{font-family:'Caveat', cursive; font-size:2.3rem; color:#c45a3e; margin:8px 0;}
.song-box p{color:#8a6e64; font-size:1rem; line-height:1.7; max-width:420px; margin:0 auto;}

.endbox{
    text-align:center;
    background:#fffaf6;
    border-radius:24px;
    padding:36px 26px;
    margin-top:10px;
    box-shadow:0 10px 26px rgba(232,112,79,.12);
}
.endbox h3{font-family:'Caveat', cursive; font-size:2.2rem; color:#e8704f; margin-bottom:14px;}

div.stButton > button{
    font-family:'Patrick Hand', cursive;
    font-size:1.1rem;
    background:#e8704f;
    color:#fff;
    border:none;
    border-radius:999px;
    padding:13px 36px;
    box-shadow:0 8px 18px rgba(232,112,79,.32);
    display:block;
    margin:0 auto;
}
div.stButton > button:hover{ background:#d65f3e; color:#fff; }

.reveal{
    text-align:center;
    font-family:'Caveat', cursive;
    font-size:1.6rem;
    color:#e8704f;
    margin-top:18px;
}

.foot{
    text-align:center;
    color:#c2a097;
    font-family:'Patrick Hand', cursive;
    margin-top:50px;
    font-size:.9rem;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown('''
<div class="title-card">
  <div class="pet-names">muskmelon × babybear</div>
  <h1>for my babybear 🐻</h1>
  <p>okay get comfy, this one's a little long</p>
</div>
''', unsafe_allow_html=True)

st.markdown(f'''
<div class="scrap" style="text-align:center;">
  <p>2.5 years deserves more than a "u good?" text. so here's the actual story — start to now.</p>
</div>
''', unsafe_allow_html=True)

# ---------- STORY: alternating text/photo ----------
def story_block(tag, text, photo, rot, photo_first=False):
    c1, c2 = st.columns([3, 2])
    text_col, photo_col = (c2, c1) if photo_first else (c1, c2)
    with text_col:
        st.markdown(f'<div class="scrap"><span class="tag">{tag}</span><p>{text}</p></div>', unsafe_allow_html=True)
    with photo_col:
        st.markdown(photo_tag(photo, rot), unsafe_allow_html=True)

st.markdown('<div class="divider">how it started</div>', unsafe_allow_html=True)

story_block(
    "the pranathi effect",
    'i still remember the day pranathi came up to me and said <i>"tujhe pata hai gaurav bhaiya mile aaj, wo aise the waise the"</i> — and she made me think i like you, even though i never thought so before that.',
    "1000233437.jpg", -4
)

story_block(
    "the stalking era",
    "from her random stories about you, following you and \"stalking\" became part of my daily routine. with some courage she made me text you, and i still remember how scared i was — yet without thinking, i did it anyway.",
    "1000233438.jpg", 3, photo_first=True
)

story_block(
    "the photo i was scared to send",
    "talking behind the phone was cool, until you wanted to see me. scared of how i looked, a thousand insecurities deep, i sent you the photo... thought you'd never talk to me again after that. don't know why you did, but you did.",
    "1000233439.jpg", -3
)

story_block(
    "december",
    "the crossover i was trying to avoid actually happened. my heart was racing like those cars in f1. that text in december made me feel my first real heartbeat for someone, and i realised i'd gotten attached to you far beyond just \"do i like him.\"",
    "1000233434.jpg", 4, photo_first=True
)

st.markdown('<div class="divider">where we are now</div>', unsafe_allow_html=True)

story_block(
    "2.5 years later",
    "today, 2.5 years have passed and i still love you like crazy. your smallest validation makes all my effort feel worth it. i developed the courage to face a camera with my teeth wide open without fear — and i thank you for all the effort you put in to make me feel confident, and loved.",
    "1000233435.jpg", -2
)

story_block(
    "the harder part",
    "but as they say, the story can never always be happy. so was mine. plots i never expected showed up right in front of my eyes. i wanted to disappear, all my insecurities and hatred for myself took over me — i felt heartbroken, restless, emotions i'd never felt before.",
    "1000233436.jpg", 3, photo_first=True
)

st.markdown(f'''
<div class="scrap" style="text-align:center;">
  <p><b>but at the end, i'm still here</b>, with you, hoping that things won't happen again and that this story always gets its happy ending.</p>
</div>
''', unsafe_allow_html=True)

# ---------- OUR SONG ----------
st.markdown('''
<div class="song-box">
  <div class="tag2">our song, btw</div>
  <h2>moonlight — dhruv</h2>
  <p>you know the one. the one that comes on and we both just go quiet for a second.
  put it on, lie down, and pretend i'm there arguing with you about which side of the bed is "mine."</p>
</div>
''', unsafe_allow_html=True)

# ---------- LAST PHOTO + CLOSING ----------
st.markdown('<div class="divider">always</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.markdown(photo_tag("1000233433.jpg", -1), unsafe_allow_html=True)

st.markdown('''
<div class="endbox">
  <h3>okay, last thing, babybear</h3>
  <p style="color:#8a6e64; font-size:1.02rem; line-height:1.8; max-width:440px; margin:0 auto 18px;">
  whatever this week's been throwing at you — i'm not going anywhere. not because i have to.
  because there's genuinely no one else i'd rather build a stupid little website for at 1am.
  </p>
</div>
''', unsafe_allow_html=True)

st.write("")
if "hugged" not in st.session_state:
    st.session_state.hugged = False
if st.button("tap this, babybear"):
    st.session_state.hugged = True
if st.session_state.hugged:
    st.markdown('<div class="reveal">there. you\'ve been hugged. virtually, badly, but with full intent. 🐻🍈</div>', unsafe_allow_html=True)

st.markdown('<div class="foot">made by your muskmelon, who is very proud of you</div>', unsafe_allow_html=True)