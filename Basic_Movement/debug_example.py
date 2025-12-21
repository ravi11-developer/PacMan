"""
DEBUG LOGGING TUTORIAL
======================
This file shows you how to use logging for debugging your code.
Copy these patterns into your own files!
"""

import logging

# ============================================================================
# STEP 1: SET UP LOGGING (Put this at the top of your file after imports)
# ============================================================================

# Configure logging - Change the level to control what you see:
# - logging.DEBUG: See EVERYTHING (most detailed)
# - logging.INFO: See important info only
# - logging.WARNING: See only warnings and errors (quietest)

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# ============================================================================
# STEP 2: USE LOGGING IN YOUR CODE
# ============================================================================

class ExampleGame:
    def __init__(self, width, height):
        # Debug message - shows when object is created
        logger.debug(f"Creating ExampleGame with width={width}, height={height}")
        
        self.width = width
        self.height = height
        self.score = 0
        self.players = []
        
        # Info message - for important milestones
        logger.info("ExampleGame initialized successfully")
    
    def addPlayer(self, name):
        # Debug what's happening in the function
        logger.debug(f"Adding player: {name}")
        
        self.players.append(name)
        
        # See the current state of a list/variable
        logger.debug(f"Current players list: {self.players}")
        logger.info(f"Player {name} joined. Total players: {len(self.players)}")
    
    def updateScore(self, points):
        old_score = self.score
        self.score += points
        
        # See before and after values
        logger.debug(f"Score updated: {old_score} -> {self.score} (added {points})")
    
    def processLoop(self):
        """Example of debugging loops"""
        logger.debug("Starting game loop")
        
        # Debug loop iterations
        for i in range(5):
            # You can see each iteration
            logger.debug(f"Loop iteration {i}")
            
            # Debug conditionals
            if i % 2 == 0:
                logger.debug(f"  {i} is even")
            else:
                logger.debug(f"  {i} is odd")
        
        logger.debug("Game loop completed")
    
    def checkCollision(self, x, y):
        """Example of debugging function calls and returns"""
        logger.debug(f"checkCollision called with x={x}, y={y}")
        
        # Debug calculations
        distance = (x**2 + y**2) ** 0.5
        logger.debug(f"Calculated distance: {distance}")
        
        collision = distance < 10
        
        # Debug the return value
        logger.debug(f"Returning collision={collision}")
        return collision

# ============================================================================
# EXAMPLE USAGE
# ============================================================================

def main():
    logger.info("=== Program started ===")
    
    # Create game instance
    game = ExampleGame(800, 600)
    
    # Add some players
    game.addPlayer("Alice")
    game.addPlayer("Bob")
    
    # Update score
    game.updateScore(10)
    game.updateScore(5)
    
    # Run a loop
    game.processLoop()
    
    # Check collision
    result = game.checkCollision(3, 4)
    logger.info(f"Collision result: {result}")
    
    logger.info("=== Program ended ===")

# ============================================================================
# COMMON DEBUG PATTERNS YOU CAN COPY
# ============================================================================

def debug_patterns_reference():
    """Copy these patterns into your code"""
    
    # 1. Debug variable values
    my_var = 42
    logger.debug(f"my_var = {my_var}")
    
    # 2. Debug when entering/exiting functions
    logger.debug("Entering functionName()")
    # ... function code ...
    logger.debug("Exiting functionName()")
    
    # 3. Debug loop iterations
    for i in range(10):
        logger.debug(f"Processing item {i}")
    
    # 4. Debug dictionary/list contents
    my_dict = {"key": "value", "count": 5}
    logger.debug(f"Dictionary contents: {my_dict}")
    
    # 5. Debug conditionals
    if True:
        logger.debug("Condition was True")
    else:
        logger.debug("Condition was False")
    
    # 6. Debug object attributes
    class MyClass:
        def __init__(self):
            self.x = 10
            logger.debug(f"Created MyClass with x={self.x}")
    
    # 7. Warning for potential issues (always shows)
    logger.warning("This is a potential problem!")
    
    # 8. Multiple variables at once
    x, y, z = 1, 2, 3
    logger.debug(f"Position: x={x}, y={y}, z={z}")

# ============================================================================
# HOW TO CONTROL OUTPUT
# ============================================================================

"""
TO SHOW ALL DEBUG MESSAGES (when developing):
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

TO SHOW ONLY IMPORTANT INFO (when testing):
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

TO HIDE DEBUG MESSAGES (when running normally):
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')

Just change ONE line at the top of your file!
"""

# ============================================================================
# RUN THIS FILE TO SEE EXAMPLES
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("RUNNING WITH logging.DEBUG - You'll see everything:")
    print("="*60 + "\n")
    
    main()
    
    print("\n" + "="*60)
    print("Now try changing line 19 to:")
    print("  logging.basicConfig(level=logging.INFO, ...)")
    print("And run again to see less output!")
    print("="*60 + "\n")
