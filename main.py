import streamlit as st
import pandas as pd

# Using "with" notation
with st.sidebar:
    st.header("各科成绩")
    options = st.multiselect(
        '选课情况',
        ['政治', '历史', '地理', '物理', '化学', '生物', '技术'],
    )
    Chs_mark = st.text_input('语文成绩')
    Chs_grade = st.radio(
        'Chs_grade',
        ['A', 'B', 'C', 'D', 'E'],
        horizontal=True,
        label_visibility="collapsed",
    )
    Math_mark = st.text_input('数学成绩')
    Math_grade = st.radio(
        'Math_grade',
        ['A', 'B', 'C', 'D', 'E'],
        horizontal=True,
        label_visibility="collapsed",
    )
    Eng_mark = st.text_input('英语成绩')
    Eng_grade = st.radio(
        'Eng_grade',
        ['A', 'B', 'C', 'D', 'E'],
        horizontal=True,
        label_visibility="collapsed",
    )
    Pol_mark = st.text_input('政治成绩')
    Pol_grade = st.radio(
        'Pol_grade',
        ['A', 'B', 'C', 'D', 'E'],
        horizontal=True,
        label_visibility="collapsed",
    )
    His_mark = st.text_input('历史成绩')
    His_grade = st.radio(
        'His_grade',
        ['A', 'B', 'C', 'D', 'E'],
        horizontal=True,
        label_visibility="collapsed",
    )
    Geo_mark = st.text_input('地理成绩')
    Geo_grade = st.radio(
        'Geo_grade',
        ['A', 'B', 'C', 'D', 'E'],
        horizontal=True,
        label_visibility="collapsed",
    )
    Che_mark = st.text_input('化学成绩')
    Che_grade = st.radio(
        'Che_grade',
        ['A', 'B', 'C', 'D', 'E'],
        horizontal=True,
        label_visibility="collapsed",
    )
    Bio_mark = st.text_input('生物成绩')
    Bio_grade = st.radio(
        'Bio_grade',
        ['A', 'B', 'C', 'D', 'E'],
        horizontal=True,
        label_visibility="collapsed",
    )
    Tec_mark = st.text_input('技术成绩')
    Tec_grade = st.radio(
        'Tec_grade',
        ['A', 'B', 'C', 'D', 'E'],
        horizontal=True,
        label_visibility="collapsed",
    )
    btn_stats = st.button('OK')
st.header("Mark")

if btn_stats:
    Mark_list = [Chs_mark, Math_mark, Eng_mark, Pol_mark, His_mark, Geo_mark, Che_mark, Bio_mark, Tec_mark]
    Grade_list = [Chs_grade, Math_grade, Eng_grade, Pol_grade, His_grade, Geo_grade, Che_grade, Bio_grade, Tec_grade]
    A_num, B_num, C_num, D_num, E_num = 0, 0, 0, 0, 0
    # 初始化数组

    for i in Grade_list:
        if i == 'A':
            A_num += 1
        elif i == 'B':
            B_num += 1
        elif i == 'C':
            C_num += 1
        elif i == 'D':
            D_num += 1
        else:
            E_num += 1
    Grade_nums = [A_num, B_num, C_num, D_num, E_num]
    st.write('分数', Chs_mark, Math_mark, Eng_mark, Pol_mark, His_mark, Geo_mark, Che_mark, Bio_mark, Tec_mark)
    st.write('等级', Chs_grade, Math_grade, Eng_grade, Pol_grade, His_grade, Geo_grade, Che_grade, Bio_grade, Tec_grade)
    st.write('选课', options[0], options[1], options[2])
    print(Grade_nums)

    df = pd.read_csv('/Users/fan/PycharmProjects/pythonProject1/sch.csv')
    st.write(df)
