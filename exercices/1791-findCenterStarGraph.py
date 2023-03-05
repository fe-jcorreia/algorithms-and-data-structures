def findCenter(edges):
  edge1 = edges[0]
  edge2 = edges[1]

  if edge1[0] in edge2:
    return edge1[0]
  else:
    return edge1[1]
