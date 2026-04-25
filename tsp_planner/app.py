import streamlit as st
from itertools import permutations

st.set_page_config(page_title="TSP Planner", layout="centered")

st.title("Tourist Travel Planner (TSP)")

# ---- Input: Cities ----
cities_input = st.text_input(
    "Enter cities (comma separated)",
    placeholder="Example: A,B,C"
)

cities = [c.strip() for c in cities_input.split(",") if c.strip()]
n = len(cities)

# ---- Input: Distance Matrix ----
dist = []
if n > 0:
    st.subheader("Enter Distance Matrix")
    st.caption("Enter each row as comma-separated numbers. Diagonal should be 0.")

    for i in range(n):
        row_str = st.text_input(
            f"Distances from {cities[i]}",
            placeholder="Example: 0,10,15",
            key=f"row_{i}"
        )
        if row_str:
            try:
                row = [int(x.strip()) for x in row_str.split(",")]
                dist.append(row)
            except:
                dist.append([])

# ---- TSP Logic ----
def calculate_distance(route, matrix):
    total = 0
    for i in range(len(route) - 1):
        total += matrix[route[i]][route[i + 1]]
    total += matrix[route[-1]][route[0]]  # return to start
    return total

def validate_matrix(matrix, n):
    if len(matrix) != n:
        return False, "Please enter all rows."
    for i, row in enumerate(matrix):
        if len(row) != n:
            return False, f"Row {i+1} must have {n} values."
    return True, ""

# ---- Solve Button ----
if st.button("Find Optimal Route"):
    if n < 2:
        st.error("Enter at least 2 cities.")
    else:
        ok, msg = validate_matrix(dist, n)
        if not ok:
            st.error(msg)
        else:
            min_dist = float("inf")
            best_route = None

            for perm in permutations(range(n)):
                d = calculate_distance(perm, dist)
                if d < min_dist:
                    min_dist = d
                    best_route = perm

            route_names = [cities[i] for i in best_route] + [cities[best_route[0]]]

            st.success("Optimal Route Found!")
            st.write("**Route:**", " → ".join(route_names))
            st.write("**Total Distance:**", min_dist)
