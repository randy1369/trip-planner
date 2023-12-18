import streamlit as st
import json



st.set_page_config(layout="wide")

# Function to display information for each tourist place
def display_place_info(place_name, place_state):
    st.subheader(f"Information about {place_name}")
    file_path = f"json-files/{place_state}.json"

    with open(file_path, "r") as file:
        place_data = json.load(file)

       
        # Create tabs dynamically based on the available data
        tabs = st.tabs([attr for attr in place_data[place_name]])
        

        # Display information for each tab
        for tab_name, tab_data in zip(tabs, place_data[place_name].values()):
            
            with tab_name:
                
                # You can customize the content for each tab based on tab_data
                with st.expander("About-", expanded=True):
                    st.write(tab_data['description'])
                    image_url = tab_data['image']
                    st.image(image_url, width=600)

                with st.expander("Activities-"):
                    st.table(tab_data['activities'])

                with st.expander("Accommadation-"):
                    st.table(tab_data['accommodation'])

                with st.expander("Transportaion-"):
                    st.table(tab_data['transportation'])


# Main Streamlit app
def main():
    st.sidebar.title("Tourist Places")

    # Sidebar: Choose the tourist place
    chosen_state = st.sidebar.selectbox("Choose a state", ["kerala", "Goa", "Other States"])

    if chosen_state == "Kerala":
        # If Kerala is chosen, display sub-options
        chosen_place = st.sidebar.selectbox("Choose a tourist place in Kerala", ["Munnar", "Alappuzha", "Kochi", "Trivandrum", "Thekkady", "Wayanad"])

        # Display information for the selected place
        display_place_info(chosen_place, chosen_state)



if __name__ == "__main__":
    main()
