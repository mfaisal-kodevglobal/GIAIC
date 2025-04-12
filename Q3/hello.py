import streamlit as st

# Function to load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
local_css("assets/style.css")
#=========================================================
st.html("""
    <style>
        .stMainBlockContainer {
            max-width:100rem;
        }
    </style>
    """
)
#=========================================================
st.write('===================================================================================================================================================================')
st.write('''
            <style>
                [data-testid="stHorizontalBlock"]:has(div.PortMarker) [data-testid="stMarkdownContainer"] p { 
                    margin: 0px 0px 0.2px; 
                    color: #ff00ff;
                }        
            </style>
''', unsafe_allow_html=True)

with st.container():
    INcol1, INcol2 = st.columns(2) 
    with INcol1:
            st.write('div 1 PortMarker <hr>', unsafe_allow_html=True)
            st.write("""<div class='PortMarker'/>something should be here... with css using style.css file that present in assets folder</div>""", unsafe_allow_html=True)
    with INcol2:
            st.write('div 2 <hr>', unsafe_allow_html=True)

with st.container():
    INcol11, INcol22, INcol33, INcol44, INcol55, INcol66, INcol77, INcol88, INcol99, INcol1010, INcol1111, INcol1212 = st.columns(12)
    with INcol11:
        st.write('div 11')
        st.write('<div class="faisal">container is here...</div>', unsafe_allow_html=True)
    with INcol22: 
        st.write('div 22')
        st.write('<ul><li>11111</li><li>22222</li><li>33333</li></ul>', unsafe_allow_html=True)
    with INcol33: 
        st.write('div 33')
        st.write('<ul><li>11111</li><li>22222</li><li>33333</li></ul>', unsafe_allow_html=True) 
    with INcol44: 
        st.write('div 44')
        st.write('<ul><li>11111</li><li>22222</li><li>33333</li></ul>', unsafe_allow_html=True)
    with INcol55: 
        st.write('div 55')
        st.write('<ul><li>11111</li><li>22222</li><li>33333</li></ul>', unsafe_allow_html=True)        
    with INcol66: 
        st.write('div 66')
        st.write('<ul><li>11111</li><li>22222</li><li>33333</li></ul>', unsafe_allow_html=True)    
    with INcol77: 
        st.write('div 77')
        st.write('<ul><li>11111</li><li>22222</li><li>33333</li></ul>', unsafe_allow_html=True)    
    with INcol88: 
        st.write('div 88')
        st.write('<ul><li>11111</li><li>22222</li><li>33333</li></ul>', unsafe_allow_html=True)    
    with INcol99: 
        st.write('div 99')
        st.write('<ul><li>11111</li><li>22222</li><li>33333</li></ul>', unsafe_allow_html=True)    
    with INcol1010: 
        st.write('div 10 10')
        st.write('<ul><li>11111</li><li>22222</li><li>33333</li></ul>', unsafe_allow_html=True)    
    with INcol1111: 
        st.write('div 11 11')
        st.write('<ul><li>11111</li><li>22222</li><li>33333</li></ul>', unsafe_allow_html=True)        
    with INcol1212: 
        st.write('div 12 12')
        st.write('<ul><li>11111</li><li>22222</li><li>33333</li></ul>', unsafe_allow_html=True)        
        
st.write('===================================================================================================================================================================')
#=========================================================Text Inside and Out of Container========================================================
st.write("text outside the container")
with st.container():
    st.write("text inside the container")    
st.write("More text outside the container")
st.markdown(
    """
        <style>
            div[data-testid="stVerticalBlock"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
                border: 1px solid red;
            }
        </style>
    """, unsafe_allow_html=True,
)
st.write('===================================================================================================================================================================')
#=========================================================
def create_container_with_color(id, color="#E4F2EC"):
    # todo: instead of color you can send in any css
    plh = st.container()
    html_code = """<div id = 'my_div_outer'></div>"""
    st.markdown(html_code, unsafe_allow_html=True)

    with plh:
        inner_html_code = """<div id = 'my_div_inner_%s'></div>""" % id
        plh.markdown(inner_html_code, unsafe_allow_html=True)

    ## applying style
    chat_plh_style = """
        <style>
            div[data-testid='stVerticalBlock']:has(div#my_div_inner_%s):not(:has(div#my_div_outer)) {
                background-color: %s;
                border-radius: 20px;
                padding: 10px;
            };
        </style>
        """
    chat_plh_style = chat_plh_style % (id, color)

    st.markdown(chat_plh_style, unsafe_allow_html=True)
    return plh

create_container_with_color(999, color="green");
st.write('===================================================================================================================================================================')
#=========================================================
plh = st.container()
script = """<div id = 'chat_outer'></div>"""
st.markdown(script, unsafe_allow_html=True)

with plh:
    script = """<div id = 'chat_inner'></div>"""
    st.markdown(script, unsafe_allow_html=True)
    st.text("Random inner text")

st.text("Random outer text")

## applying style
chat_plh_style = """<style>
div[data-testid='stVerticalBlock']:has(div#chat_inner):not(:has(div#chat_outer)) {background-color: #E4F2EC};
</style>
"""

st.markdown(chat_plh_style, unsafe_allow_html=True)   
st.write('===================================================================================================================================================================')
#==========================================================
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.write('cool column box 1')
col2.write('cool column box 2')
col3.write('cool column box 3')
col4.write('cool column box 4')
col5.write('cool column box 5')
col6.write('cool column box 6')
st.write('===================================================================================================================================================================')
#===========================================================
st.write('===================================================================================================================================================================')
st.title("Text Display 123");st.title("Text Display 123");
st.write("Write content 456")
st.text("Text content... 789")
st.markdown("# Markdown content 123")
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.title("Title content 456")
st.header("Header content 789")
st.subheader("Sub header content 123")
st.code("[i for i in range(1,10)]")

st.title("Data Display 456");


    
import pandas as pd

df : pd.DataFrame = pd.DataFrame({"Col1":[1,2,3],
                                "Col2":['a','b','c']})

# st.write(df)
# st.table(df)
# st.json(df.to_dict())
# st.metric('My metric', 42, 2)

st.title("Display Media 789 789 789")
st.video("https://youtu.be/_OVnXw2ldog?si=2qsVAd3WdTUAlRVH")
st.image("data:image/png;base64,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")
#st.audio("urdu.mp3")