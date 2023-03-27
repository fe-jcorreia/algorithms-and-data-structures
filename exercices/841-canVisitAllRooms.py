def canVisitAllRooms(rooms):
  status = ['U'] * len(rooms)

  def dfs(initialVertex):
    status[initialVertex] = 'D'

    for nextVertex in rooms[initialVertex]:
      if status[nextVertex] == 'U':
        dfs(nextVertex)

    status[initialVertex] = 'P'

  dfs(0)
  if 'U' in status: return False
  return True


print(canVisitAllRooms([[1],[2],[3],[]]))
print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))