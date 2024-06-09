"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    # Class attribute to keep track of the number of Aliens created
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate, health=3):
        """Initialize the Alien object with coordinates and health."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = health
        Alien.total_aliens_created += 1

    def hit(self):
        """Decrement Alien health by one point."""
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        """Return a boolean for if Alien is alive (if health is > 0)."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move Alien object to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        """Implementation TBD."""
        pass

    def __repr__(self):
        """Return a string representation of the Alien object."""
        return (f'Alien(x_coordinate={self.x_coordinate}, '
                f'y_coordinate={self.y_coordinate}, health={self.health})')

def new_aliens_collection(coordinate_pairs):
    """Creating several aliens at once"""
    list_of_aliens = []
    for item in coordinate_pairs:
        list_of_aliens.append(Alien(item[0], item[1]))
    return list_of_aliens
