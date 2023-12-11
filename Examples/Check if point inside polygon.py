from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# is inside
point = Point(0.5, 0.5)
polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
print(polygon.contains(point))

# is outside
point2 = Point(2, 2)
polygon2 = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
print(polygon2.contains(point2))

# not square polygon
point2 = Point(2, 2)
polygon2 = Polygon([(0, 0), (0, 1), (1, 1), (5, 1), (5, 5), (0, 5)])
print(polygon2.contains(point2))
