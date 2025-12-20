# Basic_Movement  - Variable Documentation

## constants.py

### Screen Configuration Variables
| Variable | Data Type | Value | Use |
|----------|-----------|-------|-----|
| `TILEWIDTH` | `int` | 24 | Width of each tile in pixels |
| `TILEHEIGHT` | `int` | 24 | Height of each tile in pixels |
| `NROWS` | `int` | 36 | Number of rows in the game grid |
| `NCOLS` | `int` | 28 | Number of columns in the game grid |
| `SCREENWIDTH` | `int` | NCOLS*TILEWIDTH | Total screen width in pixels |
| `SCREENHEIGHT` | `int` | NROWS*TILEHEIGHT | Total screen height in pixels |
| `SCREENSIZE` | `tuple` | (SCREENWIDTH, SCREENHEIGHT) | Screen dimensions as a tuple for pygame |

### Color Constants
| Variable | Data Type | Value | Use |
|----------|-----------|-------|-----|
| `BLACK` | `tuple` | (0, 0, 0) | RGB color for black background |
| `YELLOW` | `tuple` | (255, 255, 0) | RGB color for Pacman |
| `WHITE` | `tuple` | (255, 255, 255) | RGB color for node connections |
| `RED` | `tuple` | (255, 0, 0) | RGB color for node circles |

### Direction Constants
| Variable | Data Type | Value | Use |
|----------|-----------|-------|-----|
| `STOP` | `int` | 0 | No movement direction |
| `UP` | `int` | 1 | Upward movement direction |
| `DOWN` | `int` | -1 | Downward movement direction |
| `LEFT` | `int` | 2 | Leftward movement direction |
| `RIGHT` | `int` | -2 | Rightward movement direction |

### Entity Constants
| Variable | Data Type | Value | Use |
|----------|-----------|-------|-----|
| `PACMAN` | `int` | 0 | Identifier constant for Pacman entity |

---

## vector.py

### Vector2 Class Instance Variables
| Variable | Data Type | Use |
|----------|-----------|-----|
| `self.x` | `float/int` | X coordinate of the 2D vector |
| `self.y` | `float/int` | Y coordinate of the 2D vector |
| `self.thresh` | `float` | Threshold (0.000001) for floating-point comparison to handle precision errors |

### Method Local Variables
| Variable | Data Type | Use |
|----------|-----------|-----|
| `other` | `Vector2` | Another vector for operations (add, subtract, equality) |
| `scalar` | `float/int` | Scalar value for multiplication/division operations |

---

## pacman.py

### Pacman Class Instance Variables
| Variable | Data Type | Use |
|----------|-----------|-----|
| `self.name` | `int` | Entity identifier (PACMAN constant) |
| `self.directions` | `dict` | Maps direction constants to Vector2 movement vectors |
| `self.direction` | `int` | Current movement direction (STOP/UP/DOWN/LEFT/RIGHT) |
| `self.speed` | `float` | Movement speed in pixels per second (100 * TILEWIDTH/16) |
| `self.radius` | `int` | Radius of Pacman circle for rendering (10 pixels) |
| `self.color` | `tuple` | RGB color for Pacman (YELLOW) |
| `self.node` | `Node` | Current node Pacman is at or just passed |
| `self.position` | `Vector2` | Current pixel position of Pacman on screen |
| `self.target` | `Node` | Target node Pacman is moving toward |

### Method Parameters and Local Variables
| Variable | Data Type | Use |
|----------|-----------|-----|
| `node` | `Node` | Initial node for Pacman (constructor parameter) |
| `dt` | `float` | Delta time in seconds for frame-independent movement |
| `direction` | `int` | Direction constant being checked or validated |
| `key_pressed` | `pygame.key.ScancodeWrapper` | Keyboard state array from pygame |
| `screen` | `pygame.Surface` | Display surface for rendering Pacman |
| `p` | `tuple` | Integer tuple of position for drawing (from asInt()) |
| `temp` | `Node` | Temporary variable for swapping nodes during reverse |
| `vec1` | `Vector2` | Vector from current node to target node |
| `vec2` | `Vector2` | Vector from current node to Pacman's position |
| `node2target` | `float` | Squared magnitude of distance to target |
| `node2Self` | `float` | Squared magnitude of distance to Pacman |

---

## nodes.py

### Node Class Instance Variables
| Variable | Data Type | Use |
|----------|-----------|-----|
| `self.position` | `Vector2` | Position of the node in pixel coordinates |
| `self.neighbors` | `dict` | Maps direction constants to neighboring Node objects (or None) |

### Node Class Method Variables
| Variable | Data Type | Use |
|----------|-----------|-----|
| `x` | `float/int` | X coordinate for node position (constructor parameter) |
| `y` | `float/int` | Y coordinate for node position (constructor parameter) |
| `screen` | `pygame.Surface` | Display surface for rendering |
| `n` | `int` | Direction key when iterating through neighbors |
| `line_str` | `tuple` | Start point of line (current node position as tuple) |
| `line_end` | `tuple` | End point of line (neighbor node position as tuple) |

### NodeGroup Class Instance Variables
| Variable | Data Type | Use |
|----------|-----------|-----|
| `self.nodeList` | `list` | List containing all Node objects in the game |

### NodeGroup Method Local Variables
| Variable | Data Type | Use |
|----------|-----------|-----|
| `nodeA` to `nodeG` | `Node` | Individual node objects for test maze setup |
| `node` | `Node` | Current node in iteration during rendering |

---

## run.py

### GameController Class Instance Variables
| Variable | Data Type | Use |
|----------|-----------|-----|
| `self.screen` | `pygame.Surface` | Main display surface (SCREENSIZE dimensions, 32-bit) |
| `self.background` | `pygame.Surface` | Background surface filled with BLACK color |
| `self.clock` | `pygame.time.Clock` | Clock object for controlling frame rate |
| `self.nodes` | `NodeGroup` | Container for all nodes in the game |
| `self.pacman` | `Pacman` | Pacman player object |

### Method Local Variables
| Variable | Data Type | Use |
|----------|-----------|-----|
| `dt` | `float` | Delta time in seconds (tick at 30 FPS / 1000.0) |
| `event` | `pygame.event.Event` | Event object from pygame event queue |

### Script-Level Variables
| Variable | Data Type | Use |
|----------|-----------|-----|
| `game` | `GameController` | Main game controller instance |

---

## Summary Statistics


- **Total Classes:** 4 (Vector2, Pacman, Node, NodeGroup, GameController)
- **Total Instance Variables:** 21
- **Total Method Parameters/Local Variables:** 20+
- **Primary Data Types Used:** int, float, tuple, dict, list, Vector2, Node, pygame objects
