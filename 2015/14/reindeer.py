#!/usr/bin/env python

class Deer():
  def __init__(self, name, speed, duration, rest):
    self.name = name
    self.speed = int(speed)
    self.duration = int(duration)
    self.rest = int(rest)
    self.moved = 0
    self.running = 0
    self.rested = 0
    self.clock = 0
    self.points = 0

  def __repr__(self):
    return "<Deer name:%s speed:%d duration:%d rest:%d moved:%d running:%d rested:%d clock:%d self.points:%d>" % (self.name, self.speed, self.duration, self.rest, self.moved, self.running, self.rested, self.clock, self.points)

  def run(self, seconds):
    while seconds > 0:
      if self.running < self.duration:
        self.moved += self.speed
        self.running += 1
      else:
        self.rested += 1
        if self.rested >= self.rest:
          self.running = 0
          self.rested = 0
      self.clock += 1
      seconds -= 1

  def tick(self):
    self.run(1)

  def point(self):
    self.points += 1

class Simulation():
  def __init__(self, deer):
    self.deer = deer
    self.clock = 0

  def run(self, length):
    for i in range(length):
      longest = 0
      for d in self.deer:
        d.tick()
        if d.moved > longest:
          longest = d.moved
      for d in self.deer:
        if d.moved == longest:
          d.point()

  def winner_distance(self):
    longest_distance = 0
    for d in self.deer:
      if d.moved > longest_distance:
        longest_distance = d.moved
    return longest_distance

  def winner_points(self):
    most_points = 0
    for d in self.deer:
      if d.points > most_points:
        most_points = d.points
    return most_points

def parseLine(line):
  l = line.split()
  return Deer(l[0], l[3], l[6], l[13])

if __name__ == '__main__':
  with open('input', 'r') as f:
    lines = f.read().splitlines()

  deer = []
  for line in lines:
    deer.append(parseLine(line))

  s = Simulation(deer)
  s.run(2503)
  print s.winner_distance(), s.winner_points()
