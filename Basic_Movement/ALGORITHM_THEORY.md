# Basic_Movement Directory - Algorithm & Theory Documentation

## constants.py

### Algorithms & Theory Used

#### **No Complex Algorithms**
- Simple constant definitions using direct assignment
- **Theory:** Static configuration pattern for maintainability

#### **Mathematical Calculations**
- `SCREENWIDTH = NCOLS * TILEWIDTH`
- `SCREENHEIGHT = NROWS * TILEHEIGHT`
- **Theory:** Derived values pattern - calculating dependent constants from base values

#### **Color Encoding**
- **RGB Color Model Theory:** Colors represented as tuples (Red, Green, Blue) with values 0-255
- Used for pygame rendering

#### **Directional Encoding Strategy**
- Opposite directions use negated values (UP=1, DOWN=-1; LEFT=2, RIGHT=-2)
- **Theory:** Allows easy direction reversal using multiplication by -1
- Enables `oppositeDirection` checks using `direction == self.direction * -1`

---

## vector.py

### Algorithms & Theory Used

#### **1. Vector Mathematics**
- **Linear Algebra Theory:** 2D vector representation and operations
- Implements mathematical vector space operations

#### **2. Operator Overloading**
```python
__add__, __sub__, __mul__, __div__, __eq__
```
- **Theory:** Pythonic design - makes Vector2 objects behave like mathematical vectors
- Enables intuitive syntax: `v1 + v2` instead of `v1.add(v2)`

#### **3. Vector Addition (`__add__`)**
- **Formula:** `(x1, y1) + (x2, y2) = (x1+x2, y1+y2)`
- **Use:** Calculate new positions by adding velocity vectors

#### **4. Vector Subtraction (`__sub__`)**
- **Formula:** `(x1, y1) - (x2, y2) = (x1-x2, y1-y2)`
- **Use:** Calculate direction vectors between two points

#### **5. Scalar Multiplication (`__mul__`)**
- **Formula:** `k * (x, y) = (k*x, k*y)`
- **Use:** Scale velocity by time or speed multiplier
- **Application:** `self.directions[direction] * self.speed * dt`

#### **6. Magnitude Calculation**
- **Euclidean Distance Formula:** `√(x² + y²)`
- **Pythagorean Theorem Applied:** Calculate vector length
- **Optimization:** `magnitudeSquared()` avoids expensive sqrt when only comparing distances

#### **7. Floating-Point Comparison**
- **Algorithm:** Threshold-based equality check
- **Theory:** Handles floating-point precision errors
- Compares `abs(x1 - x2) < threshold` instead of `x1 == x2`
- **Epsilon Comparison:** threshold = 0.000001

#### **8. Type Conversion Methods**
- `asTuple()`: Returns coordinate pair for pygame line drawing
- `asInt()`: Converts float coordinates to integers for pixel-perfect rendering
- **Theory:** Type casting for API compatibility

---

## pacman.py

### Algorithms & Theory Used

#### **1. Finite State Machine (FSM)**
- **States:** Direction states (STOP, UP, DOWN, LEFT, RIGHT)
- **Transitions:** Based on keyboard input and node validation
- **Theory:** Models Pacman's behavior as state-dependent logic

#### **2. Frame-Independent Movement**
- **Algorithm:** Position update using delta time
- **Formula:** `position += velocity * speed * dt`
- **Theory:** Ensures consistent movement speed regardless of frame rate
- **dt (delta time):** Time elapsed since last frame in seconds

#### **3. Node-Based Pathfinding**
- **Graph Traversal Theory:** Navigate through connected nodes
- Current implementation: Manual navigation without pathfinding algorithm
- **Target-based movement:** Move toward target node, update when reached

#### **4. Overshoot Detection Algorithm**
```python
vec1 = target.position - node.position
vec2 = position - node.position
return vec2.magnitudeSquared() >= vec1.magnitudeSquared()
```
- **Theory:** Compares distances using squared magnitudes (avoids sqrt)
- **Logic:** If distance traveled >= distance to target, we've reached/passed it
- **Optimization:** Uses `magnitudeSquared()` instead of `magnitude()` for performance

