import tkinter as tk
from itertools import permutations

# Function to calculate total distance
def calculate_distance(route, dist):
    total = 0
    for i in range(len(route) - 1):
        total += dist[route[i]][route[i+1]]
    total += dist[route[-1]][route[0]]  # return to start
    return total

# Solve TSP
def solve_tsp():
    cities = entry_cities.get().split(',')
    cities = [c.strip() for c in cities]

    n = len(cities)

    # Get distance matrix
    dist = []
    for i in range(n):
        row = list(map(int, entries[i].get().split(',')))
        dist.append(row)

    best_route = None
    min_dist = float('inf')

    for perm in permutations(range(n)):
        current_dist = calculate_distance(perm, dist)
        if current_dist < min_dist:
            min_dist = current_dist
            best_route = perm

    route_names = [cities[i] for i in best_route] + [cities[best_route[0]]]

    output.delete("1.0", tk.END)
    output.insert(tk.END, f"Optimal Route: {' -> '.join(route_names)}\n")
    output.insert(tk.END, f"Total Distance: {min_dist}")

# GUI setup
root = tk.Tk()
root.title("Tourist Travel Planner (TSP)")

tk.Label(root, text="Enter Cities (comma separated):").pack()
entry_cities = tk.Entry(root, width=40)
entry_cities.pack()

entries = []

def create_matrix():
    for widget in frame.winfo_children():
        widget.destroy()

    cities = entry_cities.get().split(',')
    n = len(cities)

    for i in range(n):
        tk.Label(frame, text=f"Distances from {cities[i]}:").grid(row=i, column=0)
        e = tk.Entry(frame)
        e.grid(row=i, column=1)
        entries.append(e)

frame = tk.Frame(root)
frame.pack()

tk.Button(root, text="Create Distance Matrix", command=create_matrix).pack()
tk.Button(root, text="Find Optimal Route", command=solve_tsp).pack()

output = tk.Text(root, height=10, width=50)
output.pack()

root.mainloop()
