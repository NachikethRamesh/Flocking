class Boid:
    def __init__(self, width, height):
        self.boid = PVector(random(width), random(height))
        self.velocity = PVector.random2D()
        self.velocity.setMag(random(1, 3))
        self.acceleration = PVector();
        self.maxForce = 0.2
        self.maxVelocity = 4;
        
    def show(self):
        fill(255)
        noStroke()
        ellipse(self.boid.x, self.boid.y, 10, 10)
        
    def update(self):
        if(self.boid.x > width):
            self.boid.x = 0
        elif (self. boid.x < 0.1):
            self.boid.x = width
        elif (self.boid.y > height):
            self.boid.y = 0
        elif(self.boid.y < 0.1):
            self.boid.y = height
            
        self.boid.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxVelocity)
        self.acceleration.mult(0)
        
    def alignment(self, boids):
        visibleRadius = 40
        total = 0
        steering = PVector()
        for particle in boids:
            distance = dist(self.boid.x, self.boid.y, particle.boid.x, particle.boid.y)
            if (self != particle and distance <= visibleRadius):
                total += 1
                steering.add(particle.velocity)
        
        if(total > 0):
            steering.div(total)
            steering.setMag(self.maxVelocity)
            steering.sub(self.velocity)
            steering.limit(self.maxForce)
            
        return steering
        
    def cohesion(self, boids):
        visibleRadius = 30
        total = 0
        steering = PVector()
        for particle in boids:
            distance = dist(self.boid.x, self.boid.y, particle.boid.x, particle.boid.y)
            if(self != particle and distance <= visibleRadius):
                total += 1
                steering.add(particle.boid)
        
        if(total > 0):
            steering.div(total)
            steering.sub(self.boid)
            steering.setMag(self.maxVelocity)
            steering.sub(self.velocity)
            steering.limit(self.maxForce)
        
        return steering
        
        
    def separation(self, boids):
        visibleRadius = 25
        total = 0
        steering = PVector()
        for particle in boids:
            distance = dist(self.boid.x, self.boid.y, particle.boid.x, particle.boid.y)
            if (self != particle and distance <= visibleRadius):
                total += 1
                diff = PVector.sub(self.boid, particle.boid)
                steering.add(diff)
        
        if(total > 0):
            steering.div(total)
            steering.setMag(self.maxVelocity)
            steering.sub(self.velocity)
            steering.limit(self.maxForce)
            
        return steering
        
    def flocking(self, boids):
        align = self.alignment(boids)
        cohesion = self.cohesion(boids)
        separate = self.separation(boids)
        
        self.acceleration.add(align)
        self.acceleration.add(cohesion)
        self.acceleration.add(separate)