#### **5. Direction Validation Algorithm**
- **Graph Connectivity Check:** Verifies if movement direction has a valid edge
- **Algorithm:**
  1. Check if direction is not STOP
  2. Verify `node.neighbors[direction]` is not None
- **Theory:** Prevents movement through walls (non-existent edges)

#### **6. Opposite Direction Detection**
- **Algorithm:** `direction == self.direction * -1`
- **Mathematical Theory:** Uses the encoding scheme (UP=1/DOWN=-1, LEFT=2/RIGHT=-2)
- **Use:** Allows instant 180° turns for responsive controls

#### **7. Direction Reversal Algorithm**
```python
direction *= -1
swap(node, target)
```
- **Theory:** Reverses movement by negating direction and swapping current/target nodes
- Maintains continuous movement when player reverses direction

#### **8. Input Polling System**
- **Event-driven vs Polling:** Uses polling for continuous input response
- `pygame.key.get_pressed()`: Returns current state of all keys
- **Priority System:** First valid key press wins (UP > DOWN > LEFT > RIGHT > STOP)

#### **9. Target Selection Algorithm**
```python
if valid(direction):
    target = node.neighbors[direction]
else if valid(current_direction):
    target = node.neighbors[current_direction]
else:
    direction = STOP
```
- **Logic:** Try new direction, fallback to current direction, stop if blocked

#### **10. Rendering Algorithm**
- **Circle Rasterization:** Uses pygame's built-in circle drawing
- **Bresenham's Circle Algorithm** (internal to pygame): Efficient pixel plotting
- Converts float position to int for pixel alignment

---

## nodes.py

### Algorithms & Theory Used

#### **1. Graph Data Structure**
- **Theory:** Directed graph representation using adjacency lists
- **Nodes:** Vertices in the graph (positions in maze)
- **Edges:** Connections stored in `neighbors` dictionary

#### **2. Adjacency List Representation**
```python
neighbors = {UP: Node, DOWN: Node, LEFT: Node, RIGHT: Node}
```
- **Space Complexity:** O(4) per node (constant for 4-directional movement)
- **Time Complexity:** O(1) neighbor lookup using dictionary
- **Theory:** Efficient for sparse graphs (not all directions connected)

#### **3. Manual Graph Construction**
- `setupTestNodes()`: Hardcoded maze structure
- **Algorithm:** Create nodes, then manually link neighbors bidirectionally
- **Example:** `nodeA.neighbors[RIGHT] = nodeB` and `nodeB.neighbors[LEFT] = nodeA`
- **Theory:** Ensures graph consistency (bidirectional edges)

#### **4. Graph Traversal for Rendering**
```python
for node in nodeList:
    for neighbor in node.neighbors:
```
- **Algorithm:** Iterate through all nodes and their edges
- **Complexity:** O(V + E) where V=nodes, E=edges
- **Theory:** Standard graph traversal for visualization

#### **5. Line Drawing Algorithm**
- **Bresenham's Line Algorithm** (internal to pygame): Draws lines between nodes
- Connects node positions to show valid paths
- **Input:** Start tuple, end tuple from Vector2.asTuple()

#### **6. Circle Drawing for Nodes**
- **Rendering Algorithm:** Draw circle at each node position
- **Visual Theory:** Shows intersection points in the maze
- **Parameters:** Position (center), radius=12, color=RED

#### **7. Iterator Pattern**
```python
for n in self.neighbors.keys()
```
- **Design Pattern:** Iterate through dictionary keys to check all directions
- **Theory:** Enables clean traversal of all possible directions

---

## run.py

### Algorithms & Theory Used

#### **1. Game Loop Pattern**
```python
while True:
    update()
    render()
```
- **Theory:** Standard game architecture - continuous update/render cycle
- **Infinite Loop:** Runs until program exit

