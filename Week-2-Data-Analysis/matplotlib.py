import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a plot
plt.plot(x, y)

# Add a title and labels
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')

# Add a title and labels
plt.title('Multiple Lines Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()

# Show the plot
plt.show()import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a scatter plot
plt.scatter(x, y)

# Add a title and labels
plt.title('Simple Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]

# Create a bar plot
plt.bar(categories, values)

# Add a title and labels
plt.title('Simple Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show the plot
plt.show()import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create a histogram
plt.hist(data, bins=5)

# Add a title and labels
plt.title('Simple Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Create subplots
fig, axs = plt.subplots(2)

# First subplot
axs[0].plot(x, y1)
axs[0].set_title('First Subplot')

# Second subplot
axs[1].plot(x, y2)
axs[1].set_title('Second Subplot')

# Add a title to the figure
fig.suptitle('Multiple Subplots')

# Show the plot
plt.show()import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a plot with customizations
plt.plot(x, y, color='green', linestyle='--', marker='o')

# Add a title and labels
plt.title('Customized Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a plot
plt.plot(x, y)

# Add a title and labels
plt.title('Save Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Save the plot to a file
plt.savefig('plot.png')

# Show the plot
plt.show()