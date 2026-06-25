#Entity (SuperClass)
class Entity:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

#Treasure        
class Treasure(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 'T')

#Player        
class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, "@")
        self.health = 3
        
    def move(self, direction):
        new_x = self.x
        new_y = self.y
        if direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1
        if 0 <= new_x < 5 and 0 <= new_y < 5:
            self.x = new_x
            self.y = new_y
  
        
#Traps        
class Trap(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, "X")

    def check_collision(self, player):
        if self.x == player.x and self.y == player.y:
            player.health -= 1
            print("You stepped on a trap!")
            print("Health remaining:", player.health)
        
    
    
#Main loop
class GameManager():
    #Drawing the Grid             
    def draw_grid(self, treasure, player, trap_list):
        grid = [['.' for _ in range(5)] for _ in range(5)]
        
        for trap in trap_list:
            grid[trap.y][trap.x] = trap.symbol
            
        grid[treasure.y][treasure.x] = treasure.symbol
        grid[player.y][player.x] = player.symbol
        
        for row in grid:
            print("   ".join(row))
        print("\n")
    
    def main(self):
        player_obj = Player(0,0)
        treasure_obj = Treasure(4,4)
        trap_list = [Trap(2,2), Trap(1,3), Trap(4,2)]
        
        print("Welcome to the Labrynth!\n")
        
        game_over = False
        
        while not game_over:
            self.draw_grid(treasure_obj, player_obj, trap_list)
            action = input("Move using W (up), A (left), S (down), D (right) or Q to quit: ").lower()
            
            if action == 'q':
                print("Thanks for playing!")
                break
                
            direction = ""
            if action == "w":
                direction = "up"
            elif action == "s":
                direction = "down"
            elif action == "a":
                direction = "left"
            elif action == "d":
                direction = "right"
            
            #Check for Invalid input    
            if direction:
                player_obj.move(direction)
            else:
                print("Invalid input! Use W, A, S, or D.")
                continue
            
            #Check for collisions    
            for trap in trap_list:
                trap.check_collision(player_obj)
            
            #Check for player health    
            if player_obj.health <= 0:
                print("Game Over! You ran out of health.")
                game_over = True
            
            #Check to see whether player and treasure position coincide   
            if player_obj.x == treasure_obj.x and player_obj.y == treasure_obj.y:
                print("🎉 Victory! You found the treasure!")
                game_over = True
        

#Call the main function  
if __name__ == "__main__":
    manager = GameManager()
    manager.main()