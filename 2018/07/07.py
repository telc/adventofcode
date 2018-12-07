#!/usr/bin/env python2.7

from collections import defaultdict

with open('input', 'r') as f:
  input_ = f.read().splitlines()

#input_ = """Step C must be finished before step A can begin.
#Step C must be finished before step F can begin.
#Step A must be finished before step B can begin.
#Step A must be finished before step D can begin.
#Step B must be finished before step E can begin.
#Step D must be finished before step E can begin.
#Step F must be finished before step E can begin.""".splitlines()

WORKERS = 5
TIME = 60

def solve(input_):
  steps = defaultdict(list)
  for line in input_:
    step, before = line[5], line[36]
    steps[step].append(before)
  work_steps = steps.copy()
  candidates = sorted(list(set(steps.keys()) - set([s for v in steps.values() for s in v])))
  order = []
  while len(candidates):
    for step in candidates:
      if step in order:
        candidates.remove(step)
        break
      if step not in [s for v in steps.values() for s in v]:
        order.append(step)
        candidates.pop(candidates.index(step))
        candidates = sorted(candidates + steps[step])
        steps[step] = []
        break 
  workers = []
  working = set()
  time = 0
  while time == 0 or len(workers):
    new_workers = []
    for worker in workers:
      if time == worker['time'] + ord(worker['step']) - ord('A') + 1 + TIME:
        if worker['step'] in work_steps:
          for s in work_steps[worker['step']]:
            if s not in work_steps:
              work_steps[s] = []
          del work_steps[worker['step']]
          working.remove(worker['step'])
      else:
        new_workers.append(worker)
    workers = new_workers
    ready = sorted(list(set(work_steps.keys()) - set([s for v in work_steps.values() for s in v]) - working))
    if len(ready):
      for w in xrange(min(len(ready), WORKERS - len(workers))):
        workers.append({'step': ready[w], 'time': time})
        working.add(ready[w])
    time += 1
  return ''.join(order), time - 1

if __name__ == '__main__':
  print solve(input_)
