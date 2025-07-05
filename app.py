import streamlit as st

# 로스트사가 레벨별 누적 경험치 테이블 (1~100레벨)
level_exp_table = {
    1: 50, 2: 110, 3: 190, 4: 300, 5: 450, 6: 650, 7: 910, 8: 1240, 9: 1650, 10: 2150,
    11: 2750, 12: 3460, 13: 4290, 14: 5250, 15: 6350, 16: 7600, 17: 9010, 18: 10590, 19: 12350,
    20: 14300, 21: 16450, 22: 18800, 23: 21350, 24: 24100, 25: 27050, 26: 30200, 27: 33550,
    28: 37100, 29: 40850, 30: 44800, 31: 49000, 32: 53450, 33: 58150, 34: 63100, 35: 68300,
    36: 73750, 37: 79450, 38: 85400, 39: 91600, 40: 98050, 41: 104850, 42: 112000, 43: 119500,
    44: 127350, 45: 135550, 46: 144100, 47: 153000, 48: 162250, 49: 171850, 50: 181800,
    51: 192250, 52: 203200, 53: 214650, 54: 226600, 55: 239050, 56: 252000, 57: 265450,
    58: 279400, 59: 293850, 60: 308800, 61: 324550, 62: 341100, 63: 358450, 64: 376600,
    65: 395550, 66: 415300, 67: 435850, 68: 457200, 69: 479350, 70: 502300, 71: 526850,
    72: 553000, 73: 580750, 74: 610100, 75: 641050, 76: 673600, 77: 707750, 78: 742900,
    79: 780250, 80: 819200, 81: 860850, 82: 905200, 83: 952250, 84: 1002000, 85: 1054450,
    86: 1109600, 87: 1167450, 88: 1228000, 89: 1291250, 90: 1357200, 91: 1427450,
    92: 1502000, 93: 1580850, 94: 1664000, 95: 1751450, 96: 1843200, 97: 1939250,
    98: 2039600, 99: 2144250, 100: 2253200
}

exp_per_coupon = 14300  # EXP 쿠폰 1장당 제공 경험치

def get_level_from_exp(total_exp):
    for level in range(1, 101):
        if total_exp < level_exp_table[level]:
            return level - 1
    return 100

def get_needed_coupons(start_level, end_level):
    if start_level < 1 or end_level > 100 or start_level >= end_level:
        return None
    required_exp = level_exp_table[end_level] - level_exp_table[start_level]
    return (required_exp + exp_per_coupon - 1) // exp_per_coupon

# Streamlit 앱 시작
st.set_page_config(page_title="로스트사가 EXP 쿠폰 계산기", page_icon="🎮")
st.title("🎮 로스트사가 EXP 쿠폰 계산기")
st.markdown("EXP 쿠폰으로 도달 가능한 레벨 또는 필요한 쿠폰 수를 계산해보세요.")

mode = st.radio("기능 선택", ["1. 시작 레벨 + 쿠폰 → 도달 레벨", "2. 시작~목표 레벨 → 필요한 쿠폰 수"])

if mode == "1. 시작 레벨 + 쿠폰 → 도달 레벨":
    start_level = st.number_input("시작 레벨 입력 (1~99)", min_value=1, max_value=99, step=1)
    count = st.number_input("EXP 쿠폰 갯수 입력", min_value=0, step=1)
    starting_exp = level_exp_table[start_level]
    total_exp = starting_exp + count * exp_per_coupon
    reached_level = get_level_from_exp(total_exp)
    st.success(f"💡 {start_level}레벨에서 쿠폰 {count}장 사용 시 도달 가능한 레벨: **{reached_level}레벨**")
    st.write(f"📊 총 획득 경험치: `{total_exp}` EXP")

elif mode == "2. 시작~목표 레벨 → 필요한 쿠폰 수":
    col1, col2 = st.columns(2)
    with col1:
        start = st.number_input("시작 레벨", min_value=1, max_value=99, step=1, key="start")
    with col2:
        end = st.number_input("목표 레벨", min_value=start+1, max_value=100, step=1, key="end")
    coupons = get_needed_coupons(start, end)
    if coupons is not None:
        required_exp = level_exp_table[end] - level_exp_table[start]
        st.success(f"💡 {start}레벨 → {end}레벨까지 필요한 쿠폰 수: **{coupons}장**")
        st.write(f"📊 필요 경험치: `{required_exp}` EXP")
