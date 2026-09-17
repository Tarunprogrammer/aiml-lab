import heapq

def solve_puzzle(start, goal):
  queue = [(0,start,[])]
  visited=set()

  while queue:
    _,state, path=heapq.heappop(queue)

    if state ==goal:
      return path

    if state in visited: continue
    visited.add(state)

    i=state.index(0)
    moves=[d for d in(i-3,i+3,i-1 if i%3 > 0 else-1,i+1 if i%3 < 2  else-1)if 0 <=d < 9]

    for m in moves:
      new_state=list(state)
      new_state[i],new_state[m]=new_state[m],new_state[i]
      new_state=tuple(new_state)

      cost=sum(1 for j in range(9) if new_state[j]!=0 and new_state[j]!=goal[j])
      heapq.heapush(queue,(cost,new_state,path+[new_state[i]]))

      start = (1, 2, 3, 4, 0, 5, 7, 6, 8)
      goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

      solution=solve_puzzle(start, goal)
      print("solution path")
      for move in solution:
        print(move)
