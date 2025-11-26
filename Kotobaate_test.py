import random
import streamlit as st

# ことばリスト
kotoba = ["あんぱん","あいどる","いのしし","うめぼし","ういるす","えだまめ","えびちり","おにぎり","おれんじ",
            "かいがら","かいしゃ","きつつき","きみどり","くさかり","くしかつ","くつした","けいたい","けんだま","こうもり",
            "さいだー","さかむけ","しまうま","しりとり","すいっち","すいえい","せいかつ","せんせい","せんたく","そうじき","そうめん",
            "たけうま","たこやき","ちゃいむ","ちりとり","つなひき","つりざお","てあらい","てぶくろ","とびばこ","とんかつ"]

st.title("ことばあてゲーム～！")

# セッション初期化
if "answer" not in st.session_state:
    st.session_state.answer = random.choice(kotoba)
if "typed" not in st.session_state:
    st.session_state.typed = ""
if "last_message" not in st.session_state:
    st.session_state.last_message = ""

# 入力欄（直接入力）
st.session_state.typed_input = st.text_input("４文字ことばを入力してください（やめるの入力で終了）", value=st.session_state.get("typed_input",""))

# 現在の入力（常に合成して表示。固定高さでビクつき防止）
current_input = st.session_state.typed_input + st.session_state.typed
st.markdown("### 現在の入力")
st.markdown(
    f"""
    <div style="
        height:50px;
        border:1px solid #ddd;
        padding:5px 10px;
        margin-bottom:30px;
        background-color:#f9f9f9;
        display:flex;
        align-items:flex-start;
        justify-content:flex-start;
        text-align:left;">
    <span style="line-height:1.2; white-space:pre-line;">{current_input}</span>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- コールバック（入力遅れ防止のため on_click でセッション更新） ----
def add_char(ch: str):
    st.session_state.typed += ch

def do_ok():
    ci = st.session_state.typed_input + st.session_state.typed
    if not ci:
        return
    if ci == st.session_state.answer:
        st.session_state.last_message = "せいかい！"
        st.session_state.answer = random.choice(kotoba)
        st.session_state.typed = ""
        st.session_state.typed_input = ""
    elif ci == "やめる":
        st.session_state.last_message = "ゲームを終了しました"
        st.session_state.typed = ""
        st.session_state.typed_input = ""
    else:
        hint_lines = []
        for i in range(min(len(st.session_state.answer), len(ci))):
            if ci[i] == st.session_state.answer[i]:
                hint_lines.append(f"{i+1}文字目が正解 ({st.session_state.answer[i]})")
        # ヒント＋再挑戦メッセージをまとめて枠内に表示
        st.session_state.last_message = "\n".join(hint_lines + ["もう一度挑戦しよう"])
        st.session_state.typed = ""

def do_quit():
    st.session_state.last_message = "ゲームを終了しました"
    st.session_state.typed = ""
    st.session_state.typed_input = ""

# ---- OK／やめる（あいうえおリストの上に配置） ----
c1, c2 = st.columns(2)
with c1:
    st.button("OK", key="btn_ok", on_click=do_ok)
with c2:
    st.button("やめる", key="btn_quit", on_click=do_quit)

# メッセージ枠（余白たっぷり・固定高さで安定表示）
st.markdown(
    f"""
    <div style="
        min-height:40px;
        padding:12px; 
        margin-top:10px; 
        margin-bottom:20px; 
        color:#333;
        background-color:#fcfcfc;
        display:flex;
        align-items:flex-start;
        text-align:left;
        white-space:pre-line;
        line-height:1.5;">
        {st.session_state.last_message}
    </div>
    """,
    unsafe_allow_html=True
)

# ---- 五十音ボタン群（OK／やめるの下） ----
gojuon_columns = [
    ["あ", "い", "う", "え", "お"],
    ["か", "き", "く", "け", "こ"],
    ["さ", "し", "す", "せ", "そ"],
    ["た", "ち", "つ", "て", "と"],
    ["な", "に", "ぬ", "ね", "の"],
    ["は", "ひ", "ふ", "へ", "ほ"],
    ["ま", "み", "む", "め", "も"],
    ["や", "",  "ゆ", "",  "よ"],
    ["ら", "り", "る", "れ", "ろ"],
    ["わ", "",  "",   "",  "を"],
    ["",   "",  "",   "",  "ん"]
]
gojuon_columns_sonota = [
    ["が","ぎ","ぐ","げ","ご"],
    ["ざ","じ","ず","ぜ","ぞ"],
    ["だ","ぢ","づ","で","ど"],
    ["ば","び","ぶ","べ","ぼ"],
    ["ぱ","ぴ","ぷ","ぺ","ぽ"],
    ["ゃ","　","ゅ","　","ょ"],
    ["っ","　","　","　","ー"],
]

st.markdown("### あいうえおリスト")
cols = st.columns(len(gojuon_columns))
for col_idx, col_chars in enumerate(gojuon_columns):
    with cols[col_idx]:
        for row_idx, ch in enumerate(col_chars):
            if ch.strip():
                st.button(
                    ch,
                    key=f"btn_{ch}_{col_idx}_{row_idx}",
                    on_click=add_char,
                    args=(ch,)
                )

st.markdown("### その他ボタン")
cols2 = st.columns(len(gojuon_columns_sonota))
for col2_idx, col2_chars in enumerate(gojuon_columns_sonota):
    with cols2[col2_idx]:
        for row_idx, ch in enumerate(col2_chars):
            if ch.strip():
                st.button(
                    ch,
                    key=f"btn_{ch}_sonota_{col2_idx}_{row_idx}",
                    on_click=add_char,
                    args=(ch,)
                )