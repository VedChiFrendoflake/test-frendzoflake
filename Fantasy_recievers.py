import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for the top 10 fantasy wide receivers (replace with actual data)
data = {
    'Player': [
        'CeeDee Lamb', 'Tyreek Hill', 'Amon-Ra St.Brown', 'Mike Evans', 
        'Puka Nacua', 'D.J. Moore', 'AJ Brown', 'Deebo Samuel', 
        'Nico Collins', 'Brandon Aiyuk'
    ],
    'Receptions': [
        135, 119, 119, 79, 105, 
        96, 106, 60, 80, 75
    ],
    'Receiving Yards': [
        1749, 1799, 1515, 1255, 1486, 1364, 
        1456, 892, 1297, 1342
    ],

    'Fantasy Points': [
        405, 376, 330, 282, 298, 
        286, 289, 243, 260, 249
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit title
st.title('Top 10 Fantasy Wide Receivers')

# Scatter plot
st.subheader('Scatter Plot of Receptions vs. Receiving Yards and Fantasy Points')
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot with color based on Fantasy Points
scatter = ax.scatter(df['Receptions'], df['Receiving Yards'], c=df['Fantasy Points'], cmap='viridis', s=100)

# Annotate each point with player names
for i in range(len(df)):
    ax.annotate(df['Player'][i], (df['Receptions'][i], df['Receiving Yards'][i]), fontsize=9)

# Add titles and labels
ax.set_title('Top 10 Fantasy Wide Receivers: Receptions vs. Receiving Yards')
ax.set_xlabel('Receptions')
ax.set_ylabel('Receiving Yards')

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Fantasy Points')

# Show the plot in Streamlit
st.pyplot(fig)

