from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt

# Top 10 fantasy wide receivers from the last NFL season (replace with actual data)
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

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(df['Receptions'], df['Receiving Yards'], df['Fantasy Points'], color='blue')

# Annotate each point with player names
for i in range(len(df)):
    ax.text(df['Receptions'][i], df['Receiving Yards'][i], df['Fantasy Points'][i], df['Player'][i])

# Add titles and labels
ax.set_title('Top 10 Fantasy Wide Receivers: Receptions, Receiving Yards, and Fantasy Points')
ax.set_xlabel('Receptions')
ax.set_ylabel('Receiving Yards')
ax.set_zlabel('Fantasy Points')

# Show the plot
plt.show()
