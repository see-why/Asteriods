SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
SHOT_RADIUS=5
PLAYER_SHOOT_SPEED=500
PLAYER_SHOOT_COOLDOWN=0.1

# Movement physics settings
# Set to True for inertia-based movement (ship continues moving when key released)
# Set to False for classic direct movement (ship stops immediately when key released)
PHYSICS_MOVEMENT = True
PLAYER_ACCELERATION = 600  # Acceleration when thrusting (only used if PHYSICS_MOVEMENT = True)
PLAYER_DRAG = 0.98  # Velocity multiplier per frame (0.98 = 2% drag, only used if PHYSICS_MOVEMENT = True)

# Difficulty settings
DIFFICULTY_EASY = "easy"
DIFFICULTY_MEDIUM = "medium"
DIFFICULTY_HARD = "hard"

DIFFICULTY_SETTINGS = {
    DIFFICULTY_EASY: {
        "spawn_rate": 1.2,
        "asteroid_speed_multiplier": 0.7,
        "starting_lives": 7
    },
    DIFFICULTY_MEDIUM: {
        "spawn_rate": 0.8,
        "asteroid_speed_multiplier": 1.0,
        "starting_lives": 5
    },
    DIFFICULTY_HARD: {
        "spawn_rate": 0.5,
        "asteroid_speed_multiplier": 1.5,
        "starting_lives": 3
    }
}