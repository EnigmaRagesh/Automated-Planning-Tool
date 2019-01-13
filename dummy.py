# BFS Search implemented in the program pseudo code
visited = [state]
fringe = [state, None]
while fringe:
    state = fringe.pop(0)
    plan = fringe.pop(0)
    for act in actions:
        if self.applicable(state, act.positive_preconditions, act.negative_preconditions):
            new_state = self.apply(state, act.add_effects, act.del_effects)
            if new_state not in visited:
                if self.applicable(new_state, goal_pos, goal_not):
                    full_plan = [act]
                    while plan:
                        act, plan = plan
                        full_plan.insert(0, act)
                    return full_plan
                visited.append(new_state)
                fringe.append(new_state)
                fringe.append((act, plan))
return None