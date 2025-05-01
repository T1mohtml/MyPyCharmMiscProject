from graphviz import Digraph

# Create a directed graph
dot = Digraph(comment='Rejsekort Travel Flow')

# Define nodes
dot.node('A', 'Tap Rejsekort\n(Check-in)')
dot.node('B', 'Card saves check-in data\n(Location, Time, Type)')
dot.node('C', 'Terminal sends check-in\nto backend server (if online)')
dot.node('D', 'Travel...\n(card carries journey state)')
dot.node('E', 'Tap Rejsekort again\n(Check-out)')
dot.node('F', 'Terminal reads check-in data\nfrom card')
dot.node('G', 'Terminal calculates fare')
dot.node('H', 'Terminal sends completed trip\nto backend server')
dot.node('I', 'Backend updates final balance\nand travel history')

# Define edges between nodes
dot.edges([('A', 'B'), ('B', 'C'), ('B', 'D'),
           ('D', 'E'), ('E', 'F'), ('F', 'G'),
           ('G', 'H'), ('H', 'I')])

# Corrected output path for cross-platform compatibility
output_path = 'rejsekort_flowchart'

try:
    # Render the graph and save it as a PNG file
    dot.render(output_path, format='png', cleanup=True)
    print(f'Flowchart saved to {output_path}.png')
except Exception as e:
    print(f"An error occurred: {e}")