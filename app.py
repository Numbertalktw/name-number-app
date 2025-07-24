import streamlit as st

def letter_to_number(letter):
    return ord(letter.upper()) - ord('A') + 1

def reduce_number(n):
    while n not in [11, 22, 33] and n > 9:
        n = sum(int(d) for d in str(n))
    return n

def name_to_life_number(name):
    total = sum(letter_to_number(c) for c in name if c.isalpha())
    reduced = reduce_number(total)
    return total, reduced

st.title("🔡 英文字母 ➜ 數字轉換器")
st.markdown("輸入英文名字，計算對應的生命靈數（支援大師數 11, 22, 33）")

name = st.text_input("請輸入英文名字：")

if name:
    total, result = name_to_life_number(name)
    st.write(f"🔢 英文總和數字：{total}")
    st.write(f"🌟 對應生命靈數為：{result}")

    meaning = {
        1: "領導、獨立、自信",
        2: "合作、敏感、和諧",
        3: "創意、表達、喜悅",
        4: "穩定、實際、努力",
        5: "自由、冒險、變化",
        6: "關懷、責任、美感",
        7: "智慧、內省、靈性",
        8: "事業、權力、財富",
        9: "慈愛、完成、理想",
        11: "靈感直覺、精神覺醒",
        22: "大師建構、遠見實踐",
        33: "無私奉獻、靈性愛"
    }
    st.info(f"✨ 對應意涵：{meaning.get(result, '尚無解釋')}")
