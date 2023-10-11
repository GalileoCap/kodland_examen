from shapely.geometry import Point as SHPoint
from shapely.geometry.polygon import Polygon as SHPolygon

def asShPoint(point):
  return SHPoint(point.x, point.y)

def asShPolygon(polygon, *, translate = True):
  return SHPolygon([asShPoint(point + (polygon.pos if translate else 0)) for point in polygon.points])

def fmtScore(score):
  return f'{score[0]} - {int(score[1])}'
