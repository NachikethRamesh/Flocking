#Flocking
import Particle

width = 1000
height = 600

boids = []
for i in range(70):
    boid = Particle.Boid(width, height)
    boids.append(boid)

def setup():
    size(width, height)
    
def draw():
    background(0)
    
    for i in range(len(boids)):
        boids[i].update()
        boids[i].show()
        boids[i].flocking(boids)
    
    
    
