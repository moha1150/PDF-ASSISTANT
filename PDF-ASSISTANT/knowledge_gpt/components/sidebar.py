import streamlit as st


def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key


def sidebar():
    with st.sidebar:
        st.markdown("# About")
        st.markdown(
            "📖P.A.A.L PDF Assistant allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
        )
        st.markdown(
            "This tool is a work in progress💡 "

        )
        st.markdown("---")
        st.markdown(
            "## How to use\n"
            "1. Enter your [P.A.A.L API key](https://paalmind.com) below🔑\n"
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Ask a question about the document💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your P.A.A.L API key here;",
            help="You can get your API key from https://paalmind.com",
            value=st.session_state.get("OPENAI_API_KEY", ""),
        )

        if api_key_input:
            set_openai_api_key(api_key_input)

        st.markdown("---")
        st.markdown("Made by P.A.A.L A.I.")