#### **2. Fixed Time Step Algorithm**
```python
dt = clock.tick(30) / 1000.0
```
- **Theory:** Caps frame rate at 30 FPS
- **Delta Time Calculation:** Converts milliseconds to seconds
- **Purpose:** Provides consistent timing for physics calculations
- **Formula:** `dt = elapsed_milliseconds / 1000`

#### **3. Model-View-Controller (MVC) Pattern**
- **Model:** Pacman, NodeGroup (game state)
- **View:** render() method (visualization)
- **Controller:** update(), checkEvents() (game logic and input)
- **Theory:** Separates concerns for maintainable code

#### **4. Event Queue Processing**
```python
for event in pygame.event.get():
```
- **Algorithm:** FIFO queue processing
- **Theory:** Event-driven programming for system events (QUIT, etc.)
- **pygame.event.get():** Dequeues all pending events

#### **5. Double Buffering**
```python
screen.blit(background, (0, 0))
nodes.render(screen)
pacman.render(screen)
pygame.display.update()
```
- **Theory:** Prevents screen tearing and flickering
- **Algorithm:**
  1. Draw to back buffer (screen surface)
  2. Flip buffers on display.update()
- **Layer Rendering Order:** Background → Nodes → Pacman (painter's algorithm)

#### **6. Initialization Sequence**
```python
pygame.init()
setBackground()
setupTestNodes()
create Pacman
```
- **Theory:** Dependency management - initialize in correct order
- **Pattern:** Setup phase before game loop

#### **7. Surface Blitting Algorithm**
- **Block Image Transfer (Blit):** Copy pixels from one surface to another
- **Formula:** `destination.blit(source, position)`
- **Theory:** Fast pixel array copying for rendering backgrounds

#### **8. Singleton Game Controller Pattern**
- Single `game` instance controls entire application
- **Theory:** Centralized game state management
- All subsystems accessible through one controller

---

## Cross-File Algorithmic Patterns

### **1. Separation of Concerns**
- **constants.py:** Configuration
- **vector.py:** Math utilities
- **nodes.py:** World representation
- **pacman.py:** Entity behavior
- **run.py:** Game orchestration

### **2. Object-Oriented Design**
- **Encapsulation:** Each class manages its own data
- **Abstraction:** Vector2 hides mathematical details
- **Composition:** GameController contains Pacman and NodeGroup

### **3. Coordinate Systems**
- **World Space:** Node positions (Vector2 with floats)
- **Screen Space:** Pixel coordinates (integers)
- **Conversion:** asInt() bridges the two systems

### **4. Performance Optimizations**
- **Squared Distance Comparison:** Avoids sqrt() calls
- **Fixed Frame Rate:** Predictable performance
- **Efficient Data Structures:** Dictionaries for O(1) lookups

---

## Theoretical Concepts Summary

| Concept | Files Used | Purpose |
|---------|-----------|---------|
| **Linear Algebra** | vector.py, pacman.py | 2D space mathematics |
| **Graph Theory** | nodes.py, pacman.py | Maze navigation |
| **Finite State Machines** | pacman.py | Behavior modeling |
| **Event-Driven Programming** | run.py | Input handling |
| **Game Loop Architecture** | run.py | Real-time simulation |
| **Operator Overloading** | vector.py | Intuitive math syntax |
| **MVC Pattern** | run.py | Code organization |
| **Frame-Independent Movement** | pacman.py, run.py | Consistent timing |
| **Adjacency Lists** | nodes.py | Graph representation |
| **Double Buffering** | run.py | Smooth rendering |

---

## Complexity Analysis

### Time Complexity
- **Movement Update:** O(1) - constant time vector operations
- **Direction Validation:** O(1) - dictionary lookup
- **Overshoot Check:** O(1) - simple arithmetic
- **Render All Nodes:** O(V + E) - visit all vertices and edges
- **Input Polling:** O(1) - fixed number of keys checked

### Space Complexity
- **Vector2:** O(1) - 2 floats + threshold
- **Node:** O(1) - position + 4 neighbor pointers
- **NodeGroup:** O(V) - list of all nodes
- **Pacman:** O(1) - fixed number of attributes
- **Total Graph:** O(V + E) - nodes + edges
