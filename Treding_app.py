import streamlit as st

st.set_page_config(
    page_title='Treding App',
    page_icon='charts_with_downwards_trend',
    layout = 'wide'
)

st.title("Treding Guide App:Bar_charts:")

st.header('We provide the greatest platform for you to collect all information prior to investing in stocks.')

st.image("stock.png")

st.markdown("## We provide the following services:")

st.markdown("## :one: Stock Information")
st.write("Through this page, you can see all information about the stock")

st.markdown("## :two: Stock Information")
st.write("you can explore predicted closing prices for the next 30 days based on historical stock data and advanced forecasting models.Use this tool to gain valuable insight into market trends and make informed investment decisions")

st.markdown("## :three: CAPM Return")
st.write("Discover how the Capital Asset Pricing Model(CAPM) calculates the expected return of different stocks asset based on its risk and market performance")

st.markdown("## :four: CAPM Beta")
st.write("Calculate Beta and Expected Return for individual Stocks")

