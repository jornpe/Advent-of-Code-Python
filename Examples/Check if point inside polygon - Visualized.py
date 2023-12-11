from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt

# not square polygon
point = Point(2, 2)
point2 = Point(6, 2)
polygon = Polygon([(0, 0), (1, 0), (1, 1), (5, 1), (5, 5), (0, 5)])
print(polygon.contains(point))
print(polygon.contains(point2))

plt.plot(*polygon.exterior.xy)
plt.scatter(point.x, point.y)
plt.scatter(point2.x, point2.y)
plt.show()


